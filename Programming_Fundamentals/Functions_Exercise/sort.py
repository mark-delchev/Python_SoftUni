def sort_list(str):
    lst = [int(i) for i in str.split(" ")]
    final_lst = sorted(lst)
    return final_lst

num = input()
print(sort_list(num))
