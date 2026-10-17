import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

# Day 38: Dataset, DataLoader, batches, epochs, and an optimizer.
# This is a simple linear model, not yet a multilayer neural network.
torch.manual_seed(42)

# 1) Input (X) and target (y): the underlying rule is y = 2*x + 1.
X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]])
y = torch.tensor([[3.0], [5.0], [7.0], [9.0], [11.0], [13.0]])

# 2) Pair examples and provide them two at a time in shuffled batches.
dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=2, shuffle=True)

# 3) nn.Linear(1, 1) learns one weight and one bias.
model = nn.Linear(in_features=1, out_features=1)

# 4) Mean squared error measures how wrong our predictions are.
loss_fn = nn.MSELoss()

# 5) SGD will update ALL learnable model parameters for us.
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

epochs = 300
for epoch in range(epochs):
    model.train()  # Set training mode (important for some layer types).

    # There are 6 rows and batch_size=2: 3 batches per epoch.
    for batch_X, batch_y in loader:
        optimizer.zero_grad()              # Clear old accumulated gradients.
        predictions = model(batch_X)       # Forward: make predictions.
        loss = loss_fn(predictions, batch_y)  # Calculate batch MSE.
        loss.backward()                    # Autograd: compute gradients.
        optimizer.step()                   # SGD: update weight and bias.

    # Evaluate the full TRAINING dataset every 50 epochs.
    # Important: this is not a true test score on unseen data.
    if (epoch + 1) % 50 == 0:
        model.eval()
        with torch.no_grad():
            train_loss = loss_fn(model(X), y)
        print(f"Epoch {epoch + 1:>3}/{epochs} | Training MSE: {train_loss.item():.6f}")

# 6) Inference: no backward pass, no weight updates.
model.eval()
with torch.no_grad():
    weight = model.weight.item()
    bias = model.bias.item()
    prediction_for_7 = model(torch.tensor([[7.0]])).item()

print(f"Learned weight: {weight:.4f} (target: 2)")
print(f"Learned bias: {bias:.4f} (target: 1)")
print(f"Prediction for x=7: {prediction_for_7:.4f} (target: 15)")
