animals = input()
wolf_found = False

def Convert(string):
    li = list(string.split(", "))
    return li

animals_list = Convert(animals)

wolf_position = 0

last_position = 1

for i in range(len(animals_list)):
    if animals_list[i] == "wolf":
        wolf_position = len(animals_list) - i
        wolf_found = True
    if wolf_found:
        if wolf_position == last_position:
            print("Please go away and stop eating my sheep")
            break
        else:
            print(f"Oi! Sheep number {wolf_position - 1}! You are about to be eaten by a wolf!")
            break
