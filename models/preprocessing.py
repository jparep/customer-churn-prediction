import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def load_data(file_path):
    """Load raw data from a CSV file."""
    data = pd.read_csv(file_path)
    # Check for required columns
    required_columns = {'customerID', 'Churn'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Dataset must contain the following columns: {required_columns}")
    return data

def preprocess_data(data):
    """
    Preprocess the raw data:
    - Handle missing values.
    - Encode categorical variables.
    - Scale numerical features.
    """
    # Separate features and target
    X = data.drop(columns=['customerID', 'Churn'])
    y = data['Churn'].map({'Yes': 1, 'No': 0})  # Encode target variable

    # Define categorical and numerical columns
    categorical_cols = X.select_dtypes(include=['object']).columns
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns

    # Pipelines for preprocessing
    categorical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])
    numerical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(transformers=[
        ('num', numerical_pipeline, numerical_cols),
        ('cat', categorical_pipeline, categorical_cols)
    ])

    # Preprocess the data
    X_processed = preprocessor.fit_transform(X)

    return X_processed, y, preprocessor  # Return preprocessor for later use
