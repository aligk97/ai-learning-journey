# Day 17 - Underfitting & Overfitting

## Konular

- Underfitting
- Good fit
- Overfitting
- Train ve test performansını birlikte değerlendirme
- Train-test gap mantığı
- Overfitting azaltma yöntemleri
- Regularization'a giriş

## Temel Mantık

### Underfitting

Model verideki ilişkiyi yeterince öğrenemez.

- Train performansı düşük
- Test performansı düşük
- Model fazla basit olabilir

### Good Fit

Model training verisini öğrenirken yeni veriler üzerinde de iyi performans gösterir.

- Train performansı iyi
- Test performansı iyi
- Train-test farkı makuldür

### Overfitting

Model training verisini gereğinden fazla öğrenir ve yeni verilerde performansı düşer.

- Train performansı çok yüksek
- Test performansı belirgin şekilde daha düşük
- Train-test gap büyür

## Overfitting Nasıl Azaltılabilir?

- Model karmaşıklığını azaltmak
- Polynomial degree gibi parametreleri düşürmek
- Daha fazla training verisi kullanmak
- Regularization kullanmak

## Not

Train-test gap için evrensel bir eşik yoktur.
Sonuçlar veri setine ve probleme göre değerlendirilmelidir.

Regularization konusu ilerleyen günlerde daha detaylı ele alınacaktır.
