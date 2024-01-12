#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install flask joblib pandas


from flask import Flask, request, jsonify
import joblib  # if you have saved your model using joblib
import pandas as pd

# Load your trained KNN model
model = joblib.load('knn_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract JSON content from request
    data = request.get_json(force=True)
    
    # Convert data to appropriate format (e.g., pandas DataFrame)
    # Note: Adjust this part based on how your model expects the input
    input_data = pd.DataFrame([data])

    # Preprocess the data if necessary

    # Generate predictions
    predictions = model.predict(input_data)

    # Convert predictions to JSON
    response = jsonify(predictions=predictions.tolist())

    return response

if __name__ == '__main__':
    app.run(debug=True)

