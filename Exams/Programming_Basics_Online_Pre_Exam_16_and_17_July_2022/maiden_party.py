message = 0.60
rose = 7.20
keyholder = 3.60
caricature = 18.20
luck = 22.00

maiden_party_price = float(input())
message_num = int(input())
rose_num = int(input())
keyholder_num = int(input())
caricature_num = int(input())
luck_num = int(input())

sold_income = message * message_num + rose * rose_num + keyholder * keyholder_num + caricature * caricature_num + \
    luck * luck_num
sold_num = message_num + rose_num + keyholder_num + caricature_num + luck_num

if sold_num > 25:
    sold_income *= 0.65
final_income = sold_income * 0.90

if final_income >= maiden_party_price:
    print(f"Yes! {final_income - maiden_party_price:.2f} lv left.")
else:
    print(f"Not enough money! {maiden_party_price - final_income:.2f} lv needed.")
