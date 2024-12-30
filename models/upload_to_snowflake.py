import snowflake.connector
import pandas as pd

# Snowflake connection settings
SNOWFLAKE_USER = "jpuser"
SNOWFLAKE_PASSWORD = "jppw123"
SNOWFLAKE_ACCOUNT = "jpacc"

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT
)

# Load raw data
data = pd.read_csv("data/raw/telco_customer_churn.csv")

# Create table if not exists
conn.cursor().execute("""
CREATE TABLE IF NOT EXISTS CUSTOMER_CHURN (
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
""")

# Insert data into Snowflake
for _, row in data.iterrows():
    conn.cursor().execute(
        """
        INSERT INTO CUSTOMER_CHURN VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """,
        tuple(row)
    )

print("Data successfully loaded into Snowflake!")