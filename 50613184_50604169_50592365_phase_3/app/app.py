from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)
CORS(app) 
# Load dataset
data = pd.read_csv('output.csv')

#testing
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Recommendation System API!"})

# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        user_input = request.json
        skin_type = user_input.get('skin_type', None)
        budget = user_input.get('budget', None)
        primary_category = user_input.get('primary_category', None)
        sub_category = user_input.get('sub_category', None)
        label = user_input.get('label', None)

        print(f"Received input: skin_type={skin_type}, budget={budget}, primary_category={primary_category}, sub_category={sub_category}, label={label}")

        filtered_data = data.copy()

        if skin_type:
            if skin_type == 'Combination':
                filtered_data = filtered_data[filtered_data['Combination'] == 1]
            elif skin_type in ['Dry', 'Normal', 'Oily', 'Sensitive']:
                filtered_data = filtered_data[(filtered_data[skin_type] == 1) & (filtered_data['Combination'] == 0)]
            else:
                raise KeyError(f"Skin type '{skin_type}' not found in dataset columns")

        if budget is not None:
            budget = float(budget)
            if budget <= 0:
                return jsonify({"error": "Budget must be greater than 0"}), 400
            filtered_data = filtered_data[filtered_data['Price'] <= budget]

        if primary_category:
            filtered_data = filtered_data[filtered_data['PrimaryCategory'].str.contains(primary_category, case=False, na=False)]

        if sub_category:
            filtered_data = filtered_data[filtered_data['SubCategory'].str.contains(sub_category, case=False, na=False)]

        if label:
            filtered_data = filtered_data[filtered_data['Label'].str.contains(label, case=False, na=False)]

        print(f"Filtered data: {filtered_data.shape[0]} rows remaining")

        if filtered_data.empty:
            return jsonify({"error": "No products found matching the criteria"}), 404

        # Sort and recommend based on lowest TotalChemicalScore and highest Rank
        recommended_products = filtered_data.sort_values(by=['TotalChemicalScore', 'Rank'], ascending=[True, False]).head(5)

        print(f"Recommended products: {recommended_products[['ProductName', 'TotalChemicalScore', 'Rank', 'Price']]}")

        return jsonify(recommended_products[['ProductName', 'PrimaryCategory', 'SubCategory', 'Label', 'Rank', 'Price']].to_dict(orient='records'))
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
