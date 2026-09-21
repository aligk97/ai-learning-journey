# Day 12 — Machine Learning Fundamentals

Today I started the Machine Learning section of my AI learning journey.

The goal of this day was to understand the fundamental concepts behind Machine Learning before training actual models.

## Topics Covered

- Features and target
- `X` and `y`
- Supervised Learning
- Unsupervised Learning
- Regression
- Classification
- Training data vs new/prediction data
- Train and test sets
- `X_train`
- `X_test`
- `y_train`
- `y_test`
- `train_test_split`
- `test_size`
- `random_state`
- Model predictions (`y_pred`)
- Comparing predictions with real values (`y_test`)

## Features and Target

Features are the input variables used by the model.

Example:

```python
X = students[["study_hours", "attendance", "sleep_hours"]]
```

The target is the value that the model tries to predict.

```python
y = students["passed"]
```

## Supervised Learning

In supervised learning, the training dataset contains both:

- Features (`X`)
- Target (`y`)

The model learns the relationship between them.

```text
X → Model → y
```

Example:

```text
study_hours
attendance
sleep_hours
      ↓
    Model
      ↓
   passed
```

## Regression

Regression is used when the target is a continuous numerical value.

Examples:

- House price
- Salary
- Temperature
- Fuel consumption
- Number of days

## Classification

Classification is used when the target represents a category or class.

Examples:

- Passed / Failed
- Spam / Not Spam
- Fraud / Not Fraud
- Purchased / Not Purchased

A target containing values such as `0` and `1` can still represent classification if those numbers represent classes.

## Unsupervised Learning

In unsupervised learning, there is no target variable.

The model tries to discover patterns, similarities or groups inside the data.

Example:

```text
Customer Features
       ↓
   Clustering
       ↓
Group 1 / Group 2
```

## Training Data vs New Data

During training:

```text
X + y
  ↓
Model learns
```

For a new prediction:

```text
X_new
  ↓
Model
  ↓
y_pred
```

The target is not included in new data because it is the value we want the model to predict.

Example:

```python
new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [82],
    "sleep_hours": [7]
})
```

There is no `passed` column because that is what the model will predict.

## Train and Test Data

The dataset is divided into training and testing parts.

```text
Dataset
   │
   ├── Training Set
   │      ↓
   │   Model learns
   │
   └── Test Set
          ↓
      Model is evaluated
```

The model learns using:

```text
X_train
y_train
```

The model is tested using:

```text
X_test
```

The model produces:

```text
y_pred
```

Then the predictions are compared with the real test targets:

```text
y_pred ↔ y_test
```

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

### test_size

```python
test_size=0.2
```

means:

```text
80% → Training
20% → Testing
```

### random_state

```python
random_state=42
```

keeps the random train/test split reproducible.

The number does not have to be `42`.

## Important Variables

```text
X_train → Training features

y_train → Real target values used during training

X_test → Features reserved for testing

y_test → Real target values reserved for testing

y_pred → Predictions produced by the model
```

The test data should not be used during training because we want to evaluate how well the model performs on data it has never seen before.

## Final Understanding

By the end of Day 12, I can:

- Identify features and targets
- Create `X` and `y`
- Distinguish supervised and unsupervised learning
- Distinguish regression and classification
- Understand why supervised learning requires target data
- Understand the difference between training and prediction data
- Create new prediction data
- Understand train and test sets
- Use `train_test_split`
- Understand `test_size`
- Understand `random_state`
- Understand `X_train`, `X_test`, `y_train`, and `y_test`
- Understand the relationship between `y_pred` and `y_test`

## Next

Day 13 → Training my first Machine Learning model.
