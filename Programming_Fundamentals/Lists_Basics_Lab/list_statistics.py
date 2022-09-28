
n = int(input())
positive = []
negative = []
negative_sum = 0
positive_count = 0
for i in range(n):
    num = int(input())
    if num >= 0:
        positive_count += 1
        positive.append(num)
    elif num < 0:
        negative_sum += num
        negative.append(num)
print(positive)
print(negative)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {negative_sum}")