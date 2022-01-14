# class

class Person:
    
    # class attributes
    address = "no information"
    # constructer (yapıcı method)
    def __init__(self, name, year):
            # object attributes
            self.name = name
            self.year = year
            print("init metodu çalıştı")

            # methods

# object (instance)
p1 = Person(name ="Ahmet",year="1994")
p2 = Person(name="Sevil",year="1992")
# updating
p1.name = "Alp"
p2.name = "Sena"
p1.address = "Ankara"

# accessing object
print(f"p1 : name : {p1.name} year : {p1.year} address : {p1.address} ")
print(f"p2 : name : {p2.name} year : {p2.year} ")

print(p1)
print(p2)
print(type(p2))
print(type(p1))
