ornament_set = [2, 5]
tree_skirt = [5, 3]
tree_garland = [3, 10]
tree_lights = [15, 17]
quantity = int(input())
days = int(input())
total_price = 0
total_spirit = 0
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_price += ornament_set[0] * quantity
        total_spirit += ornament_set[1]
    if day % 3 == 0:
        total_price += (tree_garland[0] + tree_skirt[0]) * quantity
        total_spirit += tree_garland[1] + tree_skirt[1]
    if day % 5 == 0:
        total_price += tree_lights[0] * quantity
        total_spirit += tree_lights[1]
    if day % 5 == 0 and day % 3 == 0:
        total_spirit += 30 
    if day % 10 == 0:
        total_spirit -= 20
        total_price += tree_garland[0] + tree_skirt[0] + tree_lights[0]
    if day % 10 == 0 and day == days:
        total_spirit -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")



