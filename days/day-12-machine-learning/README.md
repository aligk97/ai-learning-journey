# Day 12 — Introduction to Machine Learning

The goal of Day 12 was to understand the basic parts of a Machine Learning problem before moving into train/test splitting.

## Topics Covered

- Features and target
- `X` and `y`
- Supervised Learning
- Unsupervised Learning
- Regression
- Classification
- New prediction data

## Features and Target

Features are the input variables used by the model.

```python
X = students[["study_hours", "attendance", "sleep_hours"]]
```

The target is the value that the model tries to predict.

```python
y = students["passed"]
```

## Supervised Learning

In supervised learning, the dataset contains known target values.

The model learns the relationship between `X` and `y`.

## Regression

Regression is used when the target is a continuous numerical value.

Examples:

- House price
- Salary
- Temperature
- Fuel consumption

## Classification

Classification is used when the target represents a class or category.

Examples:

- Passed / Failed
- Spam / Not Spam
- Fraud / Not Fraud

## Unsupervised Learning

In unsupervised learning, there is no known target variable.

The model tries to discover patterns, similarities, or groups in the data.

## New Prediction Data

New prediction data contains the features, but not the target we want to predict.

```python
new_car = pd.DataFrame({
    "horsepower": [175],
    "age": [5],
    "mileage": [85000]
})
```

There is no `price` column because `price` is the value we want to predict.

## Final Understanding

By the end of Day 12, I can:

- Identify features and targets
- Create `X` and `y`
- Distinguish supervised and unsupervised learning
- Distinguish regression and classification
- Understand why supervised learning needs known target values
- Prepare new data without including the target

## Next

Day 13 → `train_test_split` and training/test logic.
