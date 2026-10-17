# Day 39 — PyTorch ile İlk Neural Network (ANN)

## Amaç

PyTorch kullanarak `nn.Module` tabanlı, gizli katman içeren bir yapay sinir ağı oluşturmak; `forward()` akışını anlamak; `MSELoss` ve `Adam` ile modeli eğitmek; eğitim/değerlendirme farkını öğrenmek.

## Mimari

```text
Input (2) → Linear(2, 4) → ReLU → Linear(4, 1) → Output (1)
```

- İlk katman: 8 ağırlık + 4 bias = **12 parametre**
- Çıkış katmanı: 4 ağırlık + 1 bias = **5 parametre**
- **Toplam: 17 öğrenilebilir parametre**

## Örnek veri

Eğitim örneklerinin hedef değerleri şu kuralla hazırlanır:

`y = 2*x1 + 3*x2 + 1`

Örneğin `(x1, x2) = (2, 3)` için doğru değer **14** olur. Bu ilişki modele doğrudan verilmez; model örnek çiftleri üzerinden öğrenmeye çalışır.

## Eğitim adımları

1. `model.train()` ile eğitim modu.
2. `prediction = model(X)` ile forward propagation.
3. `criterion(prediction, y)` ile MSE loss.
4. `optimizer.zero_grad()` ile eski gradientleri temizleme.
5. `loss.backward()` ile backpropagation.
6. `optimizer.step()` ile ağırlık ve bias güncelleme.

Öğrenme oranı `0.01`, optimizer `Adam`, epoch sayısı `1000` olarak seçilmiştir.

## `train()` / `eval()` / `no_grad()` farkı

| Komut | Görevi |
| --- | --- |
| `model.train()` | Eğitim modunu etkinleştirir. |
| `model.eval()` | Değerlendirme modunu etkinleştirir (özellikle Dropout ve BatchNorm için önemlidir). |
| `torch.no_grad()` | Gradient takibini devre dışı bırakır. |

**Not:** Bu ağda Dropout ve BatchNorm bulunmadığı için `train()` ile `eval()` tek başlarına aynı giriş için hesaplanan çıktıyı değiştirmez. `eval()` gradient takibini **kapatmaz**.

## Çalıştırma

Ön koşul: Python ve PyTorch kurulu olmalı.

```bash
python main.py
```

Komut satırında parametre şekilleri, toplam 17 parametre, eğitim öncesi tahmin, her 200 epoch'taki loss ve eğitim sonrası tahmin görülür. Tohum sabit olduğunda CPU üzerinde son tahmin yaklaşık **14.01** olur; farklı PyTorch sürümlerinde sonuç küçük farklılıklar gösterebilir.

## Öğrendiklerim

- `nn.Module` katmanları ve parametreleri nasıl yönetiyor?
- `nn.Linear(in_features, out_features)` boyutları ve ağırlık sayısı nasıl hesaplanıyor?
- `forward()` ağın hesaplama sırasını nasıl belirliyor?
- `backward()` ile `optimizer.step()` arasındaki fark nedir?
- `named_parameters()`, `numel()`, `train()`, `eval()` ve `no_grad()` ne işe yarıyor?
