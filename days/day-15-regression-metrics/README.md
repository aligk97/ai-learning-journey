# Day 15 - Regression Evaluation Metrics

## Günün Hedefi

Regresyon modellerini değerlendirmek için kullanılan MAE, MSE, RMSE ve R² metriklerini birlikte kullanmak ve özellikle daha önce eksik kalan RMSE metriğini öğrenmek.

## İşlenen Konular

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² (R-squared)
- Gerçek değerler ile tahminleri karşılaştırma
- Regresyon metriklerini birlikte yorumlama

## Temel Komutlar / Fonksiyonlar

- `mean_absolute_error(y_test, predictions)`
- `mean_squared_error(y_test, predictions)`
- `np.sqrt(mse)`
- `r2_score(y_test, predictions)`

## Önemli Kavramlar

- **MAE:** Tahmin hatalarının mutlak değerlerinin ortalamasıdır. Daha küçük değer daha iyidir.
- **MSE:** Tahmin hatalarının karelerinin ortalamasıdır. Büyük hataları daha fazla cezalandırır.
- **RMSE:** MSE'nin kareköküdür. Target ile aynı birimde olduğu için yorumlaması daha kolaydır.
- **R²:** Modelin target değişkenindeki değişimin ne kadarını açıkladığını gösterir. Daha yüksek değer genellikle daha iyidir.
- **R² accuracy değildir:** Classification accuracy metriği ile aynı şey değildir.

## Minitask Özeti

İlk görevde yalnızca RMSE üzerine çalışıldı.

Yapılan işlemler:

- `mean_squared_error` ile MSE hesaplandı.
- `np.sqrt(mse)` ile RMSE elde edildi.
- Sonuç yazdırıldı.

## Final Check Özeti

Final check'te şu gerçek ve tahmin değerleri kullanıldı:

```python
y_test = [55, 62, 70, 78, 85, 92]
predictions = [57, 60, 74, 75, 88, 89]
```

Aynı veri üzerinde:

- MAE hesaplandı.
- MSE hesaplandı.
- RMSE hesaplandı.
- R² hesaplandı.
- Tüm metrikler ayrı ayrı yazdırıldı.

Yaklaşık sonuçlar:

```text
MAE  = 2.83
MSE  = 8.50
RMSE = 2.92
R²   = 0.948
```

## Gün Sonu Kazanımları

Day 14'te kullanılan MAE, MSE ve R² metrikleri tekrar edilerek eksik olan RMSE eklendi. Böylece regresyon modellerini değerlendirmek için kullanılan dört temel metriğin birlikte hesaplanması ve yorumlanması tamamlandı.
