# Day 13 — train_test_split & Training/Test Logic

The goal of Day 13 was to understand why Machine Learning datasets are separated into training and testing data.

## Topics Covered

- `train_test_split`
- Training set
- Test set
- `X_train`
- `X_test`
- `y_train`
- `y_test`
- `test_size`
- `random_state`
- Checking dataset sizes with `.shape`
- Why test data must remain unseen during training

## Train and Test Logic

```text
Dataset
   │
   ├── Training Set → Model learns
   │
   └── Test Set → Model is evaluated
```

The model learns from training data and is evaluated on data it did not see during training.

## train_test_split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

## test_size

`test_size=0.2` means:

```text
80% → Training
20% → Testing
```

## random_state

`random_state=42` makes the random split reproducible.

Using the same value produces the same train/test split again.

## Split Variables

```text
X_train → training features
y_train → training target values
X_test  → test features
y_test  → real test target values
```

## Checking the Split

```python
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
```

## Why Test Data Must Stay Unseen

If the model sees the test data during training, the test is no longer independent.

The purpose of the test set is to measure how well the model generalizes to data it has never seen before instead of simply memorizing examples.

## Final Understanding

By the end of Day 13, I can:

- Use `train_test_split`
- Split `X` and `y` into training and test sets
- Use `test_size`
- Use `random_state`
- Understand `X_train`, `X_test`, `y_train`, and `y_test`
- Check split dimensions with `.shape`
- Explain why test data must not be used during training

## Next

Day 14 → Linear Regression.
