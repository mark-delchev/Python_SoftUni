chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery_fee = 2.50

cmenus = int(input())
fmenus = int(input())
vmenus = int(input())

menus = chicken_menu * cmenus + fish_menu * fmenus + vegetarian_menu * vmenus
dessert = menus * 0.20
price = menus + dessert + delivery_fee

print(price)

