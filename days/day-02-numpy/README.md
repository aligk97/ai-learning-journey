# Day 02 - NumPy Basics

## Gunun Hedefi

NumPy array yapisini taniyip klasik Python listelerine gore neden daha pratik oldugunu anlamak; array ozelliklerini okuyabilmek ve basit secme/hesaplama islemleri yapabilmek.

## Islenen Konular

- NumPy import etme
- Python listesini NumPy array'e cevirme
- Array uzerinde toplu matematiksel islem yapma
- Array'in yapisini inceleme
- Boolean filtering ile veri secme
- Birden fazla kosulu birlikte kullanma
- Iki boyutlu array'lerde satir ve sutun mantigi
- `axis` kullanarak satir veya sutun bazli hesaplama

## Onemli Kavramlar

- **Array:** Ayni turdeki verileri daha hizli ve toplu islemek icin kullanilan NumPy veri yapisi.
- **Vectorized operation:** Dongu yazmadan array'in tum elemanlarina ayni islemi uygulama.
- **Boolean mask:** Kosulu saglayan elemanlari secmek icin `True` / `False` degerlerinden olusan filtre.
- **Axis:** Iki boyutlu veride hesaplamanin satirlara mi sutunlara mi uygulanacagini belirleyen yon.
- **Shape:** Array'in satir ve sutun bilgisini gosteren yapi.

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

- Skor listesini array'e cevirip tum elemanlari 2 ile carpma
- Array'in `shape`, `ndim`, `size`, `dtype` bilgilerini inceleme
- 60 ve uzeri notlari filtreleyip ortalama, en yuksek, en dusuk ve adet hesaplama
- 50 ile 90 arasindaki notlari secme
- Secilen notlara 5 puan ekleme
- 60 alti veya 90 ustu ekstrem notlari bulma
- Ogrenci-sinav tablosunda ogrenci ortalamalarini hesaplama
- Ortalamasi 75 ve uzeri olan ogrencileri secme

## Gun Sonu Ozeti

Bu gunde NumPy'in temel array mantigi ve listeye gore sagladigi pratiklik goruldu. Ozellikle kosula gore veri secme ve `axis` kullanarak iki boyutlu verilerde satir/sutun bazli hesaplama yapma alistirmalari one cikti.

Final task'ta ogrencilerin sinav notlari iki boyutlu array olarak tutuldu; ogrenci ortalamalari, basarili ogrenciler, sinif ortalamasi, her ogrencinin en yuksek notu ve ekstrem ortalamalar hesaplandi.
