def sayHello(name = "user"):
    return "Hello "+ name

msg = sayHello("Ahmet")
msg = sayHello("Ayşe")

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2022 - dogumYili

ageAhmet = yasHesapla(1994)
ageAlp = yasHesapla(2020)
ageFehmiye = yasHesapla(1965)

print(ageAhmet, ageAlp, ageFehmiye)

def EmekliligeKacYilKaldı(dogumYili , isim):
   """
   DOCSTRİNG: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
   INPUT: Doğum yılı
   OUTPUT: Hesaplanan yıl bilgisi
   """
   yas = yasHesapla(dogumYili)
   emekliklik = 65 -yas

   if emekliklik > 0:
        print(f"emekliliğine {emekliklik}'yıl kaldı. ")
   else :
        print("Zaten emekli oldunuz.")

EmekliligeKacYilKaldı(1983, "Ali")
EmekliligeKacYilKaldı(1950, "Ahmet")
EmekliligeKacYilKaldı(1974, "Yağmur")

print(help(EmekliligeKacYilKaldı))

print(help(list.append))
