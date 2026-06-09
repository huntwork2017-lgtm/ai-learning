import torch
import torch.nn as nn

# Inputs:
# [consistency, sleep, protein, stress]

x = torch.tensor([
    [10.0, 9.0, 8.0, 2.0],
    [9.0, 8.0, 7.0, 3.0],
    [2.0, 8.0, 8.0, 2.0],
    [3.0, 4.0, 5.0, 8.0],
    [10.0, 10.0, 10.0, 1.0],
    [4.0, 3.0, 4.0, 9.0]
])

# 1 = Success
# 0 = Not Success

y = torch.tensor([
    [1.0],
    [1.0],
    [0.0],
    [0.0],
    [1.0],
    [0.0]
])

model = nn.Sequential(
    nn.Linear(4, 4),
    nn.ReLU(),
    nn.Linear(4, 1),
    nn.Sigmoid()
)

loss_function = nn.BCELoss()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for step in range(2000):

    prediction = model(x)

    loss = loss_function(prediction, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if step % 200 == 0:
        print(f"Step {step}: Error = {loss.item():.4f}")

print("\nPredictions:")

with torch.no_grad():
    print(model(x))