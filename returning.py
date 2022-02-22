# def usalma(number):
#     # two = usalma(2)
#     # three = usalma(3)

#     def inner(power):
#         return number**power

#     return inner

# two = usalma(2) # 2-3
# three = usalma(3) 3-4

# print(two(3))
# print(three(4))

# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return "{0} rolünün {1} sayfasına ulaşabilir".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)
#     return inner       
# user1 = yetki_sorgula("Product Edit")
# print(user1("Admin"))
# print(user1("user"))




def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    
    def bolme(*args):
        bolum = args[0]
        for i in range(1,len(args)):
            bolum /= args[i]
        return int(bolum)
        
    def cıkarma(*args):
        cıkarma = 0
        for i in args:
            cıkarma -= i
        return cıkarma

    if islem_adi=="toplama":
        return toplam
    elif islem_adi== "carpma":
        return carpma
    elif islem_adi == "bolme":
        return bolme 
    else: 
        return cıkarma


toplama = islem("toplama")
print(toplama(1,3,4,5,6,8))
carpma = islem("carpma")
print(carpma(1,4,6,8))
bolme = islem("bolme")
print(bolme(200,2,5))
cıkarma = islem("cıkarma")
print(cıkarma(20,2,5,9,3))
