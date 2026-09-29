# # # Minitask 1 - Confusion Matrix'i oku

# # from sklearn.metrics import confusion_matrix

# # y_test = [0, 0, 0, 0, 1, 1, 1, 1, 1, 0]

# # predictions = [0, 0, 1, 0, 1, 0, 1, 1, 0, 0]

# # # 1. y_test ve predictions kullanarak confusion matrix oluştur.

# # cm = confusion_matrix(y_test, predictions)

# # print(cm)

# # # 2. Sonucu print et.

# # # 3. Çıkan matrise bakarak aşağıdaki değerleri kendin yaz:
# # # TN = 4
# # # FP = 1
# # # FN = 2
# # # TP = 3


# # Minitask 2 - Logistic Regression + Confusion Matrix

# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import confusion_matrix

# customers = pd.DataFrame({
#     "age": [
#         18, 20, 21, 23, 25, 27, 29, 31, 33, 35,
#         38, 40, 42, 45, 48, 50, 52, 55, 58, 60
#     ],
#     "income": [
#         18000, 20000, 22000, 24000, 27000,
#         30000, 32000, 35000, 38000, 40000,
#         43000, 45000, 48000, 52000, 55000,
#         58000, 62000, 65000, 70000, 75000
#     ],
#     "purchased": [
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 1,
#         0, 1, 1, 1, 1,
#         1, 1, 1, 1, 1
#     ]
# })

# # 1. age ve income sütunlarını X değişkenine ata.

# X = customers[["age", "income"]]

# # 2. purchased sütununu y değişkenine ata.
# y  = customers["purchased"]

# # 3. Veriyi train ve test olarak ayır.
# # test_size=0.3
# # random_state=42

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # 4. LogisticRegression modeli oluştur.

# model = LogisticRegression(max_iter=1000)


# # max_iter=1000 kullan.

# # 5. Modeli train verisiyle eğit.
# model.fit(X_train, y_train)
# # 6. X_test için tahmin yap ve predictions değişkenine ata.

# predictions = model.predict(X_test)

# # 7. y_test ve predictions kullanarak confusion matrix oluştur.

# cm = confusion_matrix(y_test, predictions)

# # 8. Confusion matrix'i print et.

# print(cm)
# # 9. Çıkan matrise bakarak yorum satırı olarak yaz:
# # TN = 4
# # FP = 0
# # FN = 0
# # TP = 2


# # Minitask 3 - Confusion Matrix değerlerini ravel() ile ayır

# from sklearn.metrics import confusion_matrix

# y_test = [0, 0, 1, 1, 0, 1, 0, 1]

# predictions = [0, 1, 1, 0, 0, 1, 0, 0]

# # 1. confusion_matrix oluştur ve cm değişkenine ata.

# cm = confusion_matrix(y_test, predictions)
# print(cm)

# # 2. cm.ravel() kullanarak değerleri:
# # tn, fp, fn, tp
# # değişkenlerine ata.

# tn,fp,fn,tp = cm.ravel()

# # 3. TN değerini print et.

# # 4. FP değerini print et.

# # 5. FN değerini print et.

# # 6. TP değerini print et.


# # Day 22 - Final Check

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 5, 6, 7, 8, 4, 9, 1, 10],
    "attendance": [40, 45, 50, 55, 60, 65, 70, 75, 80, 90,
                   55, 65, 70, 80, 85, 90, 45, 95, 35, 88],
    "passed": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
               0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
})

# 1. study_hours ve attendance sütunlarını X'e ata.

X = students[["study_hours", "attendance"]]

# 2. passed sütununu y'ye ata.

y = students['passed']

# 3. Veriyi train ve test olarak ayır.
# test_size=0.3
# random_state=42

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3, random_state=42)

# 4. LogisticRegression modeli oluştur.
# max_iter=1000

model = LogisticRegression(max_iter=1000)
# 5. Modeli eğit.
model.fit(X_train, y_train)
# 6. X_test için predictions oluştur.

predictions = model.predict(X_test)

# 7. confusion_matrix oluştur ve cm değişkenine ata.

cm = confusion_matrix(y_test, predictions)

# 8. cm'yi print et.

print(cm)

# 9. cm.ravel() kullanarak:
# tn, fp, fn, tp
# değişkenlerini oluştur.

tn, fp, fn, tp = cm.ravel()

# 10. Sonuçlara bakarak yorum satırı olarak şunları yaz:
# TN neyi ifade ediyor?
# FP neyi ifade ediyor?
# FN neyi ifade ediyor?
# TP neyi ifade ediyor?

#biliyorum hepsini sorun yok