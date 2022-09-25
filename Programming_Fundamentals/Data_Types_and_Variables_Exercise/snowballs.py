n = int(input())
largest_value = 0
final_weight = 0
final_time = 0
final_quality = 0
for i in range(n):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight / time_needed) ** quality
    if value > largest_value:
        largest_value = value
        final_weight = weight
        final_time = time_needed
        final_quality = quality
print(f"{final_weight} : {final_time} = {largest_value:.0f} ({final_quality})" )
