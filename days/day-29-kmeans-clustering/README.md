# Day 29 - K-Means Clustering

## Goal

Understand unsupervised learning and group unlabeled data with K-Means clustering.

## Topics Covered

- Unsupervised Learning
- K-Means clustering
- `n_clusters`
- Centroids
- `fit_predict()`
- `predict()`
- `cluster_centers_`
- Feature scaling with `StandardScaler`
- Inertia
- Elbow Method
- Silhouette Score
- K-Means limitations

## Key Concepts

K-Means is an unsupervised learning algorithm. There is no target variable (`y`). The model tries to discover groups inside the feature data.

`K` represents the number of clusters we want the model to create.

K-Means repeatedly assigns each sample to its nearest centroid and then updates each centroid using the mean of the samples assigned to that cluster.

`fit_predict()` learns the cluster structure and returns a cluster label for each training sample.

`predict()` assigns a new sample to the nearest already-learned centroid.

Cluster labels such as `0`, `1`, and `2` are only identifiers. Their numbers do not carry a special meaning.

Because K-Means is distance-based, features with very different scales can dominate the distance calculation. Scaling is therefore usually important.

`inertia_` measures within-cluster squared distance. Lower inertia means tighter clusters, but increasing K will naturally reduce inertia. The Elbow Method looks for a point where the improvement begins to slow down.

Silhouette Score helps evaluate how well-separated the clusters are. Values closer to 1 generally indicate clearer separation, values near 0 indicate overlap, and negative values can indicate poor assignments.

K-Means can be sensitive to outliers and is not ideal for every cluster shape.

## Final Check

`main.py`:

- Scales age and income
- Uses the Elbow Method for K values 1 through 6
- Builds a 3-cluster K-Means model
- Adds cluster labels to the DataFrame
- Prints the centroids
- Calculates Silhouette Score
- Predicts the cluster of a new customer

## Run

From the repository root:

```bash
uv run python days/day-29-kmeans-clustering/main.py
```

## Reference

[Scikit-learn: KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
