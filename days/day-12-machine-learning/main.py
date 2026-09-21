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
