# Day 05 - Pandas Basics

## Günün Hedefi

Pandas ile veri okumayı, veri setinin genel yapısını incelemeyi, satır/sütun seçmeyi, koşullu filtreleme yapmayı, sıralamayı ve eksik verilerle temel düzeyde çalışmayı öğrenmek.

## İşlenen Konular

- `Series` ve `DataFrame` yapıları
- `shape`, `columns`, `dtypes` ile veri setini hızlı tanıma
- `head()`, `tail()`, `info()`, `describe()` ile ilk inceleme
- `pd.read_csv()` ile CSV dosyası okuma
- `pathlib` ile `current_folder` kullanarak dosya yolunu güvenli kurma
- `loc` ve `iloc` ile satır/sütun seçme
- Slicing ile belirli satır ve sütun aralıklarını alma
- Boolean filtering ile koşula göre veri seçme
- `&`, `|`, `~` ile birden fazla koşul kullanma
- `sort_values()` ile veriyi sıralama
- Yeni sütun oluşturma
- `drop()` ile sütun/satır silme
- `rename()` ile sütun adı değiştirme
- `isna()`, `fillna()`, `dropna()` ile eksik verileri inceleme ve temizleme
- `unique()` ve `value_counts()` ile kategorik verileri özetleme

## Temel Komutlar / Fonksiyonlar

- `pd.Series([...])`
- `pd.DataFrame({...})`
- `pd.read_csv(current_folder / "students.csv")`
- `pathlib.Path(__file__).resolve().parent`
- `students.shape`
- `students.columns`
- `students.dtypes`
- `students.head()`
- `students.tail()`
- `students.info()`
- `students.describe()`
- `students.loc[row_filter, column_list]`
- `students.iloc[row_index, column_index]`
- `students[students["Score"] >= 80]`
- `students[(condition1) & (condition2)]`
- `students[(condition1) | (condition2)]`
- `students[~condition]`
- `students.sort_values("Score", ascending=False)`
- `students["Passed"] = students["Score"] >= 80`
- `students.drop(columns=["Age"])`
- `students.rename(columns={"Score": "Exam_Score"})`
- `students.isna().sum()`
- `students["Age"].fillna(students["Age"].mean())`
- `students.dropna(subset=["Score"])`
- `students["Department"].unique()`
- `students["Department"].value_counts()`

## Önemli Kavramlar

- **Series:** Tek sütunluk veri yapısı gibi düşünülebilir.
- **DataFrame:** Satır ve sütunlardan oluşan tablo yapısıdır.
- **Index hizalaması:** Pandas atama yaparken çoğu zaman pozisyona değil index değerlerine göre eşleştirme yapar.
- **`loc`:** Satır/sütun isimleri veya koşullar ile seçim yapar.
- **`iloc`:** Sayısal pozisyona göre seçim yapar.
- **Boolean filtering:** Sadece koşulu sağlayan satırları getirir.
- **Eksik veri:** `NaN` değerleri analiz sonucunu etkileyebilir; doldurmak veya satırı silmek gerekebilir.

## `std` Notları

`std`, yani standart sapma, verilerin ortalamanın etrafında ne kadar yayıldığını gösterir.

Kısa mantık:

```text
mean -> veri nerede merkezlenmiş?
std  -> veriler bu merkezin etrafında ne kadar dağılmış?
```

Nasıl hesaplanır?

1. Ortalama bulunur.
2. Her değerin ortalamadan farkı alınır.
3. Farkların karesi alınır.
4. Bu karelerin ortalaması alınır.
5. Sonucun karekökü alınır.

Pandas'ta `.std()` ve `describe()` içindeki `std` varsayılan olarak sample standard deviation kullanır; yani bölme işleminde `n` yerine `n - 1` kullanılır.

Yorumlama:

- `std` tek başına büyük/küçük diye yorumlanmaz.
- Ortalama ile birlikte düşünülür.
- Pratik oran: `std / mean`
- `std / mean` yaklaşık `%5` ise yayılım düşük, `%20` civarıysa belirgin, `%50` civarıysa çok yüksek sayılabilir.
- `std = 10`, değerler kesin olarak `mean - 10` ile `mean + 10` arasındadır demek değildir; sadece yayılım hakkında fikir verir.

## Yapılan Hatalar ve Düzeltmeler

### 1. `students_missing` değişkenini yanlışlıkla Series'e çevirmek

Eksik değer doldururken bütün DataFrame değişkenini tek bir sütunun sonucuna eşitlemek, `students_missing` değişkenini DataFrame olmaktan çıkarıp Series'e çevirebilir.

Yanlış mantık:

```python
students_missing = students_missing["Age"].fillna(students_missing["Age"].mean())
```

Doğru kullanım:

```python
students_missing["Age"] = students_missing["Age"].fillna(students_missing["Age"].mean())
```

### 2. `Score` Series üzerinde `dropna()` yapmak satırı silmez

Şu kullanım sadece `Score` sütunundaki Series üzerinde `NaN` değerini çıkarır; DataFrame'deki öğrencinin tüm satırını silmez:

```python
students["Score"] = students["Score"].dropna()
```

Satırı tamamen silmek için:

```python
students = students.dropna(subset=["Score"])
```

Bu, `Score` değeri eksik olan öğrenciyi komple DataFrame'den çıkarır.

### 3. `sort_values()` yönü ve sadece `Score` sütununu sıralama

`ascending=True` küçükten büyüğe sıralar. Büyükten küçüğe sıralamak için `ascending=False` gerekir.

Ayrıca sadece `Score` sütununu sıralamak yerine, öğrencinin diğer bilgilerini de koruyarak tüm DataFrame'i sıralamak daha doğrudur.

```python
passed_students = passed_students.sort_values("Score", ascending=False)
```

## Final Task Özeti

Final task'ta `Name`, `Age`, `Department` ve `Score` sütunlarından oluşan bir öğrenci DataFrame'i kullanıldı.

Yapılan işlemler:

- Veri setinin `shape`, `info()` ve `describe()` çıktıları incelendi.
- `Age` sütunundaki eksik değerler yaş ortalamasıyla dolduruldu.
- `Score` değeri eksik olan öğrencinin satırının silinmesi gerektiği öğrenildi.
- `Score >= 80` koşuluna göre `Passed` sütunu oluşturuldu.
- Sadece geçen öğrencilerden `Name`, `Department`, `Score` sütunları seçildi.
- Sonuç `Score` değerine göre büyükten küçüğe sıralandı.
- Bölümlere göre öğrenci sayısı `value_counts()` ile özetlendi.

## Gün Sonu Kazanımları

Bu günün sonunda Pandas ile küçük bir veri setini okumak, incelemek, seçmek, filtrelemek, sıralamak ve temizlemek pratik edildi. Ayrıca `std` kavramının neyi gösterdiği, nasıl hesaplandığı ve ortalama ile birlikte nasıl yorumlanması gerektiği netleştirildi.

En önemli pratik kazanım: Pandas'ta bir sütun üzerinde işlem yapmak ile DataFrame'deki satırı değiştirmek/silmek aynı şey değildir. Özellikle `dropna()`, atama ve index hizalaması konusunda dikkatli olmak gerekir.
