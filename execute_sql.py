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

# Split the script into individual statements
statements = sql_script.split(";")
cursor = conn.cursor()

# Execute each statement individually
for statement in statements:
    statement = statement.strip()  # Remove leading/trailing spaces
    if statement:  # Execute non-empty statements
        print(f"Executing: {statement}")
        try:
            cursor.execute(statement)
        except snowflake.connector.errors.ProgrammingError as e:
            print(f"Error executing statement: {statement}")
            print(f"Error message: {e}")
            continue

print("Database and table creation script executed successfully!")
