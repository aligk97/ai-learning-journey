# Day 38 — PyTorch: Dataset, DataLoader, Batch, Epoch & Optimizer

## Goal
Understand a complete PyTorch training loop: how to load examples in batches, predict, compute loss, calculate gradients, update parameters, and evaluate the result.

## Files and setup
- `main.py` — runnable, commented training example.
- Install: `python -m pip install torch`
- Run from the repo root: `python days/day-38-pytorch-training-loop/main.py`

## 1. Dataset and DataLoader
- `TensorDataset(X, y)` pairs each input row with its label or target.
- `DataLoader(dataset, batch_size=2, shuffle=True)` yields pairs of two rows per batch and shuffles row order each epoch.
- The six-row dataset creates **three batches per epoch**.
- An **epoch** means the entire training dataset is processed once; a **batch** is one group processed within an epoch.
- With 300 epochs and 3 batches each, we perform **900 optimizer steps**.

## 2. Model, loss and optimizer
The synthetic data follows `y = 2*x + 1`. We do not give the model this equation; it learns the weight and bias.

```python
model = nn.Linear(1, 1)                    # y_hat = w*x + b
loss_fn = nn.MSELoss()                    # Mean squared error
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

- `nn.Linear(1, 1)`: one input feature and one output.
- `model.parameters()`: the model's learnable parameters (weight and bias).
- `torch.optim.SGD`: Stochastic Gradient Descent optimizer.
- `lr=0.01`: learning rate, the scale of each gradient-based update.

## 3. Training loop
```python
for epoch in range(300):
    model.train()
    for batch_X, batch_y in loader:
        optimizer.zero_grad()                 # Clear gradients from previous batch
        predictions = model(batch_X)          # Forward
        loss = loss_fn(predictions, batch_y)   # Loss
        loss.backward()                       # Compute dLoss/d(weight,bias)
        optimizer.step()                      # Update the parameters
```

**Order matters:**
1. Clear accumulated gradients with `optimizer.zero_grad()`.
2. Predict using current parameters.
3. Calculate the batch loss.
4. Use `loss.backward()` to compute gradients (it does **not** update weights).
5. Use `optimizer.step()` to update weights using those gradients.

This replaces manual updates such as `w -= lr * w.grad` and `b -= lr * b.grad`.

## 4. Training versus evaluation
- `model.train()` sets training mode. This affects certain layers, such as Dropout and BatchNorm.
- `model.eval()` sets evaluation mode. It does **not** itself disable autograd.
- `with torch.no_grad():` disables gradient recording during reporting or inference.
- During evaluation we do **not** call `loss.backward()` or `optimizer.step()`.

The lesson prints loss on **the training set**. To estimate generalization, train on a training split and evaluate on a separate validation or test split (as in Day 13). Do not train on the test set.

## 5. Expected result
With the fixed seed and CPU setup used for the example, results can be near:
- Weight `~2`, bias `~1`
- Prediction for `x=7`: `~15`
- Training MSE should become small.

Exact numbers may vary with environment, implementation, or randomness.

## 6. Key distinctions
| Concept | What it does |
| --- | --- |
| `Dataset` | Pairs individual X and y samples |
| `DataLoader` | Iterates over batches |
| Batch | Subset of data used in one gradient update |
| Epoch | One pass through all training rows |
| `loss.backward()` | Computes gradients |
| `optimizer.step()` | Updates parameters |
| `optimizer.zero_grad()` | Clears accumulated gradients |
| `model.eval()` | Switches layer behavior to evaluation |
| `torch.no_grad()` | Disables gradient recording |

## Day-end summary
Created a full PyTorch training loop with batched data, MSE loss, SGD and automatic differentiation. Learned how training and evaluation differ and why training loss alone cannot establish generalization.

**Next: Day 39 — First Neural Network with PyTorch.**
