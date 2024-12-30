import snowflake.connector
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

# Read the SQL file
with open("sql/load_data.sql", "r") as file:
    sql_script = file.read()

# Execute the SQL script
cursor = conn.cursor()
cursor.execute(sql_script)

print("Database and table created successfully!")
