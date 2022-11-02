nums = input().split(", ")
int_nums = [int(i) for i in nums]
even_nums = [i for i in int_nums if i % 2 == 0]
odd_nums = [i for i in int_nums if i % 2 != 0]
negative = [i for i in int_nums if i < 0]
positive = [i for i in int_nums if i >= 0]



p_nums = ", ".join([str(i) for i in positive])
n_nums = ", ".join([str(i) for i in negative])
e_nums = ", ".join([str(i) for i in even_nums])
o_nums = ", ".join([str(i) for i in odd_nums])

print(f"Positive: {p_nums}")
print(f"Negative: {n_nums}")
print(f"Even: {e_nums}")
print(f"Odd: {o_nums}")