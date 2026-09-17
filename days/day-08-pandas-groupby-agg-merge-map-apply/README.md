# Day 08 - Pandas Advanced Data Manipulation

## Günün Hedefi

Pandas'ta birden fazla işlemi birlikte kullanarak daha gerçekçi veri analiz akışları kurmayı öğrenmek: `groupby()`, `agg()`, `merge()`, `map()` ve `apply()`.

## İşlenen Konular

- `groupby()` ile veriyi kategorilere göre gruplama
- `agg()` ile birden fazla özet istatistiği aynı anda hesaplama
- Named aggregation ile sonuç sütunlarına okunabilir isimler verme
- `merge()` ile iki DataFrame'i ortak sütun üzerinden birleştirme
- `map()` ile mevcut değerleri yeni kodlara veya etiketlere dönüştürme
- `apply(axis=1)` ile satır bazlı özel fonksiyon çalıştırma

## Temel Komutlar / Fonksiyonlar

- `df.groupby("column")["value"].mean()`
- `df.groupby("column")["value"].agg(["mean", "min", "max"])`
- `df.groupby("column").agg(new_column=("value", "mean"))`
- `pd.merge(left_df, right_df, on="key_column", how="inner")`
- `df["new_column"] = df["column"].map(dictionary)`
- `df["new_column"] = df.apply(function_name, axis=1)`

## Önemli Kavramlar

- **Named aggregation:** `agg()` içinde yeni sütun adını, kaynak sütunu ve hesaplama türünü birlikte yazmayı sağlar.
- **`merge()`:** İki tabloyu ortak bir sütun üzerinden birleştirir. SQL'deki join mantığına benzer.
- **`map()`:** Bir sütundaki değerleri dictionary yardımıyla başka değerlere dönüştürür.
- **`apply(axis=1)`:** Fonksiyonu her satır için çalıştırır. Satırdaki birden fazla sütuna göre karar vermek için kullanışlıdır.
- **`count` ve `sum` farkı:** Çalışan sayısı gibi adet hesaplarında `count`, değerleri toplamak istediğimiz durumlarda `sum` kullanılır.

## Yapılan Hatalar ve Düzeltmeler

### 1. `agg()` içine sütun adını ayrı argüman olarak vermek

`agg("salary", ["mean", "min", "max"])` doğru kullanım değildir. Önce sütun seçilir, sonra aggregation fonksiyonları verilir.

```python
merged_df.groupby("department")["salary"].agg(["mean", "min", "max"])
```

Named aggregation kullanırken ise sütun adı ve işlem tuple olarak yazılır.

```python
department_summary = merged_df.groupby("department").agg(
    average_salary=("salary", "mean"),
    highest_salary=("salary", "max"),
    employee_count=("employee_id", "count")
)
```

### 2. Çalışan sayısı için `sum` kullanmak

`employee_id` değerlerini toplamak çalışan sayısını vermez. Çalışan sayısı için `count` kullanılmalıdır.

```python
employee_count=("employee_id", "count")
```

### 3. `apply()` işlemini eski DataFrame'e uygulamak

`merge()` sonrası ana tablo `merged_df` olduğu için satır bazlı hesaplama da `merged_df` üzerinde yapılmalıdır.

```python
merged_df["level"] = merged_df.apply(employee_level, axis=1)
```

## Final Task Özeti

Final task'ta `employees` ve `departments` DataFrame'leri `department_id` üzerinden birleştirildi.

Yapılan işlemler:

- Çalışan bilgileri departman isimleriyle eşleştirildi.
- Departman bazında ortalama maaş, en yüksek maaş ve çalışan sayısı hesaplandı.
- Departman isimleri `map()` ile kısa departman kodlarına dönüştürüldü.
- Maaş ve deneyim bilgisine göre çalışan seviyesi `Senior`, `Mid` veya `Junior` olarak hesaplandı.
- Son çalışan DataFrame'i ve departman özet tablosu yazdırıldı.

## Gün Sonu Kazanımları

Bu günün sonunda Pandas'ta tek tek öğrenilen işlemler daha bütünlüklü bir analiz akışında birleştirildi. Özellikle `merge()` sonrası oluşan DataFrame'i ana çalışma tablosu olarak kullanmak ve aggregation işlemlerinde doğru hesaplama türünü seçmek önemli pratik kazanımlar oldu.
