# # Minitask 1 - First Logistic Regression

# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# students = pd.DataFrame({
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "passed":      [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# })

# # 1. study_hours sütununu X değişkenine ata.
# # X DataFrame olarak kalmalı.

# X = students[["study_hours"]]

# # 2. passed sütununu y değişkenine ata.

# y = students["passed"]

# # 3. LogisticRegression modelini oluştur.

# logistic_model = LogisticRegression()


# # 4. Modeli X ve y ile eğit.

# logistic_model.fit(X, y)


# # 5. Tüm öğrenciler için tahmin yap ve predictions değişkenine ata.

# predictions = logistic_model.predict(X)


# # 6. predictions değerini print et.

# print(predictions)



# # Minitask 2 - predict_proba

# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# students = pd.DataFrame({
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "passed":      [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# })

# X = students[["study_hours"]]
# y = students["passed"]

# model = LogisticRegression()

# model.fit(X, y)

# # 1. X içerisindeki tüm öğrencilerin
# # sınıf olasılıklarını hesapla.
# # Sonucu probabilities değişkenine ata.

# probabilities = model.predict_proba(X)


# # 2. probabilities değişkenini print et.

# print(probabilities)

# # 3. Sadece passed=1 olasılıklarını al.
# # Bunun için probabilities içerisindeki ikinci sütunu seç.
# # Sonucu passed_probabilities değişkenine ata.

# passed_probabilities = probabilities[:,1]


# # 4. passed_probabilities değişkenini print et.

# print(passed_probabilities)


# Minitask 3 - Classification Threshold


# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# students = pd.DataFrame({
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "passed":      [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# })

# X = students[["study_hours"]]
# y = students["passed"]

# model = LogisticRegression()
# model.fit(X, y)

# probabilities = model.predict_proba(X)[:, 1]

# # 1. Threshold değerini 0.5 olarak oluştur.

# threshold = 0.5

# # 2. probabilities içindeki her değer için:
# # probability >= threshold ise 1,
# # değilse 0 olacak şekilde tahminler oluştur.
# # Sonucu custom_predictions değişkenine ata.

# custom_predictions = []

# for probability in probabilities:
#     if(probability >= threshold):
#         custom_predictions.append(1)

#     else:
#         custom_predictions.append(0)

# # 3. custom_predictions değerini print et.

# print(custom_predictions)

# # 4. model.predict(X) sonucunu sklearn_predictions
# # değişkenine ata ve print et.

# sklearn_predictions = model.predict(X)
# print(sklearn_predictions)


# Minitask 4 - New Data Prediction

# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# students = pd.DataFrame({
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "passed":      [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# })

# X = students[["study_hours"]]
# y = students["passed"]

# model = LogisticRegression()
# model.fit(X, y)

# new_student = pd.DataFrame({
#     "study_hours": [4.5]
# })

# # 1. new_student için sınıf tahmini yap.
# # Sonucu prediction değişkenine ata.

# prediction = model.predict(new_student)

# # 2. prediction değerini print et.

# print(prediction)

# # 3. new_student için sınıf olasılıklarını hesapla.
# # Sonucu probability değişkenine ata.

# probability = model.predict_proba(new_student)


# # 4. probability değerini print et.

# print(probability)


# # 5. Sadece passed=1 olasılığını al
# # ve passed_probability değişkenine ata.

# passed_probability = probability[:,1]


# # 6. passed_probability değerini print et.

# print(passed_probability)


# Minitask 5 - Classification Accuracy

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score

# students = pd.DataFrame({
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                     11, 12, 13, 14, 15, 16],
#     "passed":      [0, 0, 0, 0, 0, 0, 0, 1,
#                     1, 1, 1, 1, 1, 1, 1, 1]
# })

# # 1. study_hours sütununu X değişkenine ata.
# # X DataFrame olarak kalmalı.

# X = students[["study_hours"]]

# # 2. passed sütununu y değişkenine ata.

# y = students["passed"]

# # 3. Veriyi train ve test olarak ayır.
# # test_size=0.25
# # random_state=42

# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=42)

# # 4. LogisticRegression modelini oluştur.

# model = LogisticRegression()


# # 5. Modeli yalnızca train verisiyle eğit.

# model.fit(X_train, y_train)


# # 6. X_test üzerinde tahmin yap.
# # Sonucu predictions değişkenine ata.

# predictions = model.predict(X_test)


# # 7. y_test ve predictions kullanarak
# # accuracy hesapla.
# # Sonucu accuracy değişkenine ata.

# accuracy = accuracy_score(y_test, predictions)


# # 8. accuracy değerini print et.

# print(accuracy)


# Day 21 - Final Check

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

customers = pd.DataFrame({
    "age": [18, 20, 21, 23, 25, 27, 29, 31, 33, 35,
            38, 40, 42, 45, 48, 50, 52, 55, 58, 60],
    "income": [18000, 20000, 22000, 24000, 27000,
               30000, 32000, 35000, 38000, 40000,
               43000, 45000, 48000, 52000, 55000,
               58000, 62000, 65000, 70000, 75000],
    "purchased": [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 1,
                  0, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
})

# 1. age ve income sütunlarını X değişkenine ata.

X = customers[["age","income"]]

# 2. purchased sütununu y değişkenine ata.

y = customers["purchased"]

# 3. Veriyi train ve test olarak ayır.
# test_size=0.25
# random_state=42

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 4. LogisticRegression modelini oluştur.

model = LogisticRegression()

# 5. Modeli train verisiyle eğit.

model.fit(X_train, y_train)

# 6. X_test üzerinde tahmin yap.
# Sonucu predictions değişkenine ata.

predictions = model.predict(X_test)

# 7. Accuracy hesapla ve print et.

accuracy = accuracy_score(y_test, predictions)
print(accuracy)
# 8. X_test için purchased=1 olasılıklarını hesapla.
# Sonucu purchase_probabilities değişkenine ata.

purchase_probabilities = model.predict_proba(X_test)[:, 1]


# 9. purchase_probabilities değerini print et.

print(purchase_probabilities)


# 10. Aşağıdaki yeni müşteri için sınıf tahmini yap ve print et.

new_customer = pd.DataFrame({
    "age": [37],
    "income": [44000]
})

print(model.predict(new_customer))


# 11. Aynı yeni müşteri için purchased=1 olasılığını
# hesapla ve print et.

print(model.predict_proba(new_customer)[:,1])