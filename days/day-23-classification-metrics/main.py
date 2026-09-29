import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split


# Minitask 1 - Accuracy, Precision, Recall, F1

y_test = [1, 1, 1, 1, 0, 0, 0, 0]
predictions = [1, 1, 0, 0, 1, 0, 0, 0]

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print("Minitask 1 - Classification Metrics")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)


# Day 23 - Final Check

students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                    1, 4, 6, 9],
    "attendance": [40, 45, 50, 55, 60, 65, 70, 75, 80, 90,
                   55, 60, 58, 68, 72, 78, 82, 88, 92, 95,
                   35, 62, 74, 86],
    "practice_score": [30, 35, 40, 45, 48, 52, 60, 68, 75, 88,
                       38, 42, 46, 55, 62, 70, 78, 84, 90, 94,
                       28, 50, 66, 82],
    "passed": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
               0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
               0, 0, 1, 1],
})

# 1. Feature sutunlarini X'e ata.

X = students[["study_hours", "attendance", "practice_score"]]

# 2. Target sutununu y'ye ata.

y = students["passed"]

# 3. Veriyi train ve test olarak ayir.
# test_size=0.3
# random_state=42

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y,
)

# 4. LogisticRegression modeli olustur ve egit.

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. X_test uzerinde tahmin yap.

predictions = model.predict(X_test)

# 6. Classification metriklerini hesapla.

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print("\nDay 23 - Final Check")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)
