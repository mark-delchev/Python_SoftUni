def iseven(num):
    return num % 2 == 0

def even_list(str):
    lst = [int(i) for i in str.split(" ")]
    final_lst = list(filter(iseven, lst))
    return final_lst

n = input()
print(even_list(n))