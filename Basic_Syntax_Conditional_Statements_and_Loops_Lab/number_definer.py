num = float(input())
if num == 0:
    print("zero")
elif 0 < num < 1:
    print("small positive")
elif num > 1000000:
    print("large positive")
elif num < -1000000:
    print("large negative")
elif -1 < num < 0:
    print("small negative")
elif num < 0:
    print("negative")
else:
    print("positive")

num_2 = num
negative_positive = ""
large_small = ""
if num_2 > 0:
    negative_positive = "positive"
elif num_2 < 0:
    negative_positive = "negative"
if -1 < num_2 < 0 or 0 < num_2 < 1:
    large_small = "small"
elif num_2 < -1000000 or num_2 > 1000000:
    large_small = "large"
if large_small != "":
    print(large_small, negative_positive)
elif large_small == "":
    print(negative_positive)