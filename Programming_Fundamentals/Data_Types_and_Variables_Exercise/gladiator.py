
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_trashed = 0
swords_trashed = 0
shields_trashed = 0
armor_trashed = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        helmets_trashed += 1
    if fight % 3 == 0:
        swords_trashed += 1
    if fight % 2 == 0 and fight % 3 == 0:
        shields_trashed += 1
        if shields_trashed % 2 == 0:
            armor_trashed += 1

expenses = helmets_trashed * helmet_price + \
     swords_trashed * sword_price + shields_trashed * shield_price +  \
        armor_trashed * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")



