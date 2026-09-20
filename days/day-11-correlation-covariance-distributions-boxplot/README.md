# Day 11 - Correlation, Covariance, Distributions and Boxplot

## Günün Hedefi

Değişkenler arasındaki ilişkileri correlation ve covariance ile okumayı, dağılımları histogramla incelemeyi, skewness yorumlamayı ve boxplot üzerinden potansiyel outlier değerleri görmeyi öğrenmek.

## İşlenen Konular

- Correlation ile iki değişken arasındaki ilişkinin yönünü ve gücünü yorumlama
- Correlation matrix oluşturma
- Covariance ile iki değişkenin birlikte hareket edip etmediğini okuma
- Correlation ve covariance farkını anlama
- Histogram ile dağılımı görselleştirme
- Mean, median ve skewness ilişkisini yorumlama
- Boxplot ile potansiyel outlier değerleri görme
- IQR yöntemiyle upper bound hesaplama
- Line plot ve scatter plot farkını görme

## Temel Komutlar / Fonksiyonlar

- `df["column_1"].corr(df["column_2"])`
- `df.corr(numeric_only=True)`
- `df["column_1"].cov(df["column_2"])`
- `df.cov(numeric_only=True)`
- `series.mean()`
- `series.median()`
- `series.skew()`
- `np.percentile(values, 25)`
- `np.percentile(values, 75)`
- `plt.hist(values, bins=5)`
- `plt.boxplot(values)`
- `plt.plot(x, y, marker="o")`
- `plt.scatter(x, y)`

## Önemli Kavramlar

- **Correlation:** İki değişken arasındaki doğrusal ilişkinin yönünü ve gücünü gösterir. Değer aralığı `-1` ile `1` arasındadır.
- **Positive correlation:** Bir değişken artarken diğer değişken de genel olarak artıyorsa pozitif ilişki vardır.
- **Negative correlation:** Bir değişken artarken diğer değişken genel olarak azalıyorsa negatif ilişki vardır.
- **Correlation does not imply causation:** İki değişken ilişkili görünse bile biri diğerinin kesin sebebidir denemez.
- **Covariance:** İki değişkenin birlikte hareket edip etmediğini gösterir. İşareti yorumlamak kolaydır, fakat büyüklüğü ölçeğe bağlıdır.
- **Correlation vs covariance:** Correlation ölçekten bağımsızdır; covariance ise değişkenlerin biriminden ve ölçeğinden etkilenir.
- **Distribution:** Verinin hangi değerler etrafında toplandığını ve nasıl yayıldığını gösterir.
- **Skewness:** Dağılımın sağa veya sola çarpık olup olmadığını gösterir.
- **Right-skewed distribution:** Sağ tarafta uzun kuyruk vardır; genellikle `mean > median` olur.
- **Boxplot:** Median, Q1, Q3, IQR ve potansiyel outlier değerleri tek grafikte gösterir.
- **IQR upper bound:** `Q3 + 1.5 * IQR` formülüyle hesaplanır. Bu sınırın üstündeki değerler potansiyel outlier kabul edilir.
- **Scatter plot:** İki değişken arasındaki ilişkiyi göstermek için line plot'tan daha uygundur.

## Yapılan Hatalar ve Düzeltmeler

### 1. `sleep_hours` correlation hesabında aynı sütunu tekrar kullanmak

İkinci correlation sorusunda `study_hours` tekrar yazılmıştı. `sleep_hours` ile `score` ilişkisini hesaplamak için doğru kullanım:

```python
students["sleep_hours"].corr(students["score"])
```

### 2. Outlier upper bound hesabında çarpma işaretini kaçış karakteriyle yazmak

Python kodunda çarpma işlemi için `*` doğrudan kullanılmalıdır.

```python
upper_bound = q3 + 1.5 * iqr
```

### 3. Skewness yorumunu hafif sanmak

Final check verisinde `score` skewness değeri yaklaşık `1.886` çıktığı için dağılım hafif değil, belirgin şekilde right-skewed olarak yorumlanmalıdır.

## Final Task Özeti

Final task'ta `study_hours`, `sleep_hours` ve `score` sütunlarından oluşan öğrenci DataFrame'i kullanıldı.

Yapılan işlemler:

- Bütün sayısal sütunların correlation matrix'i oluşturuldu.
- `study_hours` ile `score` arasındaki correlation değeri hesaplandı.
- `score` sütununun mean, median ve skewness değerleri hesaplandı.
- Q1, Q3, IQR ve upper bound değerleri bulundu.
- `score` dağılımı histogramla görselleştirildi.
- `score` için boxplot oluşturuldu.
- `study_hours` ve `score` ilişkisi line plot ve scatter plot ile çizildi.
- `150` değerinin potansiyel outlier olduğu yorumlandı.

Beklenen önemli sonuçlar:

```text
study_hours <-> score correlation = 0.867
mean   = 76.3
median = 71.0
skew   = 1.886
upper_bound = 118.0
```

## Gün Sonu Kazanımları

Bu günün sonunda değişkenler arasındaki ilişkiler correlation ve covariance ile yorumlandı. Dağılımların sadece grafikle değil, mean, median ve skewness değerleriyle de okunabileceği görüldü. Boxplot ve IQR yöntemiyle potansiyel outlier değerleri belirleme pratiği yapıldı.
