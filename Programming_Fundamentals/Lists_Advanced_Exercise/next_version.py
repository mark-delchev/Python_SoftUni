
start_version = input()
nums = start_version.split(".")
value_found = False
twice = False
for i in range(1, 10):
    if twice:
        break
    for j in range(0, 10):
        if twice:
            break
        for k in range(0, 10):
            if value_found:
                twice = True
                if [str(i), str(j), str(k)] != nums:
                    print(f"{i}.{j}.{k}")
                break
            if [str(i), str(j), str(k)] == nums:
                value_found = True
