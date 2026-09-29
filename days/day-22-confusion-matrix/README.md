# Day 22 - Confusion Matrix

## Konular

- Classification model evaluation
- Confusion Matrix
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)
- True Positive (TP)
- `confusion_matrix()`
- `cm.ravel()`

## Confusion Matrix Nedir?

Confusion matrix, classification modelinin tahminlerini gerçek değerlerle karşılaştıran bir tablodur.

Accuracy sadece kaç tahminin doğru olduğunu söyler. Confusion matrix ise modelin hangi sınıfta doğru, hangi sınıfta yanlış yaptığını gösterir.

Binary classification için temel yapı:

```text
[[TN, FP],
 [FN, TP]]
```

Burada:

- `TN`: Gerçek değer `0`, tahmin `0`
- `FP`: Gerçek değer `0`, tahmin `1`
- `FN`: Gerçek değer `1`, tahmin `0`
- `TP`: Gerçek değer `1`, tahmin `1`

## Scikit-learn ile Kullanımı

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, predictions)
```

Binary classification sonucunda dört değeri ayrı ayrı almak için:

```python
tn, fp, fn, tp = cm.ravel()
```

Bu değerleri ayrı okumak modelin hata türlerini anlamayı kolaylaştırır.

## Final Check Özeti

Final check'te öğrencilerin dersten geçip geçmediğini tahmin eden küçük bir classification örneği kullanıldı.

Yapılan işlemler:

- `study_hours` ve `attendance` feature olarak `X` değişkenine atandı.
- `passed` target olarak `y` değişkenine atandı.
- Veri train/test olarak ayrıldı.
- `LogisticRegression` modeli eğitildi.
- Test verisi üzerinde tahmin yapıldı.
- `confusion_matrix()` ile sonuçlar tablo haline getirildi.
- `tn`, `fp`, `fn`, `tp` değerleri `cm.ravel()` ile ayrıldı.

## Gün Sonu Özeti

Day 22 sonunda classification modellerinin sonuçlarını daha detaylı okumak için confusion matrix öğrenildi.

Bu günün temel fikri:

```text
Accuracy kaç tahminin doğru olduğunu söyler.
Confusion matrix hangi tahminlerin nasıl doğru veya yanlış olduğunu gösterir.
```

## Next

Day 23 - Accuracy, Precision, Recall, F1
