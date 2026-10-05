# Day 30 - PCA (Principal Component Analysis)

## Goal

Understand dimensionality reduction and use PCA to represent data with fewer features while preserving as much information as possible.

## Topics Covered

- Dimensionality Reduction
- Principal Component Analysis (PCA)
- Principal Components (`PC1`, `PC2`, ...)
- Variance
- `StandardScaler`
- `PCA(n_components=...)`
- `fit_transform()` and `transform()`
- `explained_variance_ratio_`
- `n_components_`
- PCA before a Machine Learning model

## Key Concepts

PCA is a dimensionality reduction technique. It reduces the number of features by creating new features called principal components.

Principal components are combinations of the original features. They are not simply selected original columns.

`PC1` captures the direction with the highest variance in the data. `PC2` captures the next highest amount of remaining variance, and so on.

Because PCA is variance-based, features should usually be scaled before applying PCA.

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

PCA can be given a fixed number of components:

```python
pca = PCA(n_components=2)
```

Or it can automatically keep enough components to preserve a chosen amount of variance:

```python
pca = PCA(n_components=0.95)
```

`explained_variance_ratio_` shows how much variance each principal component explains.

```python
print(pca.explained_variance_ratio_)
```

When PCA is used with train/test data, the same preprocessing rule applies:

```python
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)
```

The test data must not be used to fit the scaler or PCA.

PCA is especially useful when a dataset contains many features. It can reduce model complexity and make high-dimensional data easier to visualize, but the new principal components are harder to interpret than the original feature names.

## Final Check

`main.py`:

- Creates a small classification dataset
- Splits the data into train and test sets
- Scales the features with `StandardScaler`
- Applies PCA while preserving at least 95% of the variance
- Prints the selected component count and explained variance
- Trains Logistic Regression on the PCA-transformed data
- Evaluates the model with accuracy

## Core Flow

```text
X
↓
StandardScaler
↓
PCA
↓
Model
↓
Prediction
```

## Run

From the repository root:

```bash
uv run python days/day-30-pca/main.py
```

## Reference

[Scikit-learn: PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
