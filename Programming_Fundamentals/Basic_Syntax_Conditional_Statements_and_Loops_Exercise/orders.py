n = int(input())
final_price = 0
for i in range(1, n + 1):
    capsule_price = float(input())
    days = int(input())
    capsules_needed = int(input())
    if capsules_needed < 1 or capsules_needed > 2000 or \
         days < 1 or days > 31 or capsule_price < 0.01 or capsule_price > 100.00:
        continue
    else:
        capsule_final_price = capsule_price * days * capsules_needed
        final_price += capsule_final_price
        print(f"The price for the coffee is: ${capsule_final_price:.2f}")

print(f"Total: ${final_price:.2f}")