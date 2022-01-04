#1- Girilen bir sayının 0-100 arasında olup olmadıgını kontrol ediniz.
# girilen = int(input("Sayı :"))

# result = girilen > 0 and girilen < 100

#2- Girilen bir sayının pozitif çift bir sayı olup olmadıgını kontrol edin.
# girilen = int(input("Sayı "))

# result = (girilen> 0 ) and (girilen %2 ==0 ) 
# Email ve parola bilgileri ile giriş kntrol edin

# email = "asd@asd.com"
# parola = "123asd"

# girilenEmail = input("Email :")
# girilenPassword = input("Parola : " )

# result = (email == girilenEmail) and (parola == girilenPassword )

# print(f"Email ile parola dogruluk durumu {result}")
# Girilen 3 sayıyı büyüklük olarak karşılaştırın.

# sayi1 = int(input("1.sayı :"))
# sayi2 = int(input("2.sayı :"))
# sayi3 = int(input("3.sayı :"))

# result1 = ((sayi1 > sayi2) and (sayi1 > sayi3) )    
# result2 = (sayi2 > sayi3) and (sayi2>sayi1)
# result3 = (result1) == (result2)
# print(f" Sayı1 en büyük sayıdır: {result1}")
# print(f" Sayı2 en büyük sayıdır: {result2}")
# print(f" Sayı3 en büyük sayıdır: {result3}")

# 5- Kullanıcadan 2 vize (%60) ve final (%40) notu olup orlama hesaplayınız.
#    Eger ortalama 50 ve üstündeyse geçti değilse kaldı.
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalde 70 aldıgında ortalamanın önemi kalmaz.

# vize1 = float(input("1.vize :"))
# vize2 = float(input("2.vize :"))
# final = float(input("final :"))

# Ortalama =  ((( (vize2+vize1)/2)*0.6 ) + (final)*0.4 )

# result =  ((Ortalama >= 50 ) and ( final >= 50)) or (final >= 70) 
# print(f"Sınavların ortalaması : {Ortalama} , sınavı geçme durumu : {result} ")

#6- Kişini ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayın.

ad = input("İsim :")
kilo = float(input("Kilonuz :"))
boy = float(input("boyunuzu metre cinsninden giriniz : "),)

indeks = (kilo / (boy**2))
zayıf = ( indeks > 0) and (indeks < 18.4)
normal = (indeks >= 18.4) and (indeks < 24.9)
kilolu = (indeks >= 25) and (indeks < 29.9)
sisko = (indeks >= 30) and (indeks < 34.9)
print(f" {ad} isimli bireyin kilosu :{kilo} , boyu : {boy} ")
print(f" {ad} zayıf : {zayıf} ")
print(f" {ad} normal : {normal} ")
print(f" {ad} fazla kilolu : {kilolu} ")
print(f" {ad} şişman (Obez ) : {sisko} ")
