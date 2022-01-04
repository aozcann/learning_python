names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998, 2000, 1998, 1987]

names.append("Cenk")
print(names)
names.insert(0,"Sena")
print(names)
# names.remove("Deniz")
# print(names)
result = names.index("Deniz")
print(result)
print(names.count("Ali"))
result = "Ali" in names
print(result)
result =names.index("Ali")
print(result)
names.reverse()
print(names)
print("slice = ",names[::-1])
names.sort()
print(names)
years.sort()
print(years)
str = "Chevrolet,Dacia"
X = str.split(",")
print(X)
print(X[1])
print(max(years),min(years))
print(years.count(1998))
years.clear()
print(years)

Brands = [input("İlk markayı giriniz =" )
    ,input("İkinci markayı giriniz =" )
    ,input("üçüncü markayı giriniz =" )]
print(Brands)