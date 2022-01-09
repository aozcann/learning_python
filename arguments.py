# def changeName(n):
#     n = "ada"

# name = "yiğit"

# changeName(name)
# print(name)

# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara","izmir"]
# n = sehirler[:]     #slicing

# change(n)
# print(n)
# print(sehirler)
# # print(n)

def add(*params):
    print(params)
    print(params[0])
    print(params[2])
    return sum((params))

def add(*params):
    print(type(params))
    sum = 0
    for n in params:
        sum = sum + n
    return sum


print( add(10, 20, 45))
print( add(10, 20, 30))
print( add(10, 20, 30,3))
print( add(10, 20, 30,40,50,60,2))

def displayUser(**args):
    print(type(args))
    for key , value in args.items():
        print("{} is {} ".format(key,value))


displayUser(name= "Ahmet",age = 28, city = "Ankara")
displayUser(name= "ilknur",age = 33, city = "istanbul", phone = "12312412")
displayUser(name= "ibrahim",age = 33, city = "kırşehir", phone = "12312412", mail = "ibrahim@gmail.com")

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50, key1 = "Value 1", key2 = "Value 2")