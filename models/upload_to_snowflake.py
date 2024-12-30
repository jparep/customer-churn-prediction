import snowflake.connector
import pandas as pd
import numpy as np
import os
from preprocessing import load_data

# Load Snowflake connection settings
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")

# Establish connection
conn = None
try:
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
    )
    cursor = conn.cursor()

    # Set the database context
    cursor.execute("USE DATABASE CUSTOMER_CHURN_DB;")

    # Load raw data
    data_file = "data/raw/telco_customer_churn.csv"
    data = load_data(data_file)

    # Handle missing or invalid TotalCharges
    data['TotalCharges'] = data['TotalCharges'].replace(" ", np.nan)  # Replace empty strings with NaN
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')  # Convert to numeric
    # Optionally, fill NaN with 0 or the mean
    # data['TotalCharges'] = data['TotalCharges'].fillna(0)

    # Insert data row-by-row
    for _, row in data.iterrows():
        try:
            cursor.execute(
                """
                INSERT INTO CUSTOMER_CHURN (customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """,
                tuple(row)
            )
        except snowflake.connector.errors.ProgrammingError as e:
            print(f"Error inserting row: {row}")
            print(f"Error message: {e}")
            continue

    print("Processed data successfully loaded into Snowflake!")

except snowflake.connector.errors.Error as e:
    print(f"Snowflake error: {e}")

finally:
    if conn:
        conn.close()
        print("Connection closed.")
