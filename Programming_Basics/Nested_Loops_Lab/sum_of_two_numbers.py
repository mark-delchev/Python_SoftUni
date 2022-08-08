start = int(input())
end = int(input())
magic_num = int(input())
combinations = 0
num_found = False
for i in range(start, end + 1):
    for k in range(start, end + 1):
        combinations += 1
        if i + k == magic_num:
            num_found = True
            print(f"Combination N:{combinations} ({i} + {k} = {magic_num})")
            break
    if num_found:
        break
if not num_found:
    print(f"{combinations} combinations - neither equals {magic_num}")

