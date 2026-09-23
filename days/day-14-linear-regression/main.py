import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Day 14 - Final check
students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "score": [42, 48, 53, 58, 64, 69, 74, 80, 84, 90, 94, 98]
})

X = students[["study_hours"]]
y = students["score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

results = pd.DataFrame({
    "study_hours": X_test["study_hours"].values,
    "actual_score": y_test.values,
    "predicted_score": predictions
})

print("Day 14 - Linear Regression Final Check")
print(results)

coefficient = model.coef_[0]
intercept = model.intercept_

print("Coefficient:", coefficient)
print("Intercept:", intercept)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("MAE:", mae)
print("MSE:", mse)
print("R2:", r2)

new_student = pd.DataFrame({
    "study_hours": [7.5]
})

model_prediction = model.predict(new_student)
manual_prediction = intercept + coefficient * 7.5

print("Model prediction:", model_prediction[0])
print("Manual prediction:", manual_prediction)

plt.figure()
plt.scatter(students["study_hours"], students["score"])

regression_predictions = model.predict(X)

plt.plot(students["study_hours"], regression_predictions)
plt.title("Study Hours vs Score - Linear Regression")
plt.xlabel("Study Hours")
plt.ylabel("Score")

plt.show()
