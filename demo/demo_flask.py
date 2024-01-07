#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install flask')


# In[ ]:


from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Assuming your pipeline and data are loaded here
pipeline = ...  # Your trained pipeline
data = pd.read_csv('your_data.csv')  # Your dataset

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Extract user profile from the POST request
        user_profile = request.json
        
        # Validate and transform the user profile here as necessary
        # ...

        # Make recommendations
        user_df = pd.DataFrame([user_profile])
        preprocessed_user = pipeline.named_steps['preprocessor'].transform(user_df)
        knn_model = pipeline.named_steps['model']
        distances, indices = knn_model.kneighbors(preprocessed_user)

        # Prepare the recommendations to be sent back
        recommendations = data.iloc[indices[0]]['job_title'].tolist()  # Adjust based on your data
        return jsonify({'recommendations': recommendations})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


# # Interact with the API## 
# You can interact with this API by sending a POST request to the /recommend endpoint with a JSON object containing the user profile

# In[ ]:


#curl -X POST -H "Content-Type: application/json" -d '{"experience_years": 5, "number_of_switches": 2, "education_level": "Bachelor", "current_technology": "Python", "job_title": "Data Scientist", "required_technology": "Python"}' http://127.0.0.1:5000/recommend


# ## testing from python using requests library

# In[ ]:


import requests

user_profile = {
    "experience_years": 5,
    "number_of_switches": 2,
    "education_level": "Bachelor",
    "current_technology": "Python",
    "job_title": "Data Scientist",
    "required_technology": "Python"
}

response = requests.post("http://127.0.0.1:5000/recommend", json=user_profile)
print(response.json())

