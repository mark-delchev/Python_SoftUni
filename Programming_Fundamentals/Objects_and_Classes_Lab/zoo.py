class Zoo:
    __animals = 0

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "bird":
            self.birds.append(name)
        else:
            self.fishes.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name_zoo}: {', '.join(self.mammals)}\n"
        elif species == "bird":
            result += f"Birds in {self.name_zoo}: {', '.join(self.birds)}\n"
        else:
            result += f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo_instance = Zoo(zoo_name)
n = int(input())
for i in range(n):
    animal = input().split(" ")
    species_ = animal[0]
    name_ = animal[1]
    zoo_instance.add_animal(species_, name_)

species_info = input()
print(zoo_instance.get_info(species_info))





