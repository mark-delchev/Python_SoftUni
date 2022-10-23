exp_needed = float(input())
battles = int(input())
battle_counter = 0
exp_earned_total = 0
for i in range(battles):
    battle_counter += 1
    exp_earned = float(input())
    if battle_counter % 3 == 0:
        exp_earned *= 1.15
    if battle_counter % 5 == 0:
        exp_earned *= 0.90
    if battle_counter % 15 == 0:
        exp_earned *= 1.05
    exp_earned_total += exp_earned
    if exp_earned_total >= exp_needed:
        print(f"Player successfully collected his needed experience for {battle_counter} battles.")
        break
else:
    print(f"Player was not able to collect the needed experience, {(exp_needed - exp_earned_total):.2f} more needed.")