import torch

x = torch.tensor([1.0, 2.0, 3.0, 4.0])
y = torch.tensor([2.0, 4.0, 6.0, 8.0])

weight = torch.tensor([1.0], requires_grad=True)

for epoch in range(20):
    prediction = x * weight

    loss = ((prediction - y) ** 2).mean()

    loss.backward()

    with torch.no_grad():
        weight -= 0.1 * weight.grad

    weight.grad.zero_()

    print(
        f"Step {epoch+1}: Weight={weight.item():.4f}, Error={loss.item():.4f}"
    )

print("\nFinal learned pattern:")
print(f"Output = Input × {weight.item():.4f}")