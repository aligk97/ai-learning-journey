# Day 10 - Statistics Basics

## Günün Hedefi

Veri analizi ve makine öğrenmesinde sık kullanılan temel istatistik kavramlarını öğrenmek; veri setindeki merkezi eğilimi, yayılımı, aykırı değerleri ve değişkenler arasındaki ilişkiyi yorumlayabilmek.

## İşlenen Konular

- Ortalama (`mean`) ve medyan (`median`)
- Mod (`mode`) ve aralık (`range`)
- Varyans (`variance`) ve standart sapma (`standard deviation`)
- Çeyrek değerler (`Q1`, `Q2`, `Q3`)
- IQR yöntemi
- Aykırı değer (`outlier`) tespiti
- Aykırı değerleri çıkardıktan sonra ortalamayı yeniden yorumlama
- Korelasyonun yönü ve gücü
- Korelasyon ile neden-sonuç ilişkisinin farkı

## Temel Komutlar / Fonksiyonlar

- `array.mean()`
- `np.median(array)`
- `array.var()`
- `array.std()`
- `series.mode()`
- `array.max() - array.min()`
- `np.percentile(array, 25)`
- `np.percentile(array, 50)`
- `np.percentile(array, 75)`
- `np.corrcoef(x, y)`

## Önemli Kavramlar

- **Mean:** Veri setindeki değerlerin toplamının değer sayısına bölünmesiyle bulunur.
- **Median:** Sıralanmış veri setindeki ortadaki değerdir. Aykırı değerlerden mean'e göre daha az etkilenir.
- **Mode:** Veri setinde en sık tekrar eden değerdir.
- **Range:** En büyük değer ile en küçük değer arasındaki farktır.
- **Variance:** Değerlerin ortalamadan ne kadar uzaklaştığını gösterir.
- **Standard deviation:** Yayılımı verinin kendi birimiyle yorumlamayı sağlar.
- **Quartile:** Veriyi dört parçaya bölen değerlerdir.
- **IQR:** `Q3 - Q1` formülüyle hesaplanır ve veri setinin orta kısmındaki yayılımı gösterir.
- **Outlier:** Normal veri aralığının dışında kalan aykırı değerdir.
- **Correlation:** İki değişken arasındaki lineer ilişkinin yönünü ve gücünü gösterir.

## IQR ile Outlier Tespiti

Q1 ve Q3 hesaplandıktan sonra IQR bulunur.

```python
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)

iqr = q3 - q1
```

Alt ve üst sınır şu şekilde hesaplanır:

```python
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
```

Bir değer alt sınırdan küçük veya üst sınırdan büyükse outlier kabul edilir.

```python
outliers = scores[
    (scores < lower_bound) | (scores > upper_bound)
]
```

Normal değerleri seçerken değer hem alt sınırın üstünde hem de üst sınırın altında olmalıdır.

```python
clean_scores = scores[
    (scores >= lower_bound) & (scores <= upper_bound)
]
```

## Yapılan Hatalar ve Düzeltmeler

### 1. Outlier koşulunda `&` ve `|` kullanımını karıştırmak

Outlier bulurken iki koşuldan birinin gerçekleşmesi yeterlidir. Bu yüzden `|` kullanılır.

```python
outliers = scores[(scores < lower_bound) | (scores > upper_bound)]
```

### 2. Normal değerleri seçerken `|` kullanmak

Normal değerler hem alt sınırın üstünde hem de üst sınırın altında olmalıdır. Bu yüzden `&` kullanılır.

```python
clean_scores = scores[
    (scores >= lower_bound) & (scores <= upper_bound)
]
```

### 3. Korelasyonu neden-sonuç gibi yorumlamak

Korelasyon iki değişken arasındaki ilişkinin yönünü ve gücünü gösterir. Ancak tek başına neden-sonuç ilişkisi kanıtlamaz.

## Final Check Özeti

Final check'te `scores` verisi üzerinde mean, median, variance ve standard deviation hesaplandı.

Sonrasında Q1, Q3 ve IQR kullanılarak alt ve üst sınırlar bulundu. `150` değeri outlier olarak tespit edildi.

Outlier çıkarıldıktan sonra mean değeri yeniden hesaplandı. Eski mean daha yüksekti çünkü `150` değeri ortalamayı yukarı çekiyordu.

`study_hours` ve `scores` arasındaki korelasyon değeri yaklaşık `0.87` çıktı. Bu sonuç güçlü pozitif bir ilişki olduğunu gösterir, fakat "daha fazla çalışmak kesin olarak daha yüksek skora sebep olur" sonucunu tek başına kanıtlamaz.

## Gün Sonu Kazanımları

Bu günün sonunda temel istatistik değerleri hesaplama, veri setindeki yayılımı yorumlama, IQR yöntemiyle outlier bulma, outlier çıkarıldıktan sonra mean değerini karşılaştırma ve korelasyon sonucunu doğru yorumlama pratiği yapıldı.
