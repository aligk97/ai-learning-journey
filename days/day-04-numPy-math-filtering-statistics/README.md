# Day 04 - NumPy Math, Filtering and Statistics

## Günün Hedefi

NumPy ile veriler üzerinde matematiksel işlemler, temel istatistik hesapları, koşullu filtreleme ve sonuç yorumlama yapabilmek.

## İşlenen Konular

- Array üzerinde toplu matematiksel işlemler
- Toplam, ortalama, minimum, maksimum ve standart sapma hesaplama
- İki boyutlu veride `axis=0` ve `axis=1` kullanımı
- Boolean filtering ile aralık seçme
- Birden fazla koşulu birlikte kullanma
- `np.where()` ile koşula göre etiket üretme
- `any()` ve `all()` ile genel kontrol yapma
- `argmax()` ve `argmin()` ile en büyük/en küçük değerin indexini bulma

## Önemli Kavramlar

- **Vectorized math:** Array'in tüm elemanlarına aynı matematiksel işlemi tek satırda uygulama.
- **Statistics:** Verinin genel durumunu özetleyen ortalama, standart sapma, min ve max gibi değerler.
- **Boolean filtering:** Veriyi belirli koşullara göre seçme.
- **Conditional labeling:** Koşula göre `"Passed"` / `"Failed"` gibi anlamlı etiketler üretme.
- **Index of extreme values:** En büyük veya en küçük değerin kendisi yerine konumunu bulma.

## Temel Komutlar / Fonksiyonlar

- `.sum()`
- `.mean()`
- `.std()`
- `.min()`
- `.max()`
- `.mean(axis=0)`
- `.mean(axis=1)`
- `array[(condition1) & (condition2)]`
- `array[(condition1) | (condition2)]`
- `np.where(condition, value_if_true, value_if_false)`
- `.any()`
- `.all()`
- `.argmax()`
- `.argmin()`

## Mini Tasklar

- Fiyatlara yüzde 20 zam uygulama, indirim yapma ve yarı fiyat hesaplama
- Sıcaklık array'inde toplam, ortalama, min ve max bulma
- Satış tablosunda sütun ve satır bazlı ortalama, maksimum ve toplam hesaplama
- Standart sapma ile verinin yayılımını inceleme
- Sıcaklıkları belirli aralıklara göre filtreleme
- Notları `Passed` / `Failed` olarak etiketleme
- `any()` ve `all()` ile genel koşul kontrolleri yapma
- En pahalı/en ucuz ürünün indexini bulma
- İki boyutlu veride satır ve sütun bazlı `argmax` / `argmin` kullanma

## Gün Sonu Özeti

Bu günde NumPy ile veriyi sadece saklamayı değil, analiz etmeyi de pratik ettik. Matematiksel işlemler, istatistiksel özetler, koşullu filtreler ve koşula göre etiketleme aynı gün içinde birleştirildi.

Final task'ta öğrencilerin ortalamaları hesaplandı, başarılı öğrenciler filtrelendi, her öğrenci için geçme/kalma etiketi üretildi, sınıfta 90 üzeri ortalama olup olmadığı kontrol edildi ve en yüksek performanslı öğrencinin indexi bulundu.
