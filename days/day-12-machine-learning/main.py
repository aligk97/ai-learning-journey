# minitask 1

import pandas as pd

houses = pd.DataFrame({
    "size": [80, 120, 150, 200, 250],
    "rooms": [2, 3, 3, 4, 5],
    "age": [20, 15, 10, 8, 5],
    "price": [250000, 350000, 420000, 550000, 700000]
})

# Modelde kullanılacak feature sütunları
X = houses[["size", "rooms", "age"]]

# Tahmin edilmek istenen target
y = houses["price"]

print(X)
print(y)


# minitask 2

customers = pd.DataFrame({
    "age": [22, 35, 46, 28, 51],
    "income": [25000, 50000, 75000, 42000, 90000],
    "visits": [2, 6, 8, 4, 10],
    "purchased": [0, 1, 1, 0, 1]
})

X = customers[["age", "income", "visits"]]
y = customers["purchased"]

print(X)
print(y)

# Supervised - Classification
# Çünkü müşterinin satın alıp almadığını tahmin ediyoruz.
# İki farklı sınıf var: 0 ve 1.


# minitask 3

# 1.
# Geçmiş ev verilerinde size, rooms, age ve price bilgileri varsa
# yeni bir evin price değerini tahmin etmek:
# Supervised - Regression

# 2.
# Bir e-postanın spam veya not spam olduğunu tahmin etmek:
# Supervised - Classification

# 3.
# Herhangi bir grup etiketi olmadan
# benzer müşterileri gruplara ayırmak:
# Unsupervised

# 4.
# Bir arabanın yakıt tüketimini tahmin etmek:
# Supervised - Regression

# 5.
# Öğrencinin sınavı geçip geçmeyeceğini tahmin etmek:
# Supervised - Classification


# minitask 4

# 1.
# Geçmiş araba ilanlarında gerçek satış fiyatları biliniyor.
# Yeni bir arabanın satış fiyatını tahmin etmek:
# Supervised - Regression

# 2.
# Müşterilerin hangi gruba ait olduğu bilinmiyor.
# Benzer müşterileri gruplamak:
# Unsupervised

# 3.
# Geçmiş müşterilerin krediyi ödeyip ödemediği biliniyor.
# Yeni müşterinin krediyi ödeyip ödemeyeceğini tahmin etmek:
# Supervised - Classification

# 4.
# Geçmiş evlerin kaç günde satıldığı bilgisi varsa:
# Supervised - Regression
#
# Eğer geçmiş satış süresi bilgisi yoksa
# bu şekilde regression modeli doğrudan eğitilemez.

# 5.
# Önceden belirlenmiş kategori etiketi olmadan
# haber yazılarını benzerliklerine göre gruplamak:
# Unsupervised


# minitask 5

# 1.
# Geçmiş çalışanların gerçek salary değerleri biliniyor.
# Yeni çalışanın maaşını tahmin etmek:
# Supervised - Regression

# 2.
# Hayvan türü etiketi yok.
# Benzer hayvanları gruplamak:
# Unsupervised

# 3.
# Geçmiş işlemlerin fraud olup olmadığı biliniyor.
# Yeni işlemin fraud olup olmadığını tahmin etmek:
# Supervised - Classification

# 4.
# Hastalık etiketi olmadan
# benzer hasta verilerini gruplamak:
# Unsupervised

# 5.
# Geçmiş evlerin price değerleri olmadığı için target (y) yoktur.
# Fiyatlara dair referans alabileceğimiz bir sonuç bulunmadığı için
# yeni bir evin fiyatını tahmin edecek
# supervised regression modeli doğrudan eğitilemez.


# minitask 6

cars = pd.DataFrame({
    "horsepower": [100, 130, 160, 200, 250],
    "age": [12, 9, 6, 4, 2],
    "mileage": [180000, 140000, 100000, 70000, 30000],
    "price": [300000, 420000, 550000, 700000, 900000]
})

X = cars[["horsepower", "age", "mileage"]]
y = cars["price"]

new_car = pd.DataFrame({
    "horsepower": [175],
    "age": [5],
    "mileage": [85000]
})

# new_car içinde price yok çünkü
# zaten tahmin etmeye çalıştığımız değer price.

print(X)
print(y)
print(new_car)


# minitask 7

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

# Model X_test üzerinde tahmin yaptıktan sonra
# oluşan y_pred değerleri y_test ile karşılaştırılır.


# minitask 8

import pandas as pd
from sklearn.model_selection import train_test_split

houses = pd.DataFrame({
    "size": [80, 120, 150, 200, 250, 170, 140, 220, 190, 110],
    "rooms": [2, 3, 3, 4, 5, 3, 3, 4, 4, 2],
    "age": [20, 15, 10, 8, 5, 12, 9, 6, 7, 18],
    "price": [250000, 350000, 420000, 550000, 700000,
              460000, 400000, 620000, 520000, 320000]
})

# 1. size, rooms ve age sütunlarını X'e ata.

X = houses[["size", "rooms", "age"]]

# 2. price sütununu y'ye ata.

y = houses["price"]

# 3. train_test_split kullanarak veriyi ayır
#
# test_size=0.2
# random_state=42
#
# Sonuçları şu değişkenlere ata:
# X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)

# 4. X_train'i yazdır.

print(X_train)

# 5. X_test'i yazdır.
print("ssaaaaaaaaaaa")
print(X_test)

# 6. X_train ve X_test'in shape değerlerini yazdır.

print("ssaaaaaaaaaaa")
print(X_test.shape)
print("ssaaaaaaaaaaa")
print(y_test.shape)



# Day 12 - Final Check

import pandas as pd
from sklearn.model_selection import train_test_split

students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [55, 60, 65, 70, 75, 80, 85, 90, 92, 95],
    "sleep_hours": [5, 6, 6, 7, 6, 7, 8, 7, 8, 8],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

# 1.
# Feature sütunlarını X değişkenine ata.

X = students[['study_hours', "attendence", 'sleep_hours']]

# 2.
# Target sütununu y değişkenine ata.

y = students["passed"]


# 3.
# Bu problemin:
# Supervised / Unsupervised
# Regression / Classification
# olduğunu yorum satırıyla yaz ve nedenini kısaca açıkla.

print('supervised classification')

# 4.
# Veriyi train ve test olarak ayır.
#
# test_size=0.2
# random_state=42
#
# X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5.
# X_train ve X_test'i yazdır.

print(X_train)
print('------------')
print(X_test)

# 6.
# X_train, X_test, y_train ve y_test
# shape değerlerini yazdır.

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# 7.
# Aşağıdaki yeni öğrenciyi new_student
# isimli DataFrame olarak oluştur:
#
# study_hours = 6
# attendance = 82
# sleep_hours = 7


new_student = pd.DataFrame({
    "study_hours": 6,
    "attendance": 82,
    "sleep_hours": 7
})


# 8.
# new_student içinde neden "passed"
# sütunu olmadığını yorum satırıyla açıkla.

#onu bulmasini istiyoruz zaten


# 9.
# Aşağıdaki kavramları kısa yorumlarla açıkla:
#
# X_train
# y_train
# X_test
# y_test

#gerek yok biliyorum


# 10.
# Model ileride X_test üzerinde tahmin yaptığında,
# tahmin edilen değerlerin değişken adının y_pred
# olduğunu düşün.
#
# y_pred hangi değişkenle karşılaştırılır?
# Yorum satırıyla cevap ver.

#y_test ile karsilastirilir


# 11.
# Model neden X_test ve y_test verilerini
# training sırasında görmemelidir?
# Kısa yorum satırıyla açıkla.

#ezberler