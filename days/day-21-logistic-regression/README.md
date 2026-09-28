# Day 21 — Logistic Regression + Sigmoid

Today I learned the fundamentals of binary classification using Logistic Regression.

## Topics Covered

- Logistic Regression
- Binary classification
- Sigmoid concept
- `predict()`
- `predict_proba()`
- Classification threshold
- Custom threshold logic
- Predictions on unseen data
- Train/test workflow for classification
- Accuracy score

## Logistic Regression

Logistic Regression is mainly used for classification problems.

Instead of predicting a continuous numerical value, the model predicts a class.

Example:

```text
0 = Not Purchased
1 = Purchased
```

Although the model is called Logistic Regression, it is commonly used for classification.

## Probability and Sigmoid

Logistic Regression internally produces probabilities between `0` and `1`.

Example:

```text
0.18 → low probability of class 1
0.84 → high probability of class 1
```

The sigmoid function is responsible for converting values into this probability range.

## predict()

`predict()` returns the final predicted class.

```python
predictions = model.predict(X_test)
```

Example:

```text
[0, 0, 1, 1]
```

## predict_proba()

`predict_proba()` returns the probabilities for every class.

```python
probabilities = model.predict_proba(X_test)
```

For binary classification, each row contains:

```text
[class_0_probability, class_1_probability]
```

To get only the probability of class `1`:

```python
class_1_probabilities = model.predict_proba(X_test)[:, 1]
```

## Classification Threshold

The default classification threshold is generally `0.5`.

```text
probability < 0.5  → class 0
probability >= 0.5 → class 1
```

The same logic can also be implemented manually:

```python
custom_predictions = []

for probability in probabilities:
    if probability >= 0.5:
        custom_predictions.append(1)
    else:
        custom_predictions.append(0)
```

## Predicting New Data

After training the model, predictions can be made on previously unseen data.

```python
new_customer = pd.DataFrame({
    "age": [37],
    "income": [44000]
})

prediction = model.predict(new_customer)
probability = model.predict_proba(new_customer)[:, 1]
```

## Accuracy

Accuracy measures how many predictions the model classified correctly.

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
```

For example:

```text
0.80 = 80% accuracy
```

## Final Understanding

By the end of Day 21, I can:

- Build a Logistic Regression model
- Understand the difference between regression and classification
- Use `predict()` for class predictions
- Use `predict_proba()` for probabilities
- Extract the probability of a specific class
- Understand classification thresholds
- Apply a threshold manually
- Predict previously unseen data
- Split classification data into train and test sets
- Evaluate a classification model using accuracy

## Next

Day 22 — Classification Evaluation