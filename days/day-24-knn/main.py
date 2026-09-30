# Day 24 - Final Check

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

customers = pd.DataFrame({
    "age": [18, 20, 21, 23, 25, 27, 29, 31, 33, 35,
            38, 40, 42, 45, 48, 50, 52, 55, 58, 60],
    "income": [18000, 20000, 22000, 24000, 27000,
               30000, 32000, 35000, 38000, 40000,
               43000, 45000, 48000, 52000, 55000,
               58000, 62000, 65000, 70000, 75000],
    "purchased": [0, 0, 0, 0, 0,
                  0, 0, 1, 0, 1,
                  1, 1, 0, 1, 1,
                  1, 1, 1, 1, 1]
})


# 1. age ve income sütunlarını X değişkenine ata.

X = customers[["age", 'income']]


# 2. purchased sütununu y değişkenine ata.

y = customers["purchased"]

# 3. Veriyi train ve test olarak ayır.
# test_size=0.25
# random_state=42

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=42)

# 4. StandardScaler oluştur.

scaler = StandardScaler()

# 5. X_train verisini fit_transform ile scale et.

X_train_scaled = scaler.fit_transform(X_train)

# 6. X_test verisini sadece transform ile scale et.

X_test_scaled = scaler.transform(X_test)

# 7. KNeighborsClassifier oluştur.
# n_neighbors=3 kullan.

model = KNeighborsClassifier(n_neighbors=3)

# 8. Modeli scaled train verisiyle eğit.

model.fit(X_train_scaled, y_train)

# 9. Scaled test verisi üzerinde tahmin yap.

predictions = model.predict(X_test_scaled)

# 10. Accuracy hesapla.

accuracy = accuracy_score(y_test, predictions )

# 11. predictions ve accuracy sonuçlarını yazdır.

print(predictions)

print('-----')

print(accuracy)

