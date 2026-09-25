# Day 18 - Feature Scaling

## Konular

- Feature scaling mantığı
- StandardScaler
- MinMaxScaler
- fit, transform ve fit_transform
- Train/test preprocessing mantığı
- Data leakage
- Outlier'ların scaling üzerindeki etkisi
- StandardScaler ve MinMaxScaler farkı

## StandardScaler

StandardScaler her feature'ı ortalama yaklaşık 0 ve standart sapma yaklaşık 1 olacak şekilde dönüştürür.

```python
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Train verisinde `fit_transform`, test verisinde yalnızca `transform` kullanılır.

## fit ve transform

- `fit()`: Train verisinden gerekli istatistikleri öğrenir.
- `transform()`: Öğrenilen kuralları veriye uygular.
- `fit_transform()`: Önce öğrenir, sonra aynı veriyi dönüştürür.

Test verisinde tekrar `fit` yapmak test verisinden bilgi öğrenilmesine neden olur. Bu durum **data leakage** oluşturur.

## MinMaxScaler

MinMaxScaler varsayılan olarak değerleri 0 ile 1 aralığına getirir.

- Minimum değer → 0
- Maksimum değer → 1
- Diğer değerler → aradaki konumlarına göre 0 ile 1 arasında

## StandardScaler vs MinMaxScaler

### StandardScaler

- Ortalama yaklaşık 0
- Standart sapma yaklaşık 1
- Negatif değerler oluşabilir
- Sabit bir aralığa sıkıştırmaz

### MinMaxScaler

- Değerleri genellikle 0-1 aralığına getirir
- Minimum ve maksimum değerlere doğrudan bağlıdır
- Outlier olduğunda normal değerler dar bir aralığa sıkışabilir

## Outlier Etkisi

Hem StandardScaler hem de MinMaxScaler outlier'lardan etkilenebilir.

MinMaxScaler doğrudan minimum ve maksimum değerleri kullandığı için uç değerlerin etkisi özellikle belirgin olabilir.

StandardScaler ise mean ve standard deviation kullandığından outlier'lar bu istatistikleri değiştirebilir.

## Gün Sonu Özeti

Feature scaling'in amacı, ölçeğe duyarlı algoritmalarda feature'ların yalnızca sayısal büyüklükleri nedeniyle hesaplamaları gereksiz şekilde domine etmesini önlemektir.

Bu günün temel preprocessing kuralı:

```text
Train → fit_transform
Test  → transform
```
