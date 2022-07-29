budget = float(input())
GPU = int(input())
CPU = int(input())
RAM = int(input())

GPU_price = 250 * GPU
CPU_price = (GPU_price * 0.35) * CPU
RAM_price = (GPU_price * 0.10) * RAM

final_price = GPU_price + CPU_price + RAM_price
if GPU > CPU:
    final_price = final_price * 0.85
    if budget >= final_price:
        print(f'You have {budget-final_price} leva left!')
    else:
        print(f'Not enough money! You need {final_price-budget:.2f} leva more!')
else:
    if budget >= final_price:
        print(f'You have {budget-final_price:.2f} leva left!')
    else:
        print(f'Not enough money! You need {final_price-budget:.2f} leva more!')


