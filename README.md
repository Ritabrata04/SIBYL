
<p align="center" width="100%">
    <a>
        <img src="NAGIVATE CAREER (7).png" alt="Title" style="display: block; margin: auto; border-radius: 50%; width: 50%; height: auto;">
    </a>
</p>


# SIBYL: STRATEGIC INTELLIGENCE FOR BUILDING YOUR LEGACY
<p align="center"> 
    <!-- Badges for Licenses, Status, etc. -->
</p>

SIBYL is a cutting-edge machine learning ensemble model designed to empower decision-making processes. Developed as part of Dell's Hack2Hire initiative, this project leverages the power of data-driven insights to shape your future strategies. Deployed using Streamlit, SIBYL offers a seamless and interactive user experience.


[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)]()

<p align="center" width="100%">
    <img src="sibyl-qr.png" alt="SIBYL Deployment" width="70%">
</p>

<!-- TOC -->

- [REPOSITORY STRUCTURE](#Repository-Structure)
- [DEPLOYMENT](#deployment)
- [TEAM](#team)
- [CITATION](#citation)
  

<!-- /TOC -->

## Project Structure

```
Employee-Career-Path-Navigator/
│
├── pythonFunctions       # Model training,prediction and GUI
├── data/                 # Dataset used for training and testing
├── .streamlit/           # Streamlit app deployment file
├── requirements.txt      # Dependencies for the project
└── README.md
```

## Deployment

To deploy SIBYL on Streamlit:

1. Clone the repository: 
   ```
   git clone https://github.com/Ritabrata04/Employee-Career-Path-Navigator.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Team

Meet the brilliant minds behind SIBYL:

<p align="center" width="100%">
    <img src="dell_team007.jpg" alt="Team" width="70%">
</p>
<p align="center">
    [From Right to Left] 
    <a href="https://github.com/Ritabrata04" target="_blank">Ritabrata</a>,
    <a href="https://github.com" target="_blank">Yashika</a>,
    <a href="https://github.com/tangorishi" target="_blank">Rishi</a>,
    <a href="https://github.com/AnkikaGithub" target="_blank">Ankika</a>,
    <a href="https://github.com/DivyangshuGithub" target="_blank">Divyangshu</a>
</p>


## Models

<p align="center" width="100%">
    <img src="Supplementary Materials/RANDOM FOREST.jpg" alt="Random Forest Model" width="70%">
    <br>Random Forest (RF)
</p>
<p>
    RF: Random Forest refers to a statistical machine learning approach which combines multiple decision trees to improve prediction accuracy and control over-fitting. This was chosen for its ease of handling large datasets with higher dimensional spaces. In our code, it enhances the job role prediction reliability by utilizing multiple decision trees.
</p>

<p align="center" width="100%">
    <img src="Supplementary Materials/DECISION TREE.png" alt="Decision Tree Model" width="70%">
    <br>Decision Tree (DT)
</p>
<p>
    DT: Decision Tree constructs a tree-like model of decisions based on the features of the dataset. It has been chosen for its effectiveness for classification of tasks due to its simplicity and interpretability. For our use case, it categorizes job roles based on various input features, making decisions at each node of the tree.
</p>

<p align="center" width="100%">
    <img src="Supplementary Materials/SVM MODEL.png" alt="SVM Model" width="70%">
    <br>Support Vector Machine (SVM)
</p>
<p>
    SVM: SVM is a powerful classifier that works by finding a hyperplane in an N-dimensional space (N — the number of features) that distinctly classifies the data points. It is known for its versatility and its effectiveness in high-dimensional spaces. Here, it segregates job roles as per feature set boundaries.
</p>

<p align="center" width="100%">
    <img src="Supplementary Materials/XGB MODEL.png" alt="XGBoost Model" width="70%">
    <br>XGBoost (XGB)
</p>
<p>
    XGB: XGBoost stands for eXtreme Gradient Boosting. It serves as an efficient and scalable implementation of the gradient boosting framework. It improves the model's performance by sequentially correcting errors made by previous trees. It serves as an optimal solution due to its speed and performance in structured data.
</p>

## Model Performance

<p align="center" width="100%">
    <img src="model_accuracies.jpg" alt="Model Accuracies" width="70%">
</p>
