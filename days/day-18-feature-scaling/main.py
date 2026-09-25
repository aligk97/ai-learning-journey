# Day 18 - Feature Scaling

# minitask 1 - StandardScaler

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

employees = pd.DataFrame({
    "age": [22, 25, 28, 32, 35, 40, 45, 50, 55, 60],
    "experience": [1, 2, 4, 6, 8, 12, 16, 20, 25, 30],
    "salary": [25000, 30000, 38000, 45000, 52000,
               65000, 78000, 90000, 110000, 135000]
})

X = employees[["age", "experience", "salary"]]

X_train, X_test = train_test_split(
    X,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled_df = pd.DataFrame(
    X_train_scaled,
    columns=X.columns
)

print(X_train)
print(X_train_scaled_df)


# minitask 2 - fit, transform ve fit_transform mantığı

train_data = pd.DataFrame({
    "salary": [30000, 40000, 50000, 60000, 70000]
})

test_data = pd.DataFrame({
    "salary": [35000, 80000]
})

scaler = StandardScaler()

scaler.fit(train_data)

print(scaler.mean_)
print(scaler.scale_)

train_scaled = scaler.transform(train_data)
test_scaled = scaler.transform(test_data)

print("train scaled:", train_scaled)
print("test scaled:", test_scaled)

# Scaler sadece train verisinden öğrenir.
# Test verisine aynı öğrenilen ölçek uygulanır.
# Test verisinde tekrar fit yapmak data leakage oluşturur.


# minitask 3 - StandardScaler vs MinMaxScaler

from sklearn.preprocessing import MinMaxScaler

data = pd.DataFrame({
    "age": [20, 25, 30, 35, 40],
    "salary": [20000, 30000, 50000, 70000, 100000]
})

standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(data)

standard_scaled_df = pd.DataFrame(
    standard_scaled,
    columns=data.columns
)

minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(data)

minmax_scaled_df = pd.DataFrame(
    minmax_scaled,
    columns=data.columns
)

print(data)
print(standard_scaled_df)
print(minmax_scaled_df)

# StandardScaler verileri 0 etrafında toplar
# ve standart sapmayı yaklaşık 1 yapar.
#
# MinMaxScaler minimum değeri 0, maksimum değeri 1 yapar
# ve diğer değerleri bu aralığa ölçekler.
