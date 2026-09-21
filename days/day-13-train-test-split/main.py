# minitask 1

# X_train
# Modelin eğitim sırasında kullandığı feature'lar.

# y_train
# X_train verilerinin gerçek target değerleri.
# Model eğitim sırasında bunlardan öğrenir.

# X_test
# Modeli test etmek için ayrılan
# ve training sırasında gösterilmeyen feature'lar.

# y_test
# X_test verilerinin gerçek target değerleri.
# Modelin tahminleriyle karşılaştırılır.

# Model test verisini training sırasında görmemelidir.
# Aksi halde test bağımsız bir sınav olmaz.
# Modelin hiç görmediği verilerde ne kadar iyi çalıştığını
# sağlıklı şekilde ölçemeyiz.


# minitask 2

import pandas as pd
from sklearn.model_selection import train_test_split

houses = pd.DataFrame({
    "size": [80, 120, 150, 200, 250, 170, 140, 220, 190, 110],
    "rooms": [2, 3, 3, 4, 5, 3, 3, 4, 4, 2],
    "age": [20, 15, 10, 8, 5, 12, 9, 6, 7, 18],
    "price": [250000, 350000, 420000, 550000, 700000,
              460000, 400000, 620000, 520000, 320000]
})

X = houses[["size", "rooms", "age"]]
y = houses["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(X_train)
print(X_test)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# minitask 3 - Day 13 Final Check

students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [55, 60, 65, 70, 75, 80, 85, 90, 92, 95],
    "sleep_hours": [5, 6, 6, 7, 6, 7, 8, 7, 8, 8],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

X = students[["study_hours", "attendance", "sleep_hours"]]
y = students["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

print(X_test)
print(y_test)

# Model neden test verisini eğitim sırasında görmemeli?
# Ezberlememek ve daha önce görmediği verilerde
# ne kadar iyi genelleme yaptığını ölçebilmek için.
