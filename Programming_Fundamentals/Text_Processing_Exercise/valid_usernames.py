
passwords = input().split(", ")
num_range = range(48, 57)
letters_range = range(97, 122)
capital_letters_range = range(65, 90)
valid_pass = []
for password in passwords:
    for char in password:
        if ord(char) == 95 or ord(char) == 45 or ord(char) in num_range or \
                ord(char) in letters_range or ord(char) in capital_letters_range:
            pass
        else:
            break
    else:
        if 3 <= len(password) <= 16:
            valid_pass.append(password)

for pas in valid_pass:
    print(pas)





