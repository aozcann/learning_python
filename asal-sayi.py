"""
Soru: Girilen bir sayının asal olup 0lmadığını bulun
    ** Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılardır

"""

sayi = int(input("sayıyı girin:"))

asalmi = True

if sayi == 1:
    print("1 sayısı asal değildir.")

for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print(f"{sayi} sayısı asaldır.")
else:
    print(f"{sayi} sayısı asal değildir.")