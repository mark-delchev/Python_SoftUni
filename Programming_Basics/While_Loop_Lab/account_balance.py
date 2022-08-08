balance = 0.0
while balance >= 0:
    try:
        amount = float(input())
    except ValueError:
        break
    if amount < 0:
        print("Invalid operation!")
        break
    else:
        balance += amount
        print(f"Increase: {amount:.2f}")
print(f"Total: {balance:.2f}")
