# Day 04 - NumPy Math, Filtering and Statistics

## Gunun Hedefi

NumPy ile veriler uzerinde matematiksel islemler, temel istatistik hesaplari, kosullu filtreleme ve sonuc yorumlama yapabilmek.

## Islenen Konular

- Array uzerinde toplu matematiksel islemler
- Toplam, ortalama, minimum, maksimum ve standart sapma hesaplama
- Iki boyutlu veride `axis=0` ve `axis=1` kullanimi
- Boolean filtering ile aralik secme
- Birden fazla kosulu birlikte kullanma
- `np.where()` ile kosula gore etiket uretme
- `any()` ve `all()` ile genel kontrol yapma
- `argmax()` ve `argmin()` ile en buyuk/en kucuk degerin indexini bulma

## Onemli Kavramlar

- **Vectorized math:** Array'in tum elemanlarina ayni matematiksel islemi tek satirda uygulama.
- **Statistics:** Verinin genel durumunu ozetleyen ortalama, standart sapma, min ve max gibi degerler.
- **Boolean filtering:** Veriyi belirli kosullara gore secme.
- **Conditional labeling:** Kosula gore `"Passed"` / `"Failed"` gibi anlamli etiketler uretme.
- **Index of extreme values:** En buyuk veya en kucuk degerin kendisi yerine konumunu bulma.

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

- Fiyatlara yuzde 20 zam uygulama, indirim yapma ve yari fiyat hesaplama
- Sicaklik array'inde toplam, ortalama, min ve max bulma
- Satis tablosunda sutun ve satir bazli ortalama, maksimum ve toplam hesaplama
- Standart sapma ile verinin yayilimini inceleme
- Sicakliklari belirli araliklara gore filtreleme
- Notlari `Passed` / `Failed` olarak etiketleme
- `any()` ve `all()` ile genel kosul kontrolleri yapma
- En pahali/en ucuz urunun indexini bulma
- Iki boyutlu veride satir ve sutun bazli `argmax` / `argmin` kullanma

## Gun Sonu Ozeti

Bu gunde NumPy ile veriyi sadece saklamayi degil, analiz etmeyi de pratik ettik. Matematiksel islemler, istatistiksel ozetler, kosullu filtreler ve kosula gore etiketleme ayni gun icinde birlestirildi.

Final task'ta ogrencilerin ortalamalari hesaplandi, basarili ogrenciler filtrelendi, her ogrenci icin gecme/kalma etiketi uretildi, sinifta 90 uzeri ortalama olup olmadigi kontrol edildi ve en yuksek performansli ogrencinin indexi bulundu.
