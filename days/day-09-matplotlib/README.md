# Day 09 - Matplotlib

## Günün Hedefi

Matplotlib ile temel grafik türlerini oluşturmayı, grafik başlıklarını ve eksen isimlerini düzenlemeyi, birden fazla grafiği aynı figür içinde göstermeyi ve Pandas verisini görselleştirmeyi öğrenmek.

## İşlenen Konular

- `plot()` ile çizgi grafiği oluşturma
- `scatter()` ile iki değişken arasındaki ilişkiyi gösterme
- `bar()` ile kategorileri karşılaştırma
- `hist()` ve `bins` ile veri dağılımını inceleme
- `title()`, `xlabel()` ve `ylabel()` ile grafiği okunabilir hale getirme
- `figure(figsize=...)` ile grafik boyutunu ayarlama
- `label`, `legend()` ve `grid()` kullanımı
- `subplots()` ile yan yana grafikler oluşturma
- Pandas DataFrame sütunlarını Matplotlib grafiklerinde kullanma

## Temel Komutlar / Fonksiyonlar

- `plt.plot(x, y)`
- `plt.scatter(x, y)`
- `plt.bar(categories, values)`
- `plt.hist(values, bins=5)`
- `plt.figure(figsize=(width, height))`
- `plt.title("Title")`
- `plt.xlabel("X label")`
- `plt.ylabel("Y label")`
- `plt.legend()`
- `plt.grid()`
- `fig, axes = plt.subplots(1, 2, figsize=(12, 5))`
- `axes[0].set_title("Title")`
- `plt.tight_layout()`
- `plt.show()`

## Önemli Kavramlar

- **Çizgi grafiği:** Zaman veya sıralı değerler boyunca değişimi göstermek için kullanılır.
- **Scatter plot:** İki sayısal değişken arasındaki ilişkiyi görmeyi sağlar.
- **Bar chart:** Kategorileri sayısal değerlerle karşılaştırmak için kullanılır.
- **Histogram:** Tek bir sayısal veri setinin hangi aralıklarda yoğunlaştığını gösterir.
- **`bins`:** Histogramda verinin kaç aralığa bölüneceğini belirler.
- **`figsize`:** Grafiğin fiziksel boyutunu belirler. İlk değer genişlik, ikinci değer yüksekliktir.
- **`subplots()`:** Aynı figür içinde birden fazla grafik alanı oluşturur.
- **`axes[]`:** Subplot içindeki her bir grafiği ayrı ayrı yönetmek için kullanılır.
- **`tight_layout()`:** Birden fazla grafik olduğunda başlıkların ve eksen yazılarının birbirine girmesini önler.

## Yapılan Hatalar ve Düzeltmeler

### 1. İki subplot için tek `plt.grid()` kullanmak

`plt.grid()` sadece aktif olan grafiğe uygulanır. İki ayrı subplot varsa her grafik için ayrı ayrı grid eklemek daha doğrudur.

```python
axes[0].grid()
axes[1].grid()
```

### 2. `figsize` mantığını karıştırmak

`figsize`, grafikteki verinin değerlerini değiştirmez. Sadece grafiğin çizileceği alanın genişliğini ve yüksekliğini belirler.

```python
plt.figure(figsize=(9, 5))
```

## Final Task Özeti

Final task'ta `students` DataFrame'i kullanılarak yan yana iki grafik oluşturuldu.

Yapılan işlemler:

- `study_hours` ve `score` arasında scatter plot çizildi.
- `score` sütunu için `bins=5` ile histogram oluşturuldu.
- Her iki grafiğe başlık, X ekseni ve Y ekseni isimleri eklendi.
- Her iki subplot için ayrı ayrı `grid()` kullanıldı.
- Grafiklerin düzenli görünmesi için `tight_layout()` kullanıldı.

## Gün Sonu Kazanımları

Bu günün sonunda Matplotlib ile temel grafik oluşturma akışı öğrenildi. Veriyi yalnızca tablo olarak görmek yerine, ilişki, karşılaştırma ve dağılım gibi yapıları grafiklerle yorumlama pratiği yapıldı. Pandas DataFrame sütunlarının doğrudan Matplotlib grafiklerinde kullanılabileceği görüldü.
