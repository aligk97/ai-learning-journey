from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Create a dataset with multiple features
X, y = make_classification(
    n_samples=300,
    n_features=10,
    n_informative=6,
    n_redundant=2,
    random_state=42
)

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Keep enough principal components to preserve at least 95% variance
pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

print("Original feature count:", X_train.shape[1])
print("PCA component count:", pca.n_components_)
print("Explained variance ratios:", pca.explained_variance_ratio_)
print("Total explained variance:", pca.explained_variance_ratio_.sum())

# Train a model using PCA-transformed features
model = LogisticRegression(max_iter=1000)
model.fit(X_train_pca, y_train)

y_pred = model.predict(X_test_pca)

print("Accuracy:", accuracy_score(y_test, y_pred))
