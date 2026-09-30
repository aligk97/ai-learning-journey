# Day 24 - K-Nearest Neighbors (KNN)

## Topics Covered

- K-Nearest Neighbors (KNN) classification
- How KNN uses distance between data points
- `n_neighbors` and the meaning of K
- Small K and overfitting
- Large K and underfitting
- Why feature scaling is important for KNN
- StandardScaler with KNN
- `KNeighborsClassifier`
- Training and predicting with scaled data

## Final Check

Built a KNN classification model using:

- Age
- Income
- Purchase status

The data was split into training and testing sets, scaled using `StandardScaler`, and classified using `KNeighborsClassifier` with `n_neighbors=3`.

Model performance was evaluated using accuracy.