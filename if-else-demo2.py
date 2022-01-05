#1- Girin bir sayının 0-100 arasında olup olmadıgını kontrol edin.

# sayi = float(input("Sayıyı girin:"))

# if (sayi >= 0 ) and (sayi <= 100):
#     print(f"{sayi} sayısı 0-100 arasında yer alan pozitif bir sayıdır.")
# elif (sayi <= 0) :
#     print(f"{sayi} sayısı negatif bir sayıdır.")
# else :
#     print(f"{sayi} sayısı 100 den büyük pozitif bir sayıdır. ")

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# sayi = float(input("Sayıyı girin:"))

# if ( sayi > 0 ) and ( sayi % 2 == 0 ):
#     print(f"{sayi} sayısı pozitif bir çift sayıdır. ")
# elif ( sayi > 0 ) and ( sayi % 2 == 1 ):
#     print(f"{sayi} sayısı pozitif bir tek sayıdır. ")
# elif ( sayi < 0 ) and ( sayi % 2 == 0 ):
#     print(f"{sayi} sayısı negatif bir çift sayıdır. ")
# elif ( sayi < 0 ) and ( sayi % 2 == 1 ):
#     print(f"{sayi} sayısı negatif bir tek sayıdır. ")
# else :
#     print("0 çift bir sayıdır.")


#3- Email ve parola bilgileri ile giriş yapınız.

# email = "ozcanahmet94@gmail.com"
# password = "1234asd"

# userEmail = input("Email adresini giriniz: ")
# userPassword = input("Parola bilginizi giriniz: ")

# if email != userEmail :
#        print("Email adresi yanlış")
# elif password != userPassword :
#     print ("Parola bilgisi yanlış")
# else:
#     print ("Hoşgeldiniz".center(50,"*"))

# if email == userEmail and password == userPassword:
#     print ("Hoşgeldiniz".center(50,"*"))
# else :
#     print("Bilgileri kontrol edin.")
# My favori if:
# #  if email == userEmail :
# #     if password == userPassword:
# #         print ("Hoşgeldiniz".center(50,"*"))
# #     else :
# #         print("Bilgileri kontrol edin. Parola bilginiz yanlış.")
# # elif password == userPassword :
# #     print("Email bilgisi yanlış. ")
# # else :
# #     print ("Email ve Parola bilgisi yanlış.")

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırın. 

# a = float(input("1.sayı :"))
# b = float(input("2.sayı :"))
# c = float(input("3.sayı :"))

# if (a > b) and (a > c) :
#     print(f"1.sayı :{a} en büyük sayıdır ")
# elif (b > c) and (b > a) :
#     print (f"2.sayı :{b} en büyük sayıdır ")
# else : 
#     print(f"3.sayı :{c} en büyük sayıdır. ")

#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı. 
#   a) ortalama 50 olsa bile final notu en az 50 olmalıdır.
#   b) Finalden 70 alındıgında ortalamanın önemi kalmaz.

# vize1 = float(input("1.vize :"))
# vize2 = float(input("2.vize :"))
# final = float(input("final :"))

# ortalama =  ((( (vize2+vize1)/2)*0.6 ) + (final)*0.4 )

# if ((ortalama >= 50 ) and (final >= 50) ) or (final >= 70):
#     print(f"Ortalaması : {ortalama} , Başarı durumu : Geçti")
# else :
#     print(f"Ortalaması : {ortalama} ,Başarı durumu : Kaldı")

# 6 kişi kilo

ad = input("İsim :")
kilo = float(input("Kilonuz :"))
boy = float(input("boyunuzu metre cinsninden giriniz : "),)

indeks = (kilo / (boy**2))
# zayıf = ( indeks > 0) and (indeks < 18.4)
# normal = (indeks >= 18.4) and (indeks < 24.9)
# kilolu = (indeks >= 25) and (indeks < 29.9)
# sisko = (indeks >= 30) and (indeks < 34.9)

if ( indeks > 0) and (indeks < 18.4):
    print(f" {ad} isimli bireyin kilosu :{kilo} , boyu : {boy} ve zayıftır")
elif (indeks >= 18.4) and (indeks < 24.9):
    print(f" {ad} isimli bireyin kilosu :{kilo} , boyu : {boy} ve normaldir")
elif (indeks >= 25) and (indeks < 29.9):
    print(f" {ad} isimli bireyin kilosu :{kilo} , boyu : {boy} ve kiloludur")
elif (indeks >= 30) and (indeks < 34.9):
    print(f" {ad} isimli bireyin kilosu :{kilo} , boyu : {boy} ve obezdir")
    