# Day 23 - Classification Metrics

## Konular

- Accuracy
- Precision
- Recall
- F1 Score
- Classification model evaluation
- Doğru metriği seçme

## Accuracy

Accuracy, modelin tüm tahminleri içinde kaç tanesinin doğru olduğunu gösterir.

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
```

Örnek:

```text
0.80 = tahminlerin %80'i doğru
```

Accuracy dengeli veri setlerinde faydalıdır. Fakat sınıflar dengesizse tek başına yanıltıcı olabilir.

## Precision

Precision, modelin `1` diye tahmin ettiği örneklerin kaçının gerçekten `1` olduğunu gösterir.

```python
from sklearn.metrics import precision_score

precision = precision_score(y_test, predictions)
```

Precision özellikle false positive hatasının önemli olduğu durumlarda önemlidir.

Örnek:

```text
Model "satın alacak" dediğinde ne kadar güvenilir?
```

## Recall

Recall, gerçek değeri `1` olan örneklerin kaçını modelin yakalayabildiğini gösterir.

```python
from sklearn.metrics import recall_score

recall = recall_score(y_test, predictions)
```

Recall özellikle false negative hatasının önemli olduğu durumlarda önemlidir.

Örnek:

```text
Gerçekten hasta olan kişilerin kaçını yakaladık?
```

## F1 Score

F1 Score, precision ve recall değerlerini tek bir dengeli skor olarak birleştirir.

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_test, predictions)
```

Precision ve recall arasında denge kurmak istediğimizde F1 Score kullanışlıdır.

## Metrik Seçimi

Her classification problemi için en iyi metrik aynı değildir.

- Genel başarıyı görmek için `accuracy`
- Yanlış alarmı azaltmak için `precision`
- Kaçırılan pozitif örnekleri azaltmak için `recall`
- Precision ve recall dengesini görmek için `f1`

## Final Check Özeti

Final check'te öğrencilerin dersten geçip geçmediğini tahmin eden küçük bir classification modeli kuruldu.

Yapılan işlemler:

- `study_hours`, `attendance` ve `practice_score` feature olarak kullanıldı.
- `passed` target olarak seçildi.
- Veri train/test olarak ayrıldı.
- `LogisticRegression` modeli eğitildi.
- Test verisi üzerinde tahmin yapıldı.
- Accuracy, precision, recall ve F1 score hesaplandı.

## Gün Sonu Özeti

Day 23 sonunda classification modellerinde tek bir doğru metrik olmadığını öğrendik.

Bu günün temel fikri:

```text
Accuracy genel başarıyı gösterir.
Precision yanlış pozitiflere odaklanır.
Recall kaçırılan pozitiflere odaklanır.
F1 precision ve recall arasında denge kurar.
```

## Next

Day 24 - KNN
