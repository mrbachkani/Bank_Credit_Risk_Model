# 🏦 Credit Risk Prediction App

## Overview

The **Credit Risk Prediction App** is a Streamlit-based web application that predicts credit risk using machine learning. By entering customer details such as loan duration, credit amount, and age, the app provides real-time predictions on creditworthiness. This project demonstrates skills in data analysis, XGBoost model building, and web deployment.

## Features

- **Interactive User Interface**: Uses Streamlit to provide an intuitive platform for inputting customer data.
- **Real-Time Predictions**: Predicts credit risk as either "Good Credit Risk" or "Bad Credit Risk" using a pre-trained model.
- **XGBoost Classifier**: Employs a robust XGBoost model trained on the Statlog (German Credit Data) dataset.

### Screenshot

## Skills Demonstrated

1. **Data Analysis**:
   - Explored and preprocessed the Statlog (German Credit Data) dataset using Pandas.
   - Engineered features relevant for credit risk assessment.
2. **Machine Learning**:
   - Trained an XGBoost classification model to predict credit risk.
   - Utilized Joblib for model persistence and deployment.
3. **Web Application Development**:
   - Developed an interactive web app using Streamlit.
   - Implemented user input elements (sliders, input fields) for dynamic predictions.

## Dataset Citation

The model was trained on the **Statlog (German Credit Data)** dataset, sourced from the UCI Machine Learning Repository.

Dataset Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data))

## Dataset Description

The Statlog (German Credit Data) dataset contains information about loan applicants and their credit risk status. It includes features such as:

-   **Duration**: Loan duration in months.
-   **Credit Amount**: The amount of credit requested.
-   **Age**: Age of the loan applicant.
-   **Installment Rate**: Installment rate as a percentage of disposable income.
-   **Personal Status Sex**: Personal status and sex of the applicant.
-   **Housing**: Type of housing (e.g., own, rent, or free).
-   **Job**: Type of job (e.g., unskilled, skilled, or management).
-   **Target**: Credit risk status (Good or Bad).

The dataset consists of 1000 instances and a mix of categorical and numerical attributes, making it suitable for credit risk assessment.
