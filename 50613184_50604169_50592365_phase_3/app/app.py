from flask import Flask, request, jsonify, session
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
import secrets
import sqlite3

app = Flask(__name__)
CORS(app)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(16))


data = pd.read_csv('output.csv')# Load dataset

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Recommendation System API!"})

@app.route('/test', methods=['GET'])
def test_endpoint():
    return jsonify({"message": "Test successful!"})

@app.route('/routes', methods=['GET'])
def list_routes():
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        output.append(f"{rule.endpoint}: {rule.rule} [{methods}]")
    return jsonify(routes=output)

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

        # Get previously recommended products from the session
        previously_recommended = set(session.get('previously_recommended', []))  # Retrieve as list and convert to set

        filtered_data = data.copy()

        if skin_type:
            if skin_type == 'Combination':
                filtered_data = filtered_data[filtered_data['Combination'] == 1]
            elif skin_type in ['Dry', 'Normal', 'Oily', 'Sensitive']:
                filtered_data = filtered_data[(filtered_data[skin_type] == 1) & (filtered_data['Combination'] == 0)]

        if budget is not None:
            budget = float(budget)
            filtered_data = filtered_data[filtered_data['Price'] <= budget]

        if primary_category:
            filtered_data = filtered_data[filtered_data['PrimaryCategory'].str.contains(primary_category, case=False, na=False)]

        if sub_category:
            filtered_data = filtered_data[filtered_data['SubCategory'].str.contains(sub_category, case=False, na=False)]

        if label:
            filtered_data = filtered_data[filtered_data['Label'].str.contains(label, case=False, na=False)]

        
        filtered_data = filtered_data[~filtered_data['ProductName'].isin(previously_recommended)] # Exclude previously recommended products

        print(f"Filtered data: {filtered_data.shape[0]} rows remaining")

        if filtered_data.empty:
            return jsonify({"error": "No new products found matching the criteria"}), 404

        recommended_products = filtered_data.sort_values(by=['TotalChemicalScore', 'Rank'], ascending=[True, False]).head(5)
        
        new_recommendations = recommended_products['ProductName'].tolist()
        session['previously_recommended'] = list(previously_recommended.union(new_recommendations))  # Convert back to list

        return jsonify(recommended_products[['ProductName', 'PrimaryCategory', 'SubCategory', 'Label', 'Rank', 'Price']].to_dict(orient='records'))
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
    # works for local only