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