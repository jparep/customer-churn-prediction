from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data/processed_data.csv")

# Features for clustering
features = data[['tenure', 'MonthlyCharges']]

# Perform K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['cluster'] = kmeans.fit_predict(features)

# Save results
data.to_csv("data/segmented_data.csv", index=False)

# Plot clusters
plt.scatter(data['tenure'], data['MonthlyCharges'], c=data['cluster'])
plt.title("Customer Segments")
plt.xlabel("Tenure")
plt.ylabel("Monthly Charges")
plt.show()
