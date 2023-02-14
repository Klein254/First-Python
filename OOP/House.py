class House():
    def __init__(self, type, location, owner):
        self.type = type
        self.location = location
        self.owner = owner


owner_one = House("Bungalow", "Kitengela", "Sharon")
print(owner_one.type)
print(owner_one.location)
print(owner_one.owner)

print("<--------end of owner one--------->")

owner_two = House("Penthouse", "Kilimani", "David")
print(owner_two.location)
print(owner_two.owner)
print(owner_two.type)