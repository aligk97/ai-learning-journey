"""Day 37 - PyTorch Tensors & Basics

From NumPy arrays to PyTorch tensors, automatic differentiation, and
one simple manual gradient-descent training loop.
"""

import numpy as np
import torch


# 1) TENSORS: scalar (0D), vector (1D), matrix (2D)
scalar = torch.tensor(5.0)
vector = torch.tensor([1.0, 2.0, 3.0])
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

print("=== Tensor basics ===")
print("Scalar:", scalar, "shape:", scalar.shape)
print("Vector:", vector, "shape:", vector.shape)
print("Matrix:\n", matrix)
print("Matrix shape:", matrix.shape)
print("dtype:", matrix.dtype, "device:", matrix.device)
print("Matrix + 10:\n", matrix + 10)
print("Matrix * 2:\n", matrix * 2)

# Matrix multiplication: (2, 2) @ (2, 1) -> (2, 1)
weights = torch.tensor([[0.1], [0.2]])
result = matrix @ weights
print("Matrix multiplication:\n", result)
print("Result shape:", result.shape)


# 2) AUTOGRAD: derivative of the output with respect to the weight
x = torch.tensor(3.0)  # Fixed input (we do not train x)
w = torch.tensor(2.0, requires_grad=True)  # Trainable weight

y = w * x
y.backward()  # Computes dy/dw = x = 3

print("\n=== Autograd: output gradient ===")
print("y:", y.item())
print("dy/dw:", w.grad.item())


# 3) LOSS GRADIENT: derivative of the error with respect to the weight
w = torch.tensor(2.0, requires_grad=True)  # Fresh weight with no old gradient
target = torch.tensor(9.0)
prediction = w * x  # 2 * 3 = 6
loss = (prediction - target) ** 2  # (6 - 9)^2 = 9
loss.backward()  # dL/dw = 2 * (prediction - target) * x = -18

print("\n=== Autograd: loss gradient ===")
print("Prediction:", prediction.item())
print("Loss:", loss.item())
print("dLoss/dw:", w.grad.item())


# 4) MANUAL GRADIENT DESCENT: three training steps
w = torch.tensor(2.0, requires_grad=True)
learning_rate = 0.1

print("\n=== Three training epochs ===")
for epoch in range(3):
    # PyTorch accumulates gradients, so clear the previous step's value.
    # On the first step w.grad is None because backward() has not run yet.
    if w.grad is not None:
        w.grad.zero_()

    # Forward: compute a new prediction and loss from the current weight.
    prediction = w * x
    loss = (prediction - target) ** 2

    # Backward: calculate dLoss/dw and store it in w.grad.
    loss.backward()

    print(
        f"Epoch {epoch + 1}: weight={w.item():.2f}, "
        f"prediction={prediction.item():.2f}, "
        f"loss={loss.item():.2f}, gradient={w.grad.item():.2f}"
    )

    # Update the weight without recording the update in the gradient graph.
    with torch.no_grad():
        w -= learning_rate * w.grad

# Calculate the loss again to see the effect of the final weight update.
with torch.no_grad():
    final_prediction = w * x
    final_loss = (final_prediction - target) ** 2
print(f"After training: weight={w.item():.3f}, loss={final_loss.item():.3f}")


# 5) DEVICE: CUDA for supported NVIDIA GPUs, MPS for supported Apple GPUs
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print("\n=== Device ===")
print("Available device:", device)
moved_tensor = vector.to(device)
print("Tensor device after .to(device):", moved_tensor.device)


# 6) NUMPY <-> PYTORCH
array = np.array([1, 2, 3])
tensor_from_numpy = torch.tensor(array)  # Creates a copy
array_from_tensor = tensor_from_numpy.detach().cpu().numpy()

print("\n=== NumPy conversions ===")
print("NumPy -> Tensor:", tensor_from_numpy)
print("Tensor -> NumPy:", array_from_tensor)
