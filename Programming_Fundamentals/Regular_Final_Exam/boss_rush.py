n = int(input())

for i in range(n):
    boss_name_bool = False
    titles_bool = False
    Error = False
    try:
        boss_title = input().split(":")
        boss = boss_title[0]
        title = boss_title[1]
        boss_name = boss[1:-1]
        titles = title.split(" ")
        title_1 = titles[0]
        title_2 = titles[1]
        title_1 = title_1.replace("#", "")
        title_2 = title_2.replace("#", "")
    except NameError:
        Error = True
    except IndexError:
        Error = True

    if not Error:
        if boss_name.isupper() and len(boss_name) >= 4 and boss[0] == "|" and boss[-1] == "|":
            boss_name_bool = True
        if len(titles) == 2 and title_1.isalpha() and title_2.isalpha():
            titles_bool = True

    if boss_name_bool and titles_bool and not Error:
        print(f"{boss_name}, The {title_1} {title_2}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title_1) + len(title_2) + 1}")
    else:
        print("Access denied!")

