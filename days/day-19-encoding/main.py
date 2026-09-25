# # minitask 1 - Basic Encoding

# import pandas as pd

# employees = pd.DataFrame({
#     "name": ["Ali", "Ayse", "Mehmet", "Zeynep", "Can", "Ece"],
#     "remote": ["Yes", "No", "Yes", "No", "Yes", "No"]
# })

# # 1. employees DataFrame'ini yazdır.

# print(employees)

# # 2. remote sütunundaki unique değerleri yazdır.
# print(employees["remote"].unique())

# # 3. Bir dictionary oluştur:
# # "No"  -> 0
# # "Yes" -> 1

# my_dict = {
#     "No": 0,
#     "Yes": 1
# }


# # 4. map() kullanarak remote sütununu sayısal hale getir.
# # Sonucu yeni bir "remote_encoded" sütununa kaydet.

# employees["remote_encoded"] = employees['remote'].map(my_dict)


# # 5. Son DataFrame'i yazdır.

# print(employees)


# # minitask 2 - One-Hot Encoding with get_dummies()

# import pandas as pd

# employees = pd.DataFrame({
#     "name": ["Ali", "Ayse", "Mehmet", "Zeynep", "Can", "Ece"],
#     "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", "Ankara", "Izmir"],
#     "salary": [45000, 42000, 47000, 51000, 44000, 49000]
# })

# # 1. employees DataFrame'ini yazdır.

# print(employees)

# # 2. city sütunundaki unique değerleri yazdır.

# print(employees["city"].unique())

# # 3. pd.get_dummies() kullanarak
# # sadece city sütununu one-hot encode et.
# # Sonucu city_encoded isimli değişkene kaydet.

# city_encoded = pd.get_dummies(employees["city"])


# # 4. city_encoded değişkenini yazdır.

# print(city_encoded)

# # 5. city_encoded sütunlarının isimlerini yazdır.

# print(city_encoded.columns)



# # minitask 3 - Merge One-Hot Encoded Columns

# import pandas as pd

# employees = pd.DataFrame({
#     "name": ["Ali", "Ayse", "Mehmet", "Zeynep", "Can", "Ece"],
#     "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", "Ankara", "Izmir"],
#     "salary": [45000, 42000, 47000, 51000, 44000, 49000]
# })

# # 1. city sütununu pd.get_dummies() ile encode et.
# # Sonucu city_encoded değişkenine kaydet.

# city_encoded = pd.get_dummies(employees["city"])


# # 2. pd.concat() kullanarak
# # employees ve city_encoded DataFrame'lerini
# # sütun bazında yan yana birleştir.
# # Sonucu employees_encoded değişkenine kaydet.

# employees_encoded = pd.concat([employees, city_encoded], axis=1)


# # 3. employees_encoded DataFrame'ini yazdır.

# print(employees_encoded)

# # 4. employees_encoded içinden
# # orijinal city sütununu sil.

# employees_encoded.drop('city', axis=1, inplace=True)

# # 5. Son DataFrame'i tekrar yazdır.

# print(employees_encoded)


# minitask 4 - drop_first

# import pandas as pd

# employees = pd.DataFrame({
#     "name": ["Ali", "Ayse", "Mehmet", "Zeynep", "Can", "Ece"],
#     "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", "Ankara", "Izmir"],
#     "salary": [45000, 42000, 47000, 51000, 44000, 49000]
# })

# # 1. city sütununu normal pd.get_dummies() ile encode et.
# # Sonucu encoded_all değişkenine kaydet.

# encoded_all = pd.get_dummies(employees['city'])

# # 2. encoded_all DataFrame'ini yazdır.

# print(encoded_all)

# # 3. city sütununu tekrar encode et.
# # Bu kez drop_first=True kullan.
# # Sonucu encoded_drop değişkenine kaydet.

# encoded_drop = pd.get_dummies(employees["city"], drop_first=True)

# # 4. encoded_drop DataFrame'ini yazdır.

# print(encoded_drop)

# # 5. encoded_all sütun sayısını yazdır.

# print(len(encoded_all.columns))

# # 6. encoded_drop sütun sayısını yazdır.
# print(len(encoded_drop.columns))




# # minitask 5 - OneHotEncoder

# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder

# employees = pd.DataFrame({
#     "name": ["Ali", "Ayse", "Mehmet", "Zeynep", "Can", "Ece"],
#     "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", "Ankara", "Izmir"],
#     "salary": [45000, 42000, 47000, 51000, 44000, 49000]
# })

# # 1. OneHotEncoder oluştur.
# # sparse_output=False kullan.
# # encoder isimli değişkene kaydet.

# encoder = OneHotEncoder(sparse_output=False)

# # 2. employees içindeki city sütununa
# # fit_transform() uygula.
# # DİKKAT: city sütununu DataFrame olarak gönder.
# # Sonucu encoded_city değişkenine kaydet.

# encoded_city = encoder.fit_transform(employees[["city"]])

# # 3. encoded_city sonucunu yazdır.

# print(encoded_city)

# # 4. encoder.get_feature_names_out()
# # kullanarak oluşan sütun isimlerini yazdır.

# print(encoder.get_feature_names_out())

# # 5. encoded_city'nin shape değerini yazdır.

# print(encoded_city.shape)


# # minitask 6 - Train/Test Encoding

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder

# employees = pd.DataFrame({
#     "city": [
#         "Istanbul", "Ankara", "Izmir", "Istanbul",
#         "Ankara", "Izmir", "Istanbul", "Ankara"
#     ],
#     "experience": [1, 2, 3, 4, 5, 6, 7, 8],
#     "salary": [35000, 37000, 40000, 43000, 46000, 50000, 54000, 58000]
# })

# # 1. city ve experience sütunlarını X değişkenine ata.
# X = employees[["city", 'experience']]

# print(X)

# # 2. salary sütununu y değişkenine ata.

# y = employees['salary']

# # 3. Veriyi train ve test olarak ayır.
# # test_size=0.25
# # random_state=42

# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state=42)


# # 4. OneHotEncoder oluştur.
# # sparse_output=False kullan.
# # handle_unknown="ignore" kullan.
# # encoder değişkenine kaydet.

# encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")


# # 5. Encoder'ı sadece X_train içindeki city sütununa
# # fit_transform() ile uygula.
# # Sonucu train_city_encoded değişkenine kaydet.

# train_city_encoded = encoder.fit_transform(X_train[["city"]])


# # 6. Aynı encoder'ı X_test içindeki city sütununa
# # sadece transform() ile uygula.
# # Sonucu test_city_encoded değişkenine kaydet.

# test_city_encoded = encoder.transform(X_test[["city"]])


# # 7. train_city_encoded değerini yazdır.

# print(train_city_encoded)

# # 8. test_city_encoded değerini yazdır.

# print(test_city_encoded)

# # 9. encoder.get_feature_names_out() sonucunu yazdır.

# print(encoder.get_feature_names_out())


# # minitask 7 - Build Encoded Feature DataFrames

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder

# employees = pd.DataFrame({
#     "city": [
#         "Istanbul", "Ankara", "Izmir", "Istanbul",
#         "Ankara", "Izmir", "Istanbul", "Ankara"
#     ],
#     "experience": [1, 2, 3, 4, 5, 6, 7, 8],
#     "salary": [35000, 37000, 40000, 43000, 46000, 50000, 54000, 58000]
# })

# # 1. city ve experience sütunlarını X'e ata.

# X = employees[["city", "experience"]]

# # 2. salary sütununu y'ye ata.

# y = employees["salary"]

# # 3. Train/test split yap.
# # test_size=0.25
# # random_state=42

# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=42)


# # 4. OneHotEncoder oluştur.
# # sparse_output=False
# # handle_unknown="ignore"

# encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")


# # 5. X_train city sütununa fit_transform() uygula.
# # train_city_encoded değişkenine kaydet.

# train_city_encoded = encoder.fit_transform(X_train[["city"]])

# # 6. X_test city sütununa sadece transform() uygula.
# # test_city_encoded değişkenine kaydet.

# test_city_encoded = encoder.transform(X_test[['city']])


# # 7. train_city_encoded değerini DataFrame'e çevir.
# # columns için:
# # encoder.get_feature_names_out(["city"])
# #
# # index için:
# # X_train.index
# #
# # Sonucu train_city_df değişkenine kaydet.

# train_city_df = pd.DataFrame(
#     train_city_encoded,
#     columns=encoder.get_feature_names_out(["city"]),
#     index=X_train.index
# )



# # 8. test_city_encoded değerini de aynı şekilde DataFrame'e çevir.
# # index=X_test.index kullan.
# # Sonucu test_city_df değişkenine kaydet.

# test_city_df = pd.DataFrame(
#     test_city_encoded,
#     columns=encoder.get_feature_names_out(["city"]),
#     index=X_test.index
# )



# # 9. X_train içindeki experience sütunu ile
# # train_city_df'yi pd.concat(..., axis=1) ile birleştir.
# # Sonucu X_train_ready değişkenine kaydet.

# X_train_ready = pd.concat([train_city_df, X_train['experience']], axis=1)


# # 10. X_test içindeki experience sütunu ile
# # test_city_df'yi aynı şekilde birleştir.
# # Sonucu X_test_ready değişkenine kaydet.

# X_test_ready = pd.concat([test_city_df, X_test["experience"]], axis=1)


# # 11. X_train_ready değerini yazdır.

# print(X_train_ready)

# # 12. X_test_ready değerini yazdır.


# Day 19 - Final Check

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

employees = pd.DataFrame({
    "city": [
        "Istanbul", "Ankara", "Izmir", "Istanbul",
        "Ankara", "Izmir", "Istanbul", "Ankara",
        "Izmir", "Istanbul"
    ],
    "experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "salary": [
        35000, 37000, 40000, 43000, 46000,
        50000, 54000, 58000, 62000, 67000
    ]
})

# 1. city ve experience sütunlarını X değişkenine ata.

X = employees[["city", "experience"]]

# 2. salary sütununu y değişkenine ata.

y = employees["salary"]

# 3. Veriyi train ve test olarak ayır.
# test_size=0.20
# random_state=42

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=42)


# 4. OneHotEncoder oluştur.
# sparse_output=False
# handle_unknown="ignore"

encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")



# 5. Encoder'ı sadece X_train içindeki city sütununa
# fit_transform() ile uygula.
# Sonucu train_city_encoded değişkenine kaydet.

train_city_encoded = encoder.fit_transform(X_train[["city"]])


# 6. Aynı encoder ile X_test içindeki city sütununa
# sadece transform() uygula.
# Sonucu test_city_encoded değişkenine kaydet.

test_city_encoded = encoder.transform(X_test[["city"]])


# 7. train_city_encoded değerini DataFrame'e çevir.
# columns:
# encoder.get_feature_names_out(["city"])
#
# index:
# X_train.index
#
# Sonucu train_city_df değişkenine kaydet.

train_city_df = pd.DataFrame(
    train_city_encoded,
    columns=encoder.get_feature_names_out(["city"]),
    index=X_train.index
)



# 8. test_city_encoded değerini de DataFrame'e çevir.
# Aynı column isimlerini kullan.
# index=X_test.index kullan.
# Sonucu test_city_df değişkenine kaydet.

test_city_df = pd.DataFrame(
    test_city_encoded,
    columns=encoder.get_feature_names_out(['city']),
    index=X_test.index
)


# 9. X_train içindeki experience sütununu
# train_city_df ile pd.concat(..., axis=1)
# kullanarak birleştir.
# Sonucu X_train_ready değişkenine kaydet.

X_train_ready = pd.concat([train_city_df, X_train["experience"]], axis=1)


# 10. X_test için de aynı işlemi yap.
# Sonucu X_test_ready değişkenine kaydet.

X_test_ready = pd.concat([test_city_df, X_test["experience"]], axis=1)

# 11. X_train_ready değerini yazdır.

print(X_train_ready)

# 12. X_test_ready değerini yazdır.

print(X_test_ready)

# 13. Encoder'ın öğrendiği kategorileri yazdır.
# encoder.categories_ kullan.

print(encoder.categories_)

# 14. Oluşan encoded sütun isimlerini yazdır.
# encoder.get_feature_names_out(["city"]) kullan.

print(encoder.get_feature_names_out(["city"]))