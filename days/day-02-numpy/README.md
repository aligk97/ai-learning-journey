# Day 02 - NumPy Basics

## Günün Hedefi

NumPy array yapısını tanıyıp klasik Python listelerine göre neden daha pratik olduğunu anlamak; array özelliklerini okuyabilmek ve basit seçme/hesaplama işlemleri yapabilmek.

## İşlenen Konular

- NumPy import etme
- Python listesini NumPy array'e çevirme
- Array üzerinde toplu matematiksel işlem yapma
- Array'in yapısını inceleme
- Boolean filtering ile veri seçme
- Birden fazla koşulu birlikte kullanma
- İki boyutlu array'lerde satır ve sütun mantığı
- `axis` kullanarak satır veya sütun bazlı hesaplama

## Önemli Kavramlar

- **Array:** Aynı türdeki verileri daha hızlı ve toplu işlemek için kullanılan NumPy veri yapısı.
- **Vectorized operation:** Döngü yazmadan array'in tüm elemanlarına aynı işlemi uygulama.
- **Boolean mask:** Koşulu sağlayan elemanları seçmek için `True` / `False` değerlerinden oluşan filtre.
- **Axis:** İki boyutlu veride hesaplamanın satırlara mı sütunlara mı uygulanacağını belirleyen yön.
- **Shape:** Array'in satır ve sütun bilgisini gösteren yapı.

## Temel Komutlar / Fonksiyonlar

- `import numpy as np`
- `np.array()`
- `.shape`
- `.ndim`
- `.size`
- `.dtype`
- `.mean()`
- `.max()`
- `.min()`
- `scores[scores >= 60]`
- `(condition1) & (condition2)`
- `(condition1) | (condition2)`
- `.mean(axis=1)`
- `.mean(axis=0)`

## Mini Tasklar

- Skor listesini array'e çevirip tüm elemanları 2 ile çarpma
- Array'in `shape`, `ndim`, `size`, `dtype` bilgilerini inceleme
- 60 ve üzeri notları filtreleyip ortalama, en yüksek, en düşük ve adet hesaplama
- 50 ile 90 arasındaki notları seçme
- Seçilen notlara 5 puan ekleme
- 60 altı veya 90 üstü ekstrem notları bulma
- Öğrenci-sınav tablosunda öğrenci ortalamalarını hesaplama
- Ortalaması 75 ve üzeri olan öğrencileri seçme

## Gün Sonu Özeti

Bu günde NumPy'in temel array mantığı ve listeye göre sağladığı pratiklik görüldü. Özellikle koşula göre veri seçme ve `axis` kullanarak iki boyutlu verilerde satır/sütun bazlı hesaplama yapma alıştırmaları öne çıktı.

Final task'ta öğrencilerin sınav notları iki boyutlu array olarak tutuldu; öğrenci ortalamaları, başarılı öğrenciler, sınıf ortalaması, her öğrencinin en yüksek notu ve ekstrem ortalamalar hesaplandı.
