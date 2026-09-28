# Day 21 - Logistic Regression + Sigmoid

## Konular

- Logistic Regression
- Classification mantığı
- Binary classification
- Sigmoid fonksiyonu
- `predict()`
- `predict_proba()`
- Classification threshold
- Custom threshold mantığı
- Yeni veri üzerinde tahmin
- Train/test workflow
- Accuracy score

## Logistic Regression

Logistic Regression, ismine rağmen çoğunlukla classification problemlerinde kullanılır.

Regression tarafında model sürekli bir sayı tahmin ederken, classification tarafında model bir sınıf tahmin eder.

Örneğin:

```text
0 -> Not Purchased
1 -> Purchased
```

Bu günün ana farkı:

```text
Linear Regression  -> sayı tahmini
Logistic Regression -> sınıf tahmini
```

## Sigmoid Mantığı

Logistic Regression modelinin çıktısı olasılık olarak yorumlanır.

Sigmoid fonksiyonu değerleri `0` ile `1` aralığına sıkıştırır.

Örneğin:

```text
0.18 -> class 1 olma ihtimali düşük
0.84 -> class 1 olma ihtimali yüksek
```

Bu yüzden Logistic Regression, bir örneğin hangi sınıfa ait olabileceğini olasılık üzerinden değerlendirir.

## predict()

`predict()` doğrudan final sınıf tahminini döndürür.

```python
predictions = model.predict(X_test)
```

Örnek çıktı:

```text
[0, 0, 1, 1]
```

Bu çıktı artık sürekli sayılar değil, sınıf etiketleridir.

## predict_proba()

`predict_proba()` her sınıf için olasılık değerlerini döndürür.

```python
probabilities = model.predict_proba(X_test)
```

Binary classification için her satır genelde şu yapıda olur:

```text
[class_0_probability, class_1_probability]
```

Sadece `1` sınıfının olasılığını almak için ikinci sütun seçilir:

```python
class_1_probabilities = model.predict_proba(X_test)[:, 1]
```

## Classification Threshold

Varsayılan threshold çoğunlukla `0.5` olarak düşünülür.

```text
probability < 0.5  -> class 0
probability >= 0.5 -> class 1
```

Aynı mantık elle de yazılabilir:

```python
custom_predictions = []

for probability in probabilities:
    if probability >= 0.5:
        custom_predictions.append(1)
    else:
        custom_predictions.append(0)
```

Bu mantık, `predict()` fonksiyonunun arka plandaki karar verme fikrini daha anlaşılır hale getirir.

## Yeni Veri Üzerinde Tahmin

Model eğitildikten sonra daha önce görmediği yeni bir müşteri için sınıf tahmini yapılabilir.

```python
new_customer = pd.DataFrame({
    "age": [37],
    "income": [44000]
})

prediction = model.predict(new_customer)
probability = model.predict_proba(new_customer)[:, 1]
```

Burada:

- `prediction` final sınıfı verir.
- `probability` ilgili sınıfa ait olasılığı verir.

## Accuracy

Accuracy, modelin test verisindeki tahminlerinin ne kadarının doğru olduğunu gösterir.

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
```

Örneğin:

```text
0.80 = tahminlerin %80'i doğru
```

Accuracy classification için başlangıçta faydalı bir metriktir, fakat tek başına her zaman yeterli değildir. Bu yüzden sonraki gün confusion matrix ile sonuçları daha detaylı okumak gerekir.

## Final Check Özeti

Final check'te `age`, `income` ve `purchased` sütunlarından oluşan küçük bir müşteri DataFrame'i kullanıldı.

Yapılan işlemler:

- `age` ve `income` feature olarak `X` değişkenine atandı.
- `purchased` target olarak `y` değişkenine atandı.
- Veri train/test olarak ayrıldı.
- `LogisticRegression` modeli oluşturuldu.
- Model yalnızca train verisiyle eğitildi.
- Test verisi üzerinde sınıf tahminleri yapıldı.
- `accuracy_score` ile accuracy hesaplandı.
- Test verisi için `purchased=1` olasılıkları alındı.
- Yeni bir müşteri için hem sınıf tahmini hem de satın alma olasılığı hesaplandı.

## Gün Sonu Özeti

Day 21 sonunda regression problemlerinden classification problemlerine geçiş yapıldı.

Bu günün temel fikri:

```text
Model sadece sınıf tahmini yapmaz;
aynı zamanda bu sınıfa ait olasılığı da hesaplayabilir.
```

## Next

Day 22 - Confusion Matrix: TP, TN, FP, FN
