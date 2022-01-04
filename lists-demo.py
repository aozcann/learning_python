CarBrand = ["Bmw","Mercedes","Opel","Mazda"]
print(CarBrand)
print(len(CarBrand))
print(CarBrand[0]+" "+CarBrand[-1])
CarBrand[-1] = "Toyata"
print(CarBrand)
result = "Mercedes"in  CarBrand
print(result)
print(CarBrand[-2])
result = CarBrand[0:3]
result = CarBrand[:3]
result = CarBrand[-2:]
print(result)
CarBrand[-2:] = ["Toyata","Renault"]
print(CarBrand)
result = CarBrand + ["Audi","Nissan"]
print(result)
del CarBrand[-1]
print(CarBrand)
print(CarBrand[::-1])

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,80]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

print(studentA)
print(studentB)
print(studentC)

result = f"{studentA[0]} {studentA[1]} {2021-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result)