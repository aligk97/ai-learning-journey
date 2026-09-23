# Day 14 - Linear Regression

## Günün Hedefi

Makine öğrenmesi akışını baştan sona kurmak: veriyi feature ve target olarak ayırmak, train/test split yapmak, Linear Regression modelini eğitmek, test verisi üzerinde tahmin almak, modeli metriklerle değerlendirmek ve regression doğrusunu grafik üzerinde göstermek.

## İşlenen Konular

- Feature ve target ayrımı
- `X` ve `y` değişkenlerini hazırlama
- `train_test_split` ile train ve test verisi oluşturma
- `LinearRegression` modeli oluşturma
- `fit` ile modeli eğitme
- `predict` ile tahmin yapma
- Gerçek değerler ve tahminleri aynı DataFrame içinde karşılaştırma
- Coefficient ve intercept değerlerini yorumlama
- MAE, MSE ve R2 metriklerini hesaplama
- Yeni veri için model tahmini yapma
- Model tahminini manuel regression formülüyle kontrol etme
- Scatter plot ve regression line çizme

## Temel Komutlar / Fonksiyonlar

- `X = df[["feature_column"]]`
- `y = df["target_column"]`
- `train_test_split(X, y, test_size=0.25, random_state=42)`
- `LinearRegression()`
- `model.fit(X_train, y_train)`
- `model.predict(X_test)`
- `model.coef_`
- `model.intercept_`
- `mean_absolute_error(y_test, predictions)`
- `mean_squared_error(y_test, predictions)`
- `r2_score(y_test, predictions)`
- `plt.scatter(x, y)`
- `plt.plot(x, y)`

## Önemli Kavramlar

- **Feature:** Modelin tahmin yaparken kullandığı giriş değişkenidir. Bu örnekte `study_hours`.
- **Target:** Modelin tahmin etmeye çalıştığı sonuç değişkenidir. Bu örnekte `score`.
- **X:** Feature verilerini tutar. Scikit-learn için genellikle DataFrame olarak hazırlanır.
- **y:** Target verisini tutar. Genellikle Series olarak hazırlanır.
- **Train data:** Modelin ilişkiyi öğrenmek için kullandığı veridir.
- **Test data:** Modelin daha önce görmediği veriler üzerinde ne kadar başarılı olduğunu ölçmek için kullanılır.
- **Coefficient:** Feature 1 birim arttığında tahminin yaklaşık ne kadar değiştiğini gösterir.
- **Intercept:** Feature değeri 0 olduğunda modelin tahmin ettiği başlangıç değeridir.
- **MAE:** Tahmin hatalarının mutlak değerlerinin ortalamasıdır.
- **MSE:** Hataların karelerinin ortalamasıdır. Büyük hataları daha fazla cezalandırır.
- **R2:** Modelin target değişkendeki değişimi ne kadar açıkladığını gösterir.
- **Regression line:** Modelin öğrendiği doğrusal ilişkiyi grafik üzerinde gösteren çizgidir.

## Yapılan Hatalar ve Düzeltmeler

### 1. Results DataFrame oluştururken değerleri tekrar liste içine almak

`X_test`, `y_test` ve `predictions` zaten birden fazla değer içerdiği için tekrar `[]` içine alınmamalıdır.

Doğru kullanım:

```python
results = pd.DataFrame({
    "study_hours": X_test["study_hours"].values,
    "actual_score": y_test.values,
    "predicted_score": predictions
})
```

### 2. `predicted_score` sütun adını yanlış yazmak

Sütun adı `precicted_score` değil, `predicted_score` olmalıdır.

### 3. Manuel tahminde coefficient değerini doğrudan array olarak kullanmak

`model.coef_` bir array döndürür. Tek feature olduğu için ilk değer `model.coef_[0]` ile alınabilir.

```python
manual_prediction = intercept + coefficient * 7.5
```

## Final Check Özeti

Final check'te `study_hours` ve `score` sütunlarından oluşan öğrenci DataFrame'i kullanıldı.

Yapılan işlemler:

- `study_hours` feature olarak `X` değişkenine atandı.
- `score` target olarak `y` değişkenine atandı.
- Veri `test_size=0.25` ve `random_state=42` ile train/test olarak ayrıldı.
- `LinearRegression` modeli oluşturuldu ve train verisiyle eğitildi.
- Test verisi için tahminler üretildi.
- Gerçek score değerleri ve tahminler aynı DataFrame içinde karşılaştırıldı.
- Coefficient ve intercept değerleri yazdırıldı.
- MAE, MSE ve R2 metrikleri hesaplandı.
- 7.5 saat çalışan yeni bir öğrenci için model tahmini yapıldı.
- Aynı tahmin regression formülüyle manuel olarak hesaplandı.
- Tüm gerçek veriler scatter plot ile çizildi.
- Modelin öğrendiği regression doğrusu aynı grafiğe eklendi.

Beklenen önemli sonuçlar:

```text
coefficient ~= 5.071
intercept   ~= 38.223
7.5 hours prediction ~= 76.26
```

## Gün Sonu Kazanımları

Bu günün sonunda klasik supervised learning akışı baştan sona uygulandı. Verinin feature ve target olarak ayrılması, modelin eğitilmesi, test verisiyle değerlendirilmesi, yeni veri için tahmin alınması ve regression doğrusunun görselleştirilmesi birlikte tekrar edildi.
