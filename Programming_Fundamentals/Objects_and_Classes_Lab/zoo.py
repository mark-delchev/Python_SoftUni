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


