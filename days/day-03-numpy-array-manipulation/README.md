# Day 03 - NumPy Array Manipulation

## Günün Hedefi

NumPy array'lerinde veri seçmeyi ve array'in şeklini değiştirmeyi öğrenmek: slicing, sütun seçme, transpose, flatten ve reshape işlemlerini rahat kullanabilmek.

## İşlenen Konular

- İki boyutlu array'lerde satır ve sütun seçme
- Slicing ile belirli aralıkları alma
- Fancy indexing ile belirli sütunları seçme
- Negatif index kullanma
- `reshape()` ile array boyutunu değiştirme
- `flatten()` ile array'i tek boyuta indirme
- `.T` ile transpose alma
- İşlemleri arka arkaya bağlama

## Önemli Kavramlar

- **Slicing:** Array'in belirli bir satır/sütun aralığını seçme.
- **Fancy indexing:** Liste vererek belirli satır veya sütunları seçme.
- **Transpose:** Satırları sütunlara, sütunları satırlara çevirme.
- **Flatten:** Çok boyutlu array'i tek boyutlu hale getirme.
- **Reshape:** Eleman sayısı aynı kalacak şekilde array'in satır/sütun yapısını değiştirme.

## Temel Komutlar / Fonksiyonlar

- `scores[:, 1]`
- `scores[:4, [1, 3]]`
- `scores[-3:, :]`
- `.reshape(2, 3)`
- `.reshape(2, 6)`
- `.flatten()`
- `.T`

## Mini Tasklar

- Tüm öğrencilerin ikinci sınav notlarını seçme
- Belirli öğrencilerin belirli sınavlarını alma
- Tek boyutlu array'i 2 satır 3 sütun hale getirme
- İki boyutlu array'i tek boyuta indirme
- Array'in transpose'unu alma
- Son iki satırdan belirli sütunları seçme
- Veriyi flatten edip farklı boyutta reshape etme
- Transpose sonrası flatten işlemini görme

## Gün Sonu Özeti

Bu günde array içinden parça seçme ve array'in formunu değiştirme pratik edildi. Makine öğrenmesi ve veri analizinde veri bazen satır-sütun halinde, bazen tek boyutlu, bazen de farklı şekilde modele verilmek zorunda kalır. Bu günün ana kazanımı, aynı veriyi farklı şekillerde düzenleyebilmektir.

Final task'ta ilk 4 öğrencinin 2. ve 4. sınavları seçildi, transpose edildi, tek boyuta indirildi ve yeniden 4 satır 2 sütun olacak şekilde düzenlendi. Ayrıca son 3 öğrencinin tüm notları 2 satır 6 sütunluk yeni bir array'e çevrildi.
