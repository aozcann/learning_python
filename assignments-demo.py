x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

#1- kullanıcıdan aldıgınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
# firstNumber = int(input("İlk sayıyı giriniz ="))
# secondNumber = int(input("İkinci sayıyı giriniz ="))
# multiplication = firstNumber*secondNumber
# print("Girdiğiniz sayıların çarpımı = ",multiplication)
# difa = multiplication - (x+y+z)
# print("Girilenlerin x+y+z den farkı = ",difa)

#2- y' nin x' e kalansız bölümünü hesaplayın.
# a = y//x 
# print(a)
#3-(x,y,z) toplamının mod 3'ü nedir
# sum = x+y+z
# mod3 = sum%3
# print(sum)
# print(mod3)
#4-y' nin x. kuvvetini hesaplayın
# y **= x
# print(y)
#5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır?
# x, *y, z = numbers
# z = z**3
# print(z)
#6- x, *y, z = numbers işlemine göre y'nin değerlerinin toplamı kaçtır?
x, *y, z = numbers 
y = y[1]+y[2]+y[0]
print(y)