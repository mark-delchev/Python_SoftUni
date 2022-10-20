def password_check(password):
    validPass = True
    password_characters = list(ord(i) for i in password)
    password_length = len(password)
    num_counter = 0
    for i in range(password_length):
        character_num = password_characters[i]
        if validPass:
            if character_num > 122 or character_num > 90 and character_num < 97 \
                 or character_num < 65 and character_num > 57 or character_num < 48:
                print("Password must consist only of letters and digits") 
                validPass = False
        if 48 <= character_num <= 57:
            num_counter += 1
    if num_counter < 2:
        print("Password must have at least 2 digits")
        validPass = False

    if password_length < 6 or password_length > 10:
        print("Password must be between 6 and 10 characters")
        validPass = False
        
    if validPass:
        print("Password is valid")

password = input()
password_check(password)


