# Day 07 - Pandas Data Cleaning

## Günün Hedefi

Pandas ile eksik verileri bulmayı, doldurmayı veya silmeyi; duplicate satırları temizlemeyi; veriyi sıralamayı ve `groupby()` ile temel özetler çıkarmayı öğrenmek.

## İşlenen Konular

- Eksik değerleri `isna()` / `isnull()` ile kontrol etme
- Eksik değer sayılarını sütun bazında görme
- `dropna()` ile eksik değer içeren satırları silme
- `fillna()` ile eksik değerleri doldurma
- `duplicated()` ile tekrar eden satırları bulma
- `drop_duplicates()` ile duplicate satırları kaldırma
- `sort_values()` ile tek veya birden fazla sütuna göre sıralama
- `groupby()` ile gruplama yapma
- `agg()` ile birden fazla istatistiği tek seferde hesaplama

## Temel Komutlar / Fonksiyonlar

- `students.isnull()`
- `students.isnull().sum()`
- `students[students["age"].isnull()]`
- `students[students["score"].notnull()]`
- `students.dropna(subset=["score"])`
- `students["age"].fillna(students["age"].mean())`
- `students["city"].fillna("Unknown")`
- `students.duplicated()`
- `students[students.duplicated()]`
- `students.drop_duplicates()`
- `students.duplicated(subset=["name"])`
- `students.sort_values("score", ascending=False)`
- `students.sort_values(by=["city", "score"], ascending=[True, False])`
- `students.groupby("city")["score"].mean()`
- `students.groupby("city")["score"].agg(["mean", "min", "max"])`

## Önemli Kavramlar

- **Eksik veri:** DataFrame içinde boş veya bilinmeyen değerler çoğu zaman `NaN` olarak görünür.
- **`dropna()`:** Eksik değer içeren satırları siler. `subset` ile sadece belirli sütunlar kontrol edilebilir.
- **`fillna()`:** Eksik değerleri sabit bir değerle veya ortalama gibi hesaplanan bir değerle doldurur.
- **Duplicate satır:** Tüm değerleri aynı olan satır tekrar eden satırdır.
- **Subset ile duplicate kontrolü:** Sadece seçilen sütunlara bakarak tekrar kontrolü yapılabilir.
- **`sort_values()`:** DataFrame'i değerlerine göre sıralar. Atama yapılmazsa orijinal değişken kalıcı olarak değişmez.
- **`groupby()`:** Veriyi bir sütuna göre gruplar ve her grup için ayrı hesaplama yapılmasını sağlar.
- **Temizlenmiş veriyle analiz:** Eksik veya duplicate veriler temizlendikten sonra analiz `clean_students` gibi temizlenmiş DataFrame üzerinden yapılmalıdır.

## Yapılan Hatalar ve Düzeltmeler

### 1. `sort_values()` sonucunu değişkene atamamak

`sort_values()` ekrana doğru sonucu gösterebilir, fakat sonucu değişkene atamazsan DataFrame'in kendisi kalıcı olarak sıralanmaz.

```python
clean_students = clean_students.sort_values("score", ascending=False)
```

### 2. Temizlenmiş veri yerine eski DataFrame ile analiz yapmak

Eksik `score` satırı silindikten ve duplicate kayıtlar kaldırıldıktan sonra `groupby()` analizleri artık `students` yerine `clean_students` üzerinden yapılmalıdır.

```python
clean_students.groupby("city")["score"].mean()
```

Bu özellikle duplicate kayıtlar varsa sonucu değiştirir.

## Final Task Özeti

Final task'ta `name`, `age`, `score` ve `city` sütunlarından oluşan küçük bir öğrenci DataFrame'i kullanıldı.

Yapılan işlemler:

- Her sütundaki eksik değer sayısı kontrol edildi.
- Eksik `age` değerleri yaş ortalamasıyla dolduruldu.
- Eksik `city` değerleri `"Unknown"` ile dolduruldu.
- `score` değeri eksik olan satırlar silindi.
- Tamamen duplicate olan satırlar kaldırıldı.
- Temizlenmiş veri `score` değerine göre büyükten küçüğe sıralandı.
- Her şehir için ortalama `score` hesaplandı.
- Her şehir için `mean`, `min` ve `max` değerleri tek seferde hesaplandı.

## Gün Sonu Kazanımları

Bu günün sonunda Pandas ile temel veri temizleme akışı pratik edildi: eksik veriyi fark etme, uygun şekilde doldurma veya silme, tekrar eden kayıtları kaldırma, temiz veriyi sıralama ve gruplar üzerinden özet istatistik çıkarma.

En önemli pratik kazanım: Analiz yapmadan önce verinin hangi DataFrame üzerinde temizlendiğine dikkat etmek gerekir. Temizleme işlemlerinden sonra sonuçları eski veriyle değil, temizlenmiş veriyle hesaplamak gerekir.
