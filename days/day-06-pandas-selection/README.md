# Day 06 - Pandas Selection

## Günün Hedefi

Pandas DataFrame içinde belirli satırları, sütunları ve koşula uyan verileri rahatça seçmeyi öğrenmek.

## İşlenen Konular

- Birden fazla sütun seçme
- `iloc` ile pozisyona göre satır/sütun seçme
- `loc` ile index ve sütun adına göre seçim yapma
- Boolean filtering ile koşula göre satır seçme
- `&` ile birden fazla koşulu birlikte kullanma
- `|` ile koşullardan en az birini sağlayan satırları seçme
- Filtreleme yaptıktan sonra sadece gerekli sütunları alma

## Temel Komutlar / Fonksiyonlar

- `students[["name", "score"]]`
- `students.iloc[:3, [0, 1, 2]]`
- `students.loc[2:4, ["name", "city"]]`
- `students[students["score"] >= 70]`
- `students[(condition1) & (condition2)]`
- `students[(condition1) | (condition2)]`
- `students.loc[row_filter, ["name", "score"]]`

## Önemli Kavramlar

- **Sütun seçimi:** Tek sütun seçerken string, birden fazla sütun seçerken liste kullanılır.
- **`iloc`:** Satır ve sütunları sayısal pozisyona göre seçer.
- **`loc`:** Satırları index değerine, sütunları sütun adına göre seçer.
- **Boolean filtering:** Koşulu `True` olan satırları getirir.
- **`&`:** İki koşulun da doğru olmasını ister.
- **`|`:** Koşullardan en az birinin doğru olmasını yeterli görür.
- **Filtre + sütun seçimi:** Koşula uyan satırlardan sadece ihtiyaç duyulan sütunları almak için `loc` pratik ve okunaklıdır.

## Gün Sonu Kazanımları

Bu günün sonunda DataFrame içinde sütun seçme, `loc` ve `iloc` kullanma, tekli ve çoklu koşullarla filtreleme yapma pratik edildi.

En önemli pratik kazanım: Pandas'ta satır filtresi ve sütun seçimi birlikte kullanılabilir. Bu sayede hem koşula uyan kayıtları bulabilir hem de sonuçta sadece gereken sütunları gösterebilirsin.
