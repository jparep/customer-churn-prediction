# **Customer Churn Prediction for Subscription Business**

## **Project Overview**
This project predicts customer churn for a subscription-based business using machine learning and provides actionable insights for targeted retention strategies. The solution integrates data preprocessing, machine learning, clustering, and visualization using modern tools like Snowflake, Flask, Docker, and Tableau.

---

## **Features**
- Predict customer churn with a trained Random Forest model.
- Segment customers using K-means clustering.
- Dynamic visualizations in Tableau for churn and retention trends.
- Deployed as a REST API using Flask and Docker.

---

## **Technologies**
- **Programming Languages**: Python, SQL, R
- **Data Storage**: Snowflake
- **Machine Learning**: Scikit-learn
- **Visualization**: Tableau
- **Deployment**: Flask, Docker

---

## **Project Structure**
```
customer-churn-prediction/
├── app/
│   ├── __init__.py                # Initialize Flask app
│   ├── routes.py                  # API endpoints
├── models/
│   ├── churn_model.pkl            # Trained ML model
│   ├── model_training.py          # ML training script
│   ├── clustering.py              # Customer segmentation script
│   ├── upload_to_snowflake.py     # Script to upload data to Snowflake
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Raw dataset
│   ├── processed_data.csv         # Processed data for modeling
├── sql/
│   ├── load_data.sql              # SQL script to create and load Snowflake table
├── visualizations/
│   ├── tableau_dashboard.twbx     # Tableau dashboard file
├── Dockerfile                     # Dockerfile for containerizing the app
├── docker-compose.yml             # Docker Compose file (optional)
├── requirements.txt               # Python dependencies
├── config.py                      # Configuration for Snowflake and Flask
├── app.py                         # Flask entry point
├── README.md                      # Project documentation
└── .env                           # Environment variables
```

---

## **Setup and Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/jparep/customer-churn-prediction.git
cd customer-churn-prediction
```

### **2. Install Dependencies**
Install required Python libraries:
```bash
pip install -r requirements.txt
```

### **3. Configure Environment Variables**
Create a `.env` file in the root directory:
```plaintext
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
```

---

## **Data Preprocessing**

### **1. Load Data into Snowflake**
1. Use the SQL script in `sql/load_data.sql` to create the `CUSTOMER_CHURN` database and table.
2. Run the `models/upload_to_snowflake.py` script to upload data to Snowflake.

### **2. Fetch Data**
Fetch data from Snowflake into Python for processing:
```python
import pandas as pd
from snowflake.connector import connect

# Connection setup
conn = connect(user="your_username", password="your_password", account="your_account")
data = pd.read_sql("SELECT * FROM CUSTOMER_CHURN.CHURN_DATA", conn)
```

---

## **Machine Learning**

### **1. Train the Model**
Run the `models/model_training.py` script to train a Random Forest model:
```bash
python models/model_training.py
```

The trained model is saved as `models/churn_model.pkl`.

### **2. Customer Segmentation**
Run the `models/clustering.py` script to segment customers using K-means clustering:
```bash
python models/clustering.py
```

---

## **API Deployment**

### **1. Flask API**
Start the Flask application:
```bash
python app.py
```
The API will be accessible at `http://127.0.0.1:5000`.

#### **API Endpoint**
- **Predict Churn**: `POST /predict`
    - Input: JSON payload with customer features
    - Output: Predicted churn (0 or 1)

**Example**:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"features": [30, 50.0, ...]}' \
http://127.0.0.1:5000/predict
```

---

## **Docker Deployment**

### **1. Build Docker Image**
```bash
docker build -t customer-churn .
```

### **2. Run Docker Container**
```bash
docker run -p 5000:5000 customer-churn
```

---

## **Visualization**

1. Open Tableau or Power BI.
2. Connect to the Snowflake database.
3. Use the `visualizations/tableau_dashboard.twbx` file as a template or create your custom dashboard.

---

## **Future Improvements**
- Add real-time data streaming using Kafka.
- Implement deep learning models for better accuracy.
- Use SHAP for feature importance analysis.
- Enable multi-language support for the API.

---

## **License**
This project is licensed under the [MIT License](https://opensource.org/license/mit).

---

## **Acknowledgments**
- [Kaggle](https://www.kaggle.com/) for the dataset.
- [Snowflake](https://www.snowflake.com/) for cloud data storage.
- Open-source libraries and tools.
