# Day 03 - NumPy Array Manipulation

## Gunun Hedefi

NumPy array'lerinde veri secmeyi ve array'in seklini degistirmeyi ogrenmek: slicing, sutun secme, transpose, flatten ve reshape islemlerini rahat kullanabilmek.

## Islenen Konular

- Iki boyutlu array'lerde satir ve sutun secme
- Slicing ile belirli araliklari alma
- Fancy indexing ile belirli sutunlari secme
- Negatif index kullanma
- `reshape()` ile array boyutunu degistirme
- `flatten()` ile array'i tek boyuta indirme
- `.T` ile transpose alma
- Islemleri arka arkaya baglama

## Onemli Kavramlar

- **Slicing:** Array'in belirli bir satir/sutun araligini secme.
- **Fancy indexing:** Liste vererek belirli satir veya sutunlari secme.
- **Transpose:** Satirlari sutunlara, sutunlari satirlara cevirme.
- **Flatten:** Cok boyutlu array'i tek boyutlu hale getirme.
- **Reshape:** Eleman sayisi ayni kalacak sekilde array'in satir/sutun yapisini degistirme.

## Temel Komutlar / Fonksiyonlar

- `scores[:, 1]`
- `scores[:4, [1, 3]]`
- `scores[-3:, :]`
- `.reshape(2, 3)`
- `.reshape(2, 6)`
- `.flatten()`
- `.T`

## Mini Tasklar

- Tum ogrencilerin ikinci sinav notlarini secme
- Belirli ogrencilerin belirli sinavlarini alma
- Tek boyutlu array'i 2 satir 3 sutun hale getirme
- Iki boyutlu array'i tek boyuta indirme
- Array'in transpose'unu alma
- Son iki satirdan belirli sutunlari secme
- Veriyi flatten edip farkli boyutta reshape etme
- Transpose sonrasi flatten islemini gorme

## Gun Sonu Ozeti

Bu gunde array icinden parca secme ve array'in formunu degistirme pratik edildi. Makine ogrenmesi ve veri analizinde veri bazen satir-sutun halinde, bazen tek boyutlu, bazen de farkli sekilde modele verilmek zorunda kalir. Bu gunun ana kazanimi, ayni veriyi farkli sekillerde duzenleyebilmektir.

Final task'ta ilk 4 ogrencinin 2. ve 4. sinavlari secildi, transpose edildi, tek boyuta indirildi ve yeniden 4 satir 2 sutun olacak sekilde duzenlendi. Ayrica son 3 ogrencinin tum notlari 2 satir 6 sutunluk yeni bir array'e cevrildi.
