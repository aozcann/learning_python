sayilar = [1,3,5,7,9,12,19,21]

# # 1: sayilar listesini while ile ekrana yazdıralım.
# x = 0
# while x < len(sayilar) :
#     print(sayilar[x])
#     x += 1

#2 : Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

# start = int(input("başlangıç değeri girin:"))
# finish = int(input("bitiş değeri girin:"))


# while (start < finish) :
#     if (sayilar[start] % 2 == 1) :
#         print(sayilar[start])
#     start += 1

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

# x=100
# while  0 < x  :
#     x -= 1
#     print(x)

# 4: Kullanıdan aldığınız 5 sayıyı ekrana sıralı yazdırınız.

# numbers = []
# i = 0
# x = ""
# while i<5 :
#     sayi = int(input(f"{i+1}.ci sayıyı girin: "))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print(numbers)

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler lisetsine saklayınız.
#       ** ürün sayısını kullanıcıya sorun
#       ** dictionary listesi yapısı(name, price) şeklinde olsun.
#       ** ürün ekleme işlemi bittiğinde ürünleri ekranda while dögüsüyle yazdırın.

urunler = []

urunCount = int(input("Kaç adet ürün gireceksiniz: "))
i = 0

while (i<urunCount):
    name = input("ürün ismi :")
    price = int(input("ürün fiyatı :"))
    urunler.append({
        "name" : name ,
        "price" : price 
    })
    i += 1

for urun in urunler:
    print(f"ürün adı : {urun['name']} , ürün fiyatı : {urun['price']} ")
