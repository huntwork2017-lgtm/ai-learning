import torch
import torch.nn as nn

# Inputs:
# [consistency, sleep, protein]
x = torch.tensor([
    [10.0, 9.0, 8.0],   # great habits
    [9.0, 2.0, 8.0],    # consistent, bad sleep
    [2.0, 9.0, 8.0],    # not consistent
    [8.0, 8.0, 7.0],    # solid habits
])

# Outputs:
# Progress score out of 10
y = torch.tensor([
    [10.0],
    [6.0],
    [3.0],
    [8.0],
])

model = nn.Linear(3, 1)

loss_function = nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

for step in range(1000):
    prediction = model(x)

    loss = loss_function(prediction, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if step % 100 == 0:
        print(f"Step {step}: Error = {loss.item():.4f}")

print("\nFinal predictions:")
print(model(x).detach())

print("\nLearned weights:")
print(model.weight.detach())

print("\nLearned bias:")
print(model.bias.detach())