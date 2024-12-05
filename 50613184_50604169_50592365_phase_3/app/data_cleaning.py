import pandas as pd
import numpy as np

file_path = 'merged_table.csv.xls'
data = pd.read_csv(file_path)

print("Initial Data Overview:")
print(data.info())

data.dropna(subset=['Price', 'Rank'], inplace=True)

print("Data after dropping rows with missing Price or Rank:")
print(data.info())

date_columns = ['InitialDateReported', 'MostRecentDateReported', 'DiscontinuedDate', 'ChemicalDateRemoved']
date_columns_2 = [col for col in date_columns if col in data.columns]
for col in date_columns_2:
    data[col] = pd.to_datetime(data[col], errors='coerce')

# Retain the Combination column and apply logic
if 'Combination' in data.columns:
    # If Combination is 1, set all other skin types to 0
    data.loc[data['Combination'] == 1, ['Dry', 'Normal', 'Oily', 'Sensitive']] = 0
else:
    print("Warning: 'Combination' column not found in the dataset. Ensure it is included in the input data.")

agg_data = data.groupby(['ProductName', 'PrimaryCategory', 'SubCategory', 'Label', 'Combination']).agg({
    'Price': 'mean',
    'Rank': 'mean',
    'ChemicalName': 'count',
    'ChemicalCount': 'mean',
    'Dry': 'max',
    'Normal': 'max',
    'Oily': 'max',
    'Sensitive': 'max'
}).reset_index()

agg_data['TotalChemicalScore'] = agg_data['ChemicalName']

agg_data['ChemicalCount'] = (agg_data['ChemicalCount'] - agg_data['ChemicalCount'].mean()) / agg_data['ChemicalCount'].std()

print("Aggregated Data with Unique Combinations:")
print(agg_data.head())

cleaned_file_path = 'output.csv'
agg_data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned and aggregated dataset saved to: {cleaned_file_path}")
