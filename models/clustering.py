import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from preprocessing import load_data

# Load data
customer_data = load_data("data/raw/telco_customer_churn.csv")

# Features for clustering
features = customer_data[['tenure', 'MonthlyCharges']]

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(features)

# Save clustered data
customer_data.to_csv("data/processed/clustered_data_clustered.csv", index=False)

# Visualize clusters
plt.scatter(customer_data['tenure'], customer_data['MonthlyCharges'], c=customer_data['Cluster'])
plt.xlabel('Tenure')
plt.ylabel('Monthly Charges')
plt.title('Customer Clusters')
plt.show()