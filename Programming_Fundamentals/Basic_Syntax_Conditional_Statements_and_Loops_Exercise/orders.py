n = int(input())
final_price = 0
for i in range(n):
    capsule_price = float(input())
    days = int(input())
    capsules_needed = int(input())
    capsule_final_price = capsule_price * days * capsules_needed
    final_price += capsule_final_price
    if days > 0 and capsule_price > 0 and capsules_needed > 0:
        print(f"The price for the coffee is: ${capsule_final_price:.2f}")

print(f"Total: ${final_price:.2f}")