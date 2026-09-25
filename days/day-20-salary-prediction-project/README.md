# Day 20 - Salary Prediction Project

## Konular

- End-to-end regression project
- Train/test split
- OneHotEncoder
- StandardScaler
- LinearRegression
- MAE, MSE, RMSE ve R2
- Gercek degerlerle tahminleri karsilastirma

## Proje

Bu gunde kucuk bir calisan maas tahmini projesi tamamlandi.

Kullanilan feature'lar:

- `city`
- `department`
- `experience`
- `projects`
- `weekly_hours`

Target:

- `salary`

## Preprocessing

Kategorik feature'lar:

```text
city
department
```

Bu sutunlar `OneHotEncoder` ile sayisal hale getirildi.

Sayisal feature'lar:

```text
experience
projects
weekly_hours
```

Bu sutunlar `StandardScaler` ile olceklendirildi.

Train/test ayriminda temel kural korundu:

```text
Train -> fit_transform
Test  -> transform
```

Bu sayede test verisinden bilgi sizmasi engellendi.

## Model

Model olarak `LinearRegression` kullanildi.

Model sadece hazirlanan `X_train_ready` verisiyle egitildi ve tahminler `X_test_ready` uzerinden yapildi.

## Degerlendirme

Projede su regression metrikleri hesaplandi:

- MAE
- MSE
- RMSE
- R2

Gercek maaslar ve tahmin edilen maaslar grafik uzerinde karsilastirildi.

## Gun Sonu Ozeti

Day 20 sonunda onceki gunlerde ogrenilen regression, encoding, scaling, train/test split ve evaluation konulari tek bir mini projede birlestirildi.

En onemli kural:

```text
Preprocessing train verisinde ogrenilir, test verisinde sadece uygulanir.
```
