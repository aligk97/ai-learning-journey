# Day 26 - Final Check

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


customers = pd.DataFrame({
    "age": [
        18, 20, 21, 23, 25,
        27, 29, 31, 33, 35,
        38, 40, 42, 45, 48,
        50, 52, 55, 58, 60
    ],
    "income": [
        18000, 20000, 22000, 24000, 27000,
        30000, 32000, 35000, 38000, 40000,
        43000, 45000, 48000, 52000, 55000,
        58000, 62000, 65000, 70000, 75000
    ],
    "experience": [
        0, 1, 1, 2, 2,
        3, 3, 4, 4, 5,
        6, 6, 7, 8, 9,
        10, 11, 12, 13, 15
    ],
    "purchased": [
        0, 0, 0, 0, 0,
        0, 1, 0, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
})


# Features ve target
X = customers[["age", "income", "experience"]]
y = customers["purchased"]


# Train / Test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Random Forest modeli
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Modeli eğit
model.fit(X_train, y_train)


# Tahmin
y_pred = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# Feature Importance
print("\nFeature Importances:")
for feature, importance in zip(X.columns, model.feature_importances_):
    print(feature, importance)


# Gerçek değerler ve model tahminleri
print("\nGerçek Değerler:")
print(y_test.values)

print("\nTahminler:")
print(y_pred)
