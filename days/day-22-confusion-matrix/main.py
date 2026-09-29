import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


# Minitask 1 - Confusion Matrix'i oku

y_test = [0, 0, 0, 0, 1, 1, 1, 1]
predictions = [0, 0, 1, 0, 1, 0, 1, 1]

cm = confusion_matrix(y_test, predictions)

print("Minitask 1 - Confusion Matrix")
print(cm)

tn, fp, fn, tp = cm.ravel()

print("TN:", tn)
print("FP:", fp)
print("FN:", fn)
print("TP:", tp)


# Day 22 - Final Check

students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "attendance": [40, 45, 50, 55, 60, 65, 70, 75, 80, 90,
                   55, 60, 58, 68, 72, 78, 82, 88, 92, 95],
    "passed": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
               0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
})

# 1. study_hours ve attendance sutunlarini X'e ata.

X = students[["study_hours", "attendance"]]

# 2. passed sutununu y'ye ata.

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

# 5. X_test icin predictions olustur.

predictions = model.predict(X_test)

# 6. confusion_matrix olustur.

cm = confusion_matrix(y_test, predictions)

print("\nDay 22 - Final Check")
print("Confusion Matrix:")
print(cm)

# Binary classification icin confusion matrix sirasi:
# [[TN, FP],
#  [FN, TP]]

tn, fp, fn, tp = cm.ravel()

print("True Negative:", tn)
print("False Positive:", fp)
print("False Negative:", fn)
print("True Positive:", tp)
