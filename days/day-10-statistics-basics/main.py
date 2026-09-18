# minitask 1

import numpy as np

house_prices = np.array([
    2400000,
    2600000,
    2700000,
    2900000,
    3100000,
    12500000
])

# 1. Ev fiyatlarının mean değerini bul.

print(house_prices.mean())  


# 2. Median değerini bul.
print(np.median(house_prices))

# 3. Mean ile median arasında ne kadar fark olduğunu hesapla.

print("mean - median: ", house_prices.mean() - np.median(house_prices))

# 4. Hangisinin bu veri setindeki tipik ev fiyatını
# daha iyi temsil ettiğini yorum olarak yaz.

print("tek bir değerden dolayı ortalama çok yükselmiş o yüzden median a bakmak daha mantıklı")



# minitask 2

import pandas as pd
import numpy as np

scores = np.array([
    55, 70, 70, 80, 85, 85, 85, 90, 95
])

# 1. scores dizisini Pandas Series'e çevir.

scores_series = pd.Series(scores)

print(scores_series)

# 2. Mode değerini bul.

print("mode:", scores_series.mode())

# 3. En yüksek ve en düşük skor arasındaki range'i hesapla.

scores_range = scores_series.max() - scores_series.min()
print('range:', scores_range)

# 4. Mean ve median değerlerini de hesapla.

score_series_mean = scores_series.mean()
scores_series_median = scores_series.median()

# 5. Mean ve median birbirine yakın mı?
# Bunun veri dağılımı hakkında bize ne söyleyebileceğini
# yorum olarak yaz.

print("mean - median farki: ", score_series_mean - scores_series_median)
print("mean ile median birbirine yakın. Demek ki veriler birbirine yakın çünkü ortalama değer ile tam ortada ki sayılar birbirine çok yakın. Outlier söz konusu değil.")




# minitask 3

import numpy as np

class_a = np.array([78, 79, 80, 81, 82])

class_b = np.array([40, 60, 80, 100, 120])

# 1. class_a'nın mean değerini bul.

class_a_mean = class_a.mean()

# 2. class_b'nin mean değerini bul.

class_b_mean = class_b.mean()

# 3. İki sınıfın variance değerlerini hesapla.

class_a_variance = class_a.var()
class_b_variance = class_b.var()

# 4. İki sınıfın standard deviation değerlerini hesapla.

class_a_std = class_a.std()
class_b_std = class_b.std()

# 5. İki sınıfın range değerlerini hesapla.

class_a_range = class_a.max() - class_a.min()
class_b_range = class_b.max() - class_b.min()

# 6. Mean değerleri aynı olmasına rağmen
# öğrencilerin skor dağılımının neden farklı olduğunu
# variance ve standard deviation kullanarak yorumla.

merged_data = pd.DataFrame({
    "mean": [class_a_mean, class_b_mean],
    "variance": [class_a_variance, class_b_variance],
    "std": [class_a_std, class_b_std],
    "range": [class_a_range, class_b_range]
},index=["CLASS A", "CLASS B"])

print(merged_data)

print('tabloda da görüldüğü üzere. class b de sayılar arasındaki fark fazla olduğundan dolayı var ve std değerleri birbirinden farklı. Mean aynı olabilir fakat sayıların birbirine uzaklığı farklı olabilir.')



# minitask 4

import numpy as np

scores = np.array([
    45, 50, 55, 60, 65,
    70, 75, 80, 85, 90, 95
])

# 1. Q1 değerini hesapla.

print(np.percentile(scores,25))

# 2. Q2 değerini hesapla.

print(np.percentile(scores,50))

# 3. Q3 değerini hesapla.

print(np.percentile(scores,75))

# 4. Median değerini hesapla.

print(np.percentile(scores,50))

# 5. Q2 ile median'ın aynı olup olmadığını kontrol et.

print(np.percentile(scores,50) == np.median(scores))


# minitask 5

import numpy as np

scores = np.array([
    45, 50, 55, 60, 65,
    70, 75, 80, 85, 90, 95, 200
])

# 1. Q1 ve Q3 değerlerini hesapla.

q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)

# 2. IQR değerini hesapla.

iqr = q3 - q1

# 3. lower_bound ve upper_bound değerlerini hesapla.

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

print(lower_bound, upper_bound)


# 4. Boolean filtering kullanarak
# outlier olan değerleri bul.
print(scores[(scores < lower_bound) | (scores > upper_bound)])



# minitask 6

import numpy as np

study_hours = np.array([1, 2, 3, 4, 5, 6])
scores = np.array([50, 55, 65, 72, 85, 92])

# 1. np.corrcoef() kullanarak
# study_hours ve scores arasındaki
# correlation matrix'i yazdır.

np.corrcoef(study_hours, scores)

# 2. Matrix içerisinden sadece
# iki değişken arasındaki correlation değerini al.

correlation = np.corrcoef(study_hours, scores)[0, 1]

print(correlation)


# 3. Correlation değerine bakarak
# ilişkinin pozitif mi negatif mi olduğunu yorumla.

print('0.99 gibi pozitif bir sayı çıkıyor. ilişki oldukça kuvvetli ve pozitif')


# minitask 7

import numpy as np

screen_time = np.array([1, 2, 3, 4, 5, 6])
sleep_hours = np.array([8.5, 8.0, 7.5, 7.0, 6.2, 5.8])

# 1. screen_time ile sleep_hours arasındaki
# correlation değerini hesapla.

correlation = np.corrcoef(screen_time, sleep_hours)
print(correlation)


# 2. Correlation pozitif mi negatif mi yazdır.

print(correlation[0,1], "guclu negatif")

# 3. İlişkinin güçlü mü zayıf mı olduğunu yorumla.

print(correlation[0,1], "guclu negatif")


# 4. "Ekran süresi arttığı için uyku süresi azalıyor."
# demenin neden doğrudan doğru olmadığını
# kısa bir yorum olarak yaz.

print('correlation bize sonuc vermez. Sadece iki verinin birbiriyle ne kadar alakali oldugunu soyler.')


# minitask 8 - Day 10 Final Check

import numpy as np

scores = np.array([
    52, 58, 61, 65, 68,
    70, 72, 75, 78, 82,
    85, 88, 92, 150
])

study_hours = np.array([
    1, 2, 2, 3, 3,
    4, 4, 5, 5, 6,
    6, 7, 8, 9
])

# 1. scores için:
# mean, median, variance ve standard deviation hesapla.


print(scores.mean(),np.median(scores), scores.var(), scores.std())

mean = scores.mean()

# 2. Q1 ve Q3 değerlerini hesapla.
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)

# 3. IQR hesapla.

iqr = q3-q1

# 4. IQR yöntemini kullanarak
# lower_bound ve upper_bound değerlerini hesapla.

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)


# 5. Outlier olan skorları bul.

outliers = (scores[(scores < lower_bound) | (scores > upper_bound)])

# 6. Outlier'ları çıkardıktan sonra
# kalan skorların mean değerini hesapla.

clean_scores = scores[(scores >= lower_bound) & (scores <= upper_bound)]

# İlk mean ile karşılaştır.
# Outlier'ın mean üzerindeki etkisini yorumla.

print("old mean:", mean)
print("new mean:", clean_scores.mean())
# 7. study_hours ile scores arasındaki
# correlation değerini hesapla.

correlation = np.corrcoef(study_hours, scores)[0, 1]

print(correlation)

# 8. Correlation'ın:
# - yönünü
# - gücünü
# yorumla.

print('0.87 pozitif korelasyon var.')


# 9. Bu correlation sonucuna bakarak
# "fazla çalışmak yüksek skora sebep olur"
# diyebilir miyiz?
# Kısaca nedenini yaz.

print("neden sonuc ilişkisi kuramayız. Başka parametrelerde olabilir. Sadece 2 veri arasındaki ilişkinin yakınlığını yorumlayabiliriz.")