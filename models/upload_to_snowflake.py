import snowflake.connector
import pandas as pd

# Snowflake connection config
conn = snowflake.connector.connect(
    user="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account="YOUR_ACCOUNT"
)

# Load raw data
data = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Upload data
for _, row in data.iterrows():
    conn.cursor().execute("""
        INSERT INTO CUSTOMER_CHURN.CHURN_DATA VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, tuple(row))
print("Data uploaded successfully!")
