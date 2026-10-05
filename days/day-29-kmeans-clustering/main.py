import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


customers = pd.DataFrame({
    "age": [20, 22, 24, 26,
            35, 37, 39, 41,
            50, 52, 54, 56],
    "income": [20000, 23000, 25000, 28000,
               45000, 48000, 52000, 55000,
               75000, 78000, 82000, 85000]
})

X = customers[["age", "income"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method
inertias = []

for k in range(1, 7):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init="auto"
    )

    model.fit(X_scaled)
    inertias.append(model.inertia_)

plt.plot(range(1, 7), inertias, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# Final model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init="auto"
)

customers["cluster"] = model.fit_predict(X_scaled)

print(customers)

print("\nCentroids (scaled feature space):")
print(model.cluster_centers_)

score = silhouette_score(
    X_scaled,
    customers["cluster"]
)

print("\nSilhouette Score:", score)

# New customer
new_customer = pd.DataFrame({
    "age": [30],
    "income": [35000]
})

new_customer_scaled = scaler.transform(new_customer)
prediction = model.predict(new_customer_scaled)

print("\nNew Customer Cluster:", prediction[0])
