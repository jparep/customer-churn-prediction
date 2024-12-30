CREATE DATABASE IF NOT EXISTS CUSTOMER_CHURN;
USE DATABASE CUSTOMER_CHURN;

CREATE TABLE IF NOT EXISTS CHURN_DATA (
    customerID STRING,
    gender STRING,
    SeniorCitizen INT,
    Partner STRING,
    Dependents STRING,
    tenure INT,
    PhoneService STRING,
    MultipleLines STRING,
    InternetService STRING,
    OnlineSecurity STRING,
    OnlineBackup STRING,
    DeviceProtection STRING,
    TechSupport STRING,
    StreamingTV STRING,
    StreamingMovies STRING,
    Contract STRING,
    PaperlessBilling STRING,
    PaymentMethod STRING,
    MonthlyCharges FLOAT,
    TotalCharges FLOAT,
    Churn STRING
);
