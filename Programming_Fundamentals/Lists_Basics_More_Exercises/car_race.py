racer_times = input().split(" ")
finish_line = len(racer_times) // 2 + 1
racer_one = racer_times[:finish_line - 1]
racer_two = racer_times[finish_line:][::-1]
racer_one_sum = 0
racer_two_sum = 0

for i in racer_one:
    racer_one_sum += int(i)
    if int(i) == 0:
        racer_one_sum *= 0.8

for i in racer_two:
    racer_two_sum += int(i)
    if int(i) == 0:
        racer_two_sum *= 0.8

if racer_one_sum < racer_two_sum:
    print(f"The winner is left with total time: {racer_one_sum:.1f}")
else:
    print(f"The winner is right with total time: {racer_two_sum:.1f}")

