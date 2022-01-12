# # class
# class Person: 
#     # class attributes
#     address = "no information"

#     # constructer (yapıcı method)
#     def __init__(self, name, year):
    
#             # object attributes
#             self.name = name
#             self.year = int(year)

#     # instance methods
#     def intro(self):
#         print("Hello There. I am " + self.name)

#     # instance methods
#     def calculateAge(self):
#         return 2021 - self.year

# # object (instance)
# p1 = Person(name ="Ahmet",year="1994")
# p2 = Person(name="Sevil",year="1992")

# p1.intro()
# p2.intro()

# print(f"adım: {p1.name}yaşım: {p1.calculateAge()}")


class circle:
    #class object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    # Methods

    def cevre_hesaplama(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * self.yaricap**2

c1 = circle(5)

print(f"Yarıçapı {c1.yaricap} olan dairenin çevresi: {c1.cevre_hesaplama()} ")
print(f"Yarıçapı {c1.yaricap} olan dairenin alanı: {c1.alan_hesapla()} ")
