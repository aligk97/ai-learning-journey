# Day 22 - Confusion Matrix: TP, TN, FP, FN

## Konular

- Confusion matrix
- True Positive
- True Negative
- False Positive
- False Negative
- `confusion_matrix()`
- `y_test` ve `predictions` karşılaştırması
- Accuracy sonucunu daha detaylı okuma
- Classification hatalarını yorumlama

## Confusion Matrix

Confusion matrix, classification modelinin tahminlerini gerçek değerlerle karşılaştıran bir tablodur.

Accuracy sadece kaç tahminin doğru olduğunu söyler. Confusion matrix ise modelin hangi sınıfta doğru, hangi sınıfta yanlış yaptığını gösterir.

Binary classification için temel yapı:

```text
[[TN, FP],
 [FN, TP]]
```

Burada:

- `TN`: True Negative
- `FP`: False Positive
- `FN`: False Negative
- `TP`: True Positive

## TP, TN, FP, FN Mantığı

Örnek olarak `purchased` target değişkenini düşünelim:

```text
0 -> Satın almadı
1 -> Satın aldı
```

### True Positive

Gerçek değer `1`, model tahmini de `1` ise sonuç True Positive olur.

```text
Gerçek: 1
Tahmin: 1
```

Model satın alan kişiyi doğru şekilde satın aldı olarak tahmin etmiştir.

### True Negative

Gerçek değer `0`, model tahmini de `0` ise sonuç True Negative olur.

```text
Gerçek: 0
Tahmin: 0
```

Model satın almayan kişiyi doğru şekilde satın almadı olarak tahmin etmiştir.

### False Positive

Gerçek değer `0`, model tahmini `1` ise sonuç False Positive olur.

```text
Gerçek: 0
Tahmin: 1
```

Model satın almayan kişiyi yanlış şekilde satın aldı olarak tahmin etmiştir.

### False Negative

Gerçek değer `1`, model tahmini `0` ise sonuç False Negative olur.

```text
Gerçek: 1
Tahmin: 0
```

Model satın alan kişiyi yanlış şekilde satın almadı olarak tahmin etmiştir.

## Scikit-learn ile Confusion Matrix

Confusion matrix hesaplamak için `sklearn.metrics` içinden `confusion_matrix` import edilir.

```python
from sklearn.metrics import confusion_matrix

matrix = confusion_matrix(y_test, predictions)

print(matrix)
```

Binary classification için değerleri ayrı değişkenlere almak mümkündür.

```python
tn, fp, fn, tp = confusion_matrix(y_test, predictions).ravel()
```

Bu sayede sonuçlar tek tek okunabilir:

```python
print("True Negative:", tn)
print("False Positive:", fp)
print("False Negative:", fn)
print("True Positive:", tp)
```

## Accuracy Neden Tek Başına Yetmeyebilir?

Accuracy genel doğru tahmin oranını verir.

Fakat bazı problemlerde yanlış tahminlerin türü çok önemlidir.

Örneğin:

- Hasta olan bir kişiyi sağlıklı tahmin etmek ciddi bir hatadır.
- Dolandırıcılık yapan bir işlemi normal tahmin etmek ciddi bir hatadır.
- Satın alacak müşteriyi kaçırmak iş açısından önemli olabilir.

Bu yüzden classification problemlerinde sadece accuracy değerine bakmak yerine confusion matrix ile hatanın türünü de okumak gerekir.

## Final Check Özeti

Final check'te Day 21'deki Logistic Regression akışı confusion matrix ile genişletildi.

Yapılan işlemler:

- `age`, `income` ve `purchased` sütunlarından oluşan müşteri verisi kullanıldı.
- `age` ve `income` feature olarak `X` değişkenine atandı.
- `purchased` target olarak `y` değişkenine atandı.
- Veri train/test olarak ayrıldı.
- `LogisticRegression` modeli train verisiyle eğitildi.
- Test verisi üzerinde sınıf tahminleri yapıldı.
- `accuracy_score` ile accuracy hesaplandı.
- `confusion_matrix` ile tahminlerin detaylı sonucu çıkarıldı.
- `tn`, `fp`, `fn`, `tp` değerleri ayrı ayrı okundu.

## Gün Sonu Özeti

Day 22 sonunda classification modellerinin sonuçlarını daha detaylı okumak için confusion matrix öğrenildi.

Bu günün temel fikri:

```text
Accuracy kaç tahminin doğru olduğunu söyler.
Confusion matrix hangi tahminlerin nasıl doğru veya yanlış olduğunu gösterir.
```

## Next

Day 23 - Accuracy, Precision, Recall, F1
