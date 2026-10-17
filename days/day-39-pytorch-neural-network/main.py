"""Day 39: PyTorch ile ilk cok katmanli Neural Network egitimi."""

import torch
import torch.nn as nn

# Deneyin tekrarlanabilmesi icin baslangic rassalligini sabitliyoruz.
torch.manual_seed(42)

# Her satirda iki giris ozelligi bulunuyor: x1 ve x2.
X = torch.tensor(
    [
        [0, 0], [1, 0], [0, 1],
        [1, 1], [2, 0], [0, 2],
        [2, 1], [1, 2], [3, 1],
        [1, 3], [3, 3], [4, 2],
    ],
    dtype=torch.float32,
)

# Sadece egitim verisini uretmek icin bildigimiz hedef kural:
# y = 2*x1 + 3*x2 + 1
# 0:1 ve 1:2 dilimleri, hedefin [12, 1] boyutunu korur.
y = 2 * X[:, 0:1] + 3 * X[:, 1:2] + 1


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(2, 4)
        self.relu = nn.ReLU()
        self.output = nn.Linear(4, 1)

    def forward(self, x):
        x = self.hidden(x)
        x = self.relu(x)
        x = self.output(x)
        return x


model = NeuralNetwork()

# Her katmandaki agirlik ve bias tensorlerinin boyutlarini yazdir.
print('--- Parametreler ---')
for name, param in model.named_parameters():
    print(f'{name}: shape={tuple(param.shape)}, eleman={param.numel()}')

total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print('Toplam ogrenilebilir parametre:', total_params)

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
X_new = torch.tensor([[2.0, 3.0]])

# Model daha egitilmedi; agin ilk tahminine bakalim.
model.eval()
with torch.no_grad():
    print('Egitim oncesi tahmin:', model(X_new).item())

# Egitim sureci
model.train()
for epoch in range(1000):
    prediction = model(X)           # Forward propagation
    loss = criterion(prediction, y) # Kayip
    optimizer.zero_grad()           # Onceki gradientleri sifirla
    loss.backward()                 # Yeni gradientleri hesapla
    optimizer.step()                # Parametreleri guncelle

    if (epoch + 1) % 200 == 0:
        print(f'Epoch {epoch + 1:4d} | Loss: {loss.item():.6f}')

# Inference: eval() ile mod degisir, no_grad() ile gradient takibi durur.
model.eval()
with torch.no_grad():
    result = model(X_new)

print('Egitim sonrasi tahmin:', result.item())
print('Beklenen hedef:', 14.0)
