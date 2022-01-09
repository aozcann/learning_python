# 1- Gönderilen bir kelimeyi belirtilen kez erkanda gösteren foksiyon yazın.
# 2- kendine gönderline sınırsız sayıdaki parametreyi listeye dönüştüren bir fonsiyon yazın.
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.

# 1. question
# def show(word, number):
#     for i in range(number):
#         print(word)    
# word = input("Bir kelime giriniz :")
# number = int(input("Kelme kaç kez ekranda yazılsın :"))

#        or [Alternative]
# def write(word,count):
#     print(word * count)

# write("Hi \n", 10)
# show(word , number)

# 2. question
# list = []
# def unlimited(**params):
#     for key, value in params.items():
#         list.append("{} is {}  ".format(key,value))

# unlimited(name= "ibrahim",age = 33, city = "kırşehir", phone = "12312412", mail = "ibrahim@gmail.com")
# unlimited(name= "ahmet",age = 31, city = "yozgat", phone = "12312412", mail = "ahmet@gmail.com", sport = "Hockey")
# unlimited(name= "sevil",age = 30, city = "çorum", phone = "12312412", mail = "sevil@gmail.com", adress = "yaşamkent")

# print(list)
# or Alternative

# def changetoList(*params):
#     list = []

#     for param in params:
#         list.append(param)

#     return list

# result = changetoList(10,20,30,40,50 ,"Hello")

# print(result)

# third question


# def primeFinder(number1,number2):
#     for number in range(number1, number2+1):
#         if number > 1:
#             for i in range(2,number):
#                 if number % 2 == 0:
#                     break
#             else:
#                 print(number)

# number1 = int(input("Sayi1 :"))
# number2 = int(input("Sayi2 :"))

# primeFinder(number1,number2)

# or Alternative

# def primeNumber (sayi,sayi2):
#     asallar = []
#     for i in range(sayi, sayi2+1):
#         if i >1:
#             asalmi = True
#             for j in range(2, i):
#                 if (i % j == 0):
#                     asalmi = False
#                     break
#             if asalmi:
#                 asallar.append(i)
#     print(asallar)
# sayi = int(input("Aralık için ilk sayıyı girin :"))
# sayi2 = int(input("Aralık için ikinci sayıyı girin :"))
# primeNumber(sayi,sayi2)

# Fourth question
number = int(input("Number :"))
list = []
def selfDivision(number):
    for i in range(number+1):
        if i > 0 :
            if (number % i == 0):
                list.append(i)
    print(list)

selfDivision(number)