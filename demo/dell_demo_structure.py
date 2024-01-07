#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#REQUIRED DEPENDENCIES


# In[1]:


import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split


# In[2]:


data = pd.read_csv('synthetic_career_data.csv')  # Your dataset file


# In[3]:


# Convert the 'career_switches' into a numerical feature (count of switches)
data['number_of_switches'] = data['career_switches'].apply(lambda x: len(x.split(',')))

# Define which features are numerical and which are categorical
numerical_features = ['experience_years', 'number_of_switches']  # Add all numerical feature names
categorical_features = ['education_level', 'current_technology', 'job_title', 'required_technology']  # Add all categorical feature names


# In[4]:


# Create transformers for numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Define the KNN model
knn = NearestNeighbors(n_neighbors=5, algorithm='auto')


# In[5]:


# Create a pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', knn)])


# In[6]:


# Fit the model with the data
pipeline.fit(data)


# In[7]:


#MAKING RECOMMENDATIONS


# In[11]:


def make_recommendations(user_profile, pipeline):
    # Transform the user profile into the appropriate format (e.g., DataFrame)
    user_df = pd.DataFrame([user_profile])

    # Preprocess the user profile using the pipeline
    preprocessed_user = pipeline.named_steps['preprocessor'].transform(user_df)

    # Use the fitted KNN model to find nearest neighbors
    knn_model = pipeline.named_steps['model']
    distances, indices = knn_model.kneighbors(preprocessed_user)

    # Print the recommended career paths
    print("Recommended Career Paths:")
    for i in indices[0]:
        print(data.iloc[i]['job_title'])  # Adjust based on your actual job title column

# Example usage:
make_recommendations(user_profile_example, pipeline)


# In[ ]:




