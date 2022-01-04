# 1- Kullanıcıdan isim, yaş, ve eğitim bilgilerini isteyip ehliyet alabilme
#   durumu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#   lise ya da üniversite olmalıdır.

# name = input("İsim : ")
# yas = int(input("Yaşını : "))
# egitim = input("Eğitim durumu : ")

# if yas < 18:
#     print(f"{name} ehliyet için yaşınız uygun değil ")
# elif (egitim != "lise") and (egitim != "üniversite"):
#     print(f"{name} ehliyet eğitim seviyeniz uygun değil ")
# else :
#     print(f"{name} ehliyet için uygunsunuz ")
 
#2 - bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
#   not aralığına karşılık gelen not bilgisini yazdırınız.

# usernot = int(input("notu giriniz:  "))

# if (usernot >= 0) and (usernot <= 24):
#     print(f"{usernot} ile 0 aldınız")
# elif (usernot >= 25 ) and (usernot <= 44):
#     print(f"{usernot} ile 1 aldınız")
# elif (usernot >= 45) and (usernot <= 54):
#     print(f"{usernot} ile 2 aldınız")
# elif (usernot >= 55) and (usernot <= 69):
#     print(f"{usernot} ile 3 aldınız")
# elif (usernot >= 70) and (usernot <= 84):
#     print(f"{usernot} ile 4 aldınız")
# elif (usernot >= 85) and (usernot <= 100):
#     print(f"{usernot} ile 5 aldınız")
# else :
#     print("Yanlış bir değer girdiniz.")

#3- trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdaki bilgilere göre hesaplayınız.


# if 2021
import datetime
yıl = int(input("Aracın trafiğe çıktıgı yıl : "))
ay = int(input("Aracın trafiğe çıktıgı ay : "))
gun = int(input("Aracın trafiğe çıktıgı gün : "))

cıkıs = datetime.datetime(yıl, ay, gun)
x = datetime.datetime.now()

print(x)
print(cıkıs)
y = (x - cıkıs)
print(y)
if y <= datetime.timedelta(days= 365) :
    print("Aracın 1. bakım yılı")
elif y <= datetime.timedelta(days= 365*2) :
    print("Aracın 2. bakım yılı")
elif y <= datetime.timedelta(days= 365*3) :
    print("Aracın 3. bakım yılı")
else :
    print("Aracın bakım yılı geçti")