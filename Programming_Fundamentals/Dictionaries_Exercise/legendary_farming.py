materials = input().split(" ")
key_materials = ["shards", "fragments", "motes"]
junk_materials = []

dictionary = {}

for i in range(len(materials)):
    if materials[i].lower() in dictionary.keys():
        value = int(materials[i - 1])
        dictionary[materials[i].lower()] += value
        continue
    else:
        junk_materials.append(materials[i].lower())
    if materials[i].lower() in key_materials:
        key = (materials[i]).lower()
        value = int(materials[i - 1])
        dictionary[key] = value

print(dictionary)