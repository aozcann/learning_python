#1 - Girilen 2 sayıdan hangisi büyüktür?
# a = int(input("1.sayı :"))
# b = int(input("2.sayı :"))
# print(f"1.sayıyla:{a} 2. sayı:{b} eşit mi? =", a == b)
# print(f"1.sayıyla{a} 2. sayıdan{b} büyük müdür? =", a > b)
# print(f"1.sayıyla{a} 2. sayıdan{b} küçük müdür? =", a < b)
#2 - Kullanıcan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a = int(input("1.vize :"))
# b = int(input("2.vize :"))
# c = int(input("final :"))
# ortalama = ((a+b)/2*0.6) + (c*0.4)
# print(ortalama)
# gecti = True
# kaldı = False
# print(f"not ortalamanız : {ortalama} ve sınavdan geçme durumuz: {ortalama>=50} ")
# 3- Girilen bir sayının tek mi çift mi oldugunu yazdırın
# sayi = int(input("Sayı :"))
# tekcift = sayi % 2 == 1
# print(f"Sayınız tektir : {tekcift}")
# 4- Girilen sayının negatif mi pozitif mi oldugunu yazdırınız.
# sayi = int(input("Sayi :"))
# pozitifnegatif = sayi < 0
# print(f"Sayı negatiftir : {pozitifnegatif}")
# 5 - parola ve email bilgisini isteyip doğrulugunu kontrol edin.

userEmail = input("email adresinizi giriniz : ")
userPassword = input("parolanızı giriniz : ")

email = "email@sadikturan.com" == userEmail
password = "abc123" == userPassword

print(f"Kullanıcı adı : {email} ve parola : {password} ")