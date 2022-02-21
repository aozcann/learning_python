def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3)/3
    if 100 <= ortalama >=90 :
        harf = "AA"
    elif 89 <= ortalama >= 85:
        harf = "BA"
    elif 84 <= ortalama >= 80:
        harf = "BB"
    elif 79 <= ortalama >= 75:
        harf = "CB"
    elif 74 <= ortalama >= 70:
        harf = "CC"
    elif 69 <= ortalama >= 65:
        harf = "DC"
    elif 64 <= ortalama >= 60:
        harf = "DD"
    elif 59 <= ortalama >= 50:
        harf = "FD"
    else:
        harf = "FF"

    return ogrenciAdi + ": " + harf + "\n"

def ortalamaları_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input('Öğrenci adı: ')
    soyad = input('Öğrenci soyadı: ')
    not1 = input('not 1: ')
    not2 = input('not 2: ')
    not3 = input('not 3: ')

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")
def notları_kayıtet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input("1- notları oku\n2- Not gir\n3- okunanan notları kayıt et\n4- çıkış\n")

    if islem == "1":
        ortalamaları_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notları_kayıtet()
    else:
        break