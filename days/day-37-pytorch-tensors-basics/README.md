# Day 37 — PyTorch Tensors & Basics

## Goal
Use PyTorch tensors, understand automatic differentiation (autograd), and connect the NumPy backpropagation work from Days 35–36 to a simple PyTorch training step.

## Files
- `main.py` — runnable examples with line-by-line comments.

## Setup
Install both dependencies in the same Python environment selected in VS Code:

```bash
python -m pip install torch numpy
python days/day-37-pytorch-tensors-basics/main.py
```

If Pylance shows `Import "torch" could not be resolved`, verify that VS Code's **Python: Select Interpreter** points to the environment where PyTorch was installed. For CUDA or Apple Silicon acceleration, see the official installation instructions: https://pytorch.org/get-started/locally/

## 1. Tensors
A tensor is a multidimensional collection of numbers, similar to a NumPy array.

| Example | Meaning | Shape |
| --- | --- | --- |
| `torch.tensor(5.0)` | scalar / 0D | `()` |
| `torch.tensor([1., 2., 3.])` | vector / 1D | `(3,)` |
| `torch.tensor([[1., 2.], [3., 4.]])` | matrix / 2D | `(2, 2)` |

- `.shape`: tensor dimensions.
- `.dtype`: element data type (e.g., `torch.float32`).
- `.device`: where the tensor is stored (e.g., CPU or GPU).
- `+` and `*`: element-wise operations in these examples.
- `@` or `torch.matmul()`: matrix multiplication.

Example: a `(2, 2)` tensor multiplied by a `(2, 1)` tensor results in `(2, 1)`.

## 2. Automatic differentiation (autograd)
A tensor with `requires_grad=True` allows PyTorch to record operations needed to compute derivatives.

```python
x = torch.tensor(3.0)
w = torch.tensor(2.0, requires_grad=True)
y = w * x
y.backward()
print(w.grad.item())  # 3.0
```

Why `3`? For `y = wx`, the derivative with respect to the weight is `dy/dw = x = 3`.

**Important distinction:**
- `y.backward()` gives `dy/dw`: how the **output** changes as the weight changes.
- `loss.backward()` gives `dLoss/dw`: how the **error** changes as the weight changes.

We train by minimizing the loss, not by blindly increasing the output.

## 3. Loss gradient
Let:
- Input `x = 3`
- Weight `w = 2`
- Target `target = 9`
- Prediction `wx = 6`

Squared error is `L = (wx - target)^2 = (6 - 9)^2 = 9`.

Using the chain rule:

```text
dL/dw = 2(wx - target) * x
      = 2(6 - 9) * 3
      = -18
```

Calling `loss.backward()` stores this gradient in `w.grad`. The `backward()` method computes gradients; it **does not change weights** by itself.

## 4. A manual Gradient Descent update
With learning rate `0.1`:

```text
w_new = w_old - learning_rate * gradient
      = 2 - 0.1 * (-18)
      = 3.8
```

The new prediction is `3.8 * 3 = 11.4`, and the new squared error is `5.76`, compared with the previous `9`.

Two essential PyTorch details:

**`with torch.no_grad():`**

Temporarily disables recording operations for autograd. We use it while applying a manual weight update so that update is not recorded as another differentiable operation.

```python
with torch.no_grad():
    w -= learning_rate * w.grad
```

After leaving the block, autograd tracking is available again, and `w.requires_grad` is still `True`.

**`w.grad.zero_()`**

PyTorch **accumulates** gradients by default. Without clearing them, a later `backward()` would add the new gradient to the old one.

```python
if w.grad is not None:
    w.grad.zero_()
```

This resets **the stored gradient**, not the weight. The `_` suffix signals an in-place operation. On the first pass, `w.grad` can be `None`.

## 5. Mini training loop
Our loop repeats these steps three times:

1. Clear the previous gradient.
2. Forward: predict using the current weight.
3. Calculate squared-error loss.
4. Backward: calculate `dLoss/dw`.
5. Update the weight inside `torch.no_grad()`.

| Epoch | Weight before update | Loss | Gradient |
| --- | ---: | ---: | ---: |
| 1 | 2.00 | 9.00 | -18.00 |
| 2 | 3.80 | 5.76 | 14.40 |
| 3 | 2.36 | 3.69 | -11.52 |

After the third update, the weight is about `3.512` and loss is about `2.359`.

Note: This is a **manual** training loop. Day 38 introduces data loading, batches, epochs, and optimizers.

## 6. CPU, CUDA, and MPS
- `torch.cuda.is_available()` checks for usable NVIDIA CUDA acceleration.
- `torch.backends.mps.is_available()` checks for usable Apple Metal acceleration.
- Otherwise, computations can run on CPU.
- `.to(device)` moves a tensor to the selected device.

## 7. NumPy ↔ PyTorch
```python
array = np.array([1, 2, 3])
tensor = torch.tensor(array)               # NumPy -> PyTorch (copy)
array_back = tensor.detach().cpu().numpy() # PyTorch -> NumPy
```

- `.detach()` disconnects a tensor from the recorded computation graph.
- `.cpu()` moves it to the CPU, as NumPy arrays do not reside on a CUDA/MPS GPU.
- `.numpy()` converts the CPU tensor to a NumPy array.

## Day-end summary
Today we learned tensor shapes, data types, element-wise math, matrix multiplication, autograd, the difference between output and loss gradients, why weight updates use `no_grad`, why gradients must be cleared, device placement, and NumPy conversion.

**Next: Day 38 — Dataset, DataLoader, Batch, Epoch & Optimizer.**
