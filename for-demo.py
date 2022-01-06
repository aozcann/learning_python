sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesindeki hangi sayılar 3'ün katıdır.
# 2- sayilar lisetesindeki sayıların toplamı kaçtır.
# 3- sayilar lisestesindeki sayıların karelerini yazınız.

# for sayi in sayilar:
#     if (sayi%3==0):
#         print(sayi)

# toplam = 0
# for sayi in sayilar:
#     toplam = toplam + sayi
# print("toplam:",toplam)

# for sayi in sayilar:
#     if ( sayi%2 == 1):
#         print(sayi**2) 

# 4- şehirlerden hangileri en fazla 5 karakterlidir?

# sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# for sehir in sehirler:
#     if (len(sehir) <= 5):
#         print(sehir)

# 5- Ürünlerin fiyatları toplamı kaçtır.
urunler = [
    {"name":"samsung S6","price" : "3000"},
    {"name":"samsung S7","price" : "4000"},
    {"name":"samsung S8","price" : "5000"},
    {"name":"samsung S9","price" : "6000"},
    {"name":"samsung S10","price" : "7000"},
]

# sumPrice = 0
# for urun in urunler:
#     fiyat = int(urun["price"])
#     sumPrice += fiyat
# print("Toplam:",sumPrice)

#6-ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

for urun in urunler:
    if int(urun["price"]) <= 5000:
        print(urun["name"])
