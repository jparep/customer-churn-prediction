import snowflake.connector
import pandas as pd
import os

# Load Snowflake connection settings
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT
)

# Set the database context
cursor = conn.cursor()
cursor.execute("USE DATABASE CUSTOMER_CHURN_DB;")

# Load preprocessed data
data = pd.read_csv("data/processed_data.csv")

# Insert processed data into Snowflake
for _, row in data.iterrows():
    cursor.execute(
        """
        INSERT INTO CUSTOMER_CHURN (customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """,
        tuple(row)
    )

print("Processed data successfully loaded into Snowflake!")
