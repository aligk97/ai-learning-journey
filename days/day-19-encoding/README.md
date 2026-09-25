# Day 19 - Encoding

## Konular

- Encoding mantığı
- Kategorik verileri sayısal hale getirme
- `map()` ile basit encoding
- `pd.get_dummies()` ile one-hot encoding
- `drop_first` kullanımı
- `OneHotEncoder`
- `fit`, `transform` ve `fit_transform`
- `handle_unknown="ignore"`
- Train/test preprocessing mantığı
- Encoded veriyi tekrar DataFrame'e çevirme
- Encoded feature'ları sayısal feature'larla birleştirme

## Encoding

Encoding, kategorik verileri makine öğrenmesi modellerinin kullanabileceği sayısal formata dönüştürme işlemidir.

Örneğin:

```text
Yes -> 1
No  -> 0
```

Bu tarz basit dönüşümler `map()` ile yapılabilir.

## One-Hot Encoding

One-hot encoding, her kategoriyi ayrı bir sütuna çevirir.

Örneğin `city` sütununda şu kategoriler varsa:

```text
Ankara
Istanbul
Izmir
```

Oluşan sütunlar şöyle olur:

```text
city_Ankara
city_Istanbul
city_Izmir
```

İlgili şehir varsa `1`, yoksa `0` yazılır.

## OneHotEncoder

Scikit-learn tarafında kategorik verileri encode etmek için `OneHotEncoder` kullanılır.

```python
encoder = OneHotEncoder(
    sparse_output=False,
    handle_unknown="ignore"
)
```

`handle_unknown="ignore"`, test verisinde train verisinde görülmeyen yeni bir kategori çıkarsa hata vermeden işlemin devam etmesini sağlar.

## fit, transform ve fit_transform

- `fit()`: Train verisinden kategorileri öğrenir.
- `transform()`: Öğrenilen kategorilere göre veriyi dönüştürür.
- `fit_transform()`: Önce öğrenir, sonra aynı veriyi dönüştürür.

Train/test ayrımında temel kural:

```text
Train -> fit_transform
Test  -> transform
```

Test verisinde tekrar `fit_transform()` kullanmak yanlıştır. Çünkü encoder test verisinden yeniden kategori öğrenmiş olur.

## DataFrame'e Çevirme

`OneHotEncoder` çıktısı doğrudan DataFrame değildir. Bu yüzden tekrar DataFrame'e çevrilir.

```python
train_city_df = pd.DataFrame(
    train_city_encoded,
    columns=encoder.get_feature_names_out(["city"]),
    index=X_train.index
)
```

Burada `index=X_train.index` kullanmak önemlidir. Böylece encoded satırlar, orijinal train verisindeki doğru satırlarla eşleşir.

## Final Check Özeti

Final check'te `city`, `experience` ve `salary` sütunlarından oluşan bir çalışan DataFrame'i kullanıldı.

Yapılan işlemler:

- `city` ve `experience` feature olarak `X` değişkenine atandı.
- `salary` target olarak `y` değişkenine atandı.
- Veri train/test olarak ayrıldı.
- Encoder sadece train verisindeki `city` sütununda `fit_transform()` ile eğitildi.
- Test verisindeki `city` sütununa aynı encoder ile sadece `transform()` uygulandı.
- Encoded çıktılar DataFrame'e çevrildi.
- Encoded şehir sütunları `experience` sütunu ile tekrar birleştirildi.
- Encoder'ın öğrendiği kategoriler ve oluşan sütun isimleri yazdırıldı.

## Gün Sonu Özeti

Day 19 sonunda kategorik verilerin modele verilmeden önce neden sayısal hale getirilmesi gerektiği öğrenildi.

En önemli kural:

```text
Train verisinde öğren.
Test verisinde sadece uygula.
```
