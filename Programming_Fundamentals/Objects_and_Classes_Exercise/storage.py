class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if self.capacity > len(self.storage):
            self.storage.append(product)

    def get_products(self):
        return self.storage


storage_instance = Storage(2)
storage_instance.add_product(55)
storage_instance.add_product("banana")
storage_instance.add_product("potato")
storage_instance.add_product("tomato")
storage_instance.add_product("bread")
print(storage_instance.get_products())

