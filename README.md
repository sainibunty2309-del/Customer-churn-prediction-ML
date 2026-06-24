# Telco customer churn prediction

This machine learning project predicts whether a customer will churn or not.

## Dataset
IBM Telco Customer Churn Dataset

## Project Workflow
- Import Libraries
- Load Dataset
- Dataset Information
- Data Cleaning
- EDA
- Feature Engineering
- Model Training
- Feature Importance
- Model Saving

## Algorithms Used
- Logistic Regression
- Decision Tree
- Random Forest

## Best Accuracy
Write your best accuracy here

## Project Visualization

### Confusion matrix
![Confusion matrix](screenshots/confusion%20matrix.png)

### Accuracy comparision
![Accuracy comparision](screenshots/model%20accuracy%20comparision.png)

### Correlation heatmap
![Heatmap](screenshots/correlation%20heatmap.png)

### Feature Importance
![Feature Importance](screenshots/Important%20Features.png)

### Monthly Charge Distribution
![Monthly Charges](screenshots/monthly%20charge%20distribution.png)

### Contract Type vs Churn
![Contract vs Churn](screenshots/contract%20type%20vs%20churn.png)

## Key Insights
- Customers with month-to-month contracts are more likely to churn.
- Customers with higher monthly charges have higher churn probability.
- Long-term customers are less likely to leave.
- Contract type and tenure were among the most important features.

## Model Deployment

The trained Random Forest model has been deployed as an interactive Streamlit web application. The deployment allows users to enter customer information through a user-friendly interface and receive real-time churn predictions.

Deployment features include:

- Interactive web interface built with Streamlit.
- Automatic loading of the trained model (churn_model.pkl).
- Automatic preprocessing using saved label encoders (label_encoders.pkl).
- Instant prediction of whether a customer is likely to churn  or SSstay.
- Easy deployment on platforms such as Streamlit Community Cloud or local environments.
# Conclusion

After comparing multiple machine learning models, 
Random Forest performed the best for predicting customer churn with the highest accuracy.

The project analysis showed that:

- Customers with month-to-month contracts are more likely to churn.
- Customers with higher monthly charges have higher churn probability.
- Long-term customers are less likely to leave.
- Contract type and tenure were among the most important features.

This project demonstrates how machine learning can help businesses identify customers at risk of leaving and improve retention strategies.
