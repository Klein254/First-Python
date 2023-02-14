class Car:
    def __init__(self, Make, Brand, owner, color):
        self.Make = Make
        self.Brand = Brand
        self.owner = owner
        self.color = color


owner_one = Car("Toyota", "Land Cruiser", "Sharon", "Black")
print(owner_one.Make)
print(owner_one.Brand)
print(owner_one.owner)
print(owner_one.color)

print("<--------end of owner one--------->")

owner_two = Car("Audi", "R8", "David", "White")
print(owner_two.Make)
print(owner_two.Brand)
print(owner_two.owner)
print(owner_two.color)

print("<--------end of owner two--------->")

owner_three = Car("BMW", "M30I", "Lewis", "Grey")
print(owner_three.Make)
print(owner_three.Brand)
print(owner_three.owner)
print(owner_three.color)

print("<--------end of owner three--------->")

owner_four = Car("Mercedes Benz", "AMG G63", "Ray", "Matte Black")
print(owner_four.Make)
print(owner_four.Brand)
print(owner_four.owner)
print(owner_four.color)

print("<--------end of owner four--------->")