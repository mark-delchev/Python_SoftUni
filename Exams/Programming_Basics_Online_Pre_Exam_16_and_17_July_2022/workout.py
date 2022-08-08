import math
training_days = int(input())
km_ran = float(input())
km_ran_total = 0
km_ran_new = km_ran
for i in range(training_days):
    percentage_increase = int(input())
    real_percentage = percentage_increase / 100
    km_ran_new += km_ran_new * real_percentage
    km_ran_total += km_ran_new
km_ran_final = km_ran_total + km_ran
if km_ran_final >= 1000:
    print(f"You've done a great job running {math.ceil(km_ran_final - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - km_ran_final)} more kilometers")


