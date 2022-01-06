"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı 
    ifadeler ile buldurmaya çalın
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
        üzerinden hesaplansın.

    """
import random

randomNumber = random.randint(0,100)
print(randomNumber)
i = 0
down = "Aşağı"
up = "Yukarı"

# First step.

"""
answerCount = 5
i = 0
down = "Aşağı"
up = "Yukarı"
while i < answerCount :
    i += 1
    answer = int(input("tahmin ettiğiniz sayı : "))
    if answer > randomNumber:
        print(f"Yeni bir tahmin : {down} .")
    elif answer < randomNumber:
        print(f"Yeni bir tahmin : {up} .")
    else :
        print(f"Sayıyı doğru tahmin ettiniz tebrikler!!!")
    break
"""
# second step total point is 100 and each answer 20 points
""" 
totalPoint = 100
answerCount = 5
damege = 20
while i < answerCount :
    i += 1
    answer = int(input("tahmin ettiğiniz sayı : "))
    if answer > randomNumber:
        print(f"Yeni bir tahmin : {down} . kalan hakkınız {answerCount-i} ")
    elif answer < randomNumber:
        print(f"Yeni bir tahmin : {up} . kalan hakkınız {answerCount-i} ")
    else :
        print(f"Sayıyı doğru tahmin ettiniz tebrikler!!! Sayı : {randomNumber} , Puanınız {totalPoint}")
        break
    totalPoint -= damege
if answer != randomNumber:
    print(f"Başka hakkınız kalmadı . Puanınız : {totalPoint} , tahmin edilmeye çalısılan sayı : {randomNumber} ")

"""
# third step, User give a how many chance for prediction. Each answer is effect to points.

totalPoint = 100
answerCount = int(input("Kaç tahminde bulunmak istiyorsunuz : "))
pointCarculate = totalPoint/answerCount
damege = 20
while i < answerCount :
    i += 1
    answer = int(input("tahmin ettiğiniz sayı : "))
    if answer > randomNumber:
        print(f"Yeni bir tahmin : {down} . kalan hakkınız {answerCount-i} ")
    elif answer < randomNumber:
        print(f"Yeni bir tahmin : {up} . kalan hakkınız {answerCount-i} ")
    else :
        print(f"Sayıyı doğru tahmin ettiniz tebrikler!!! Sayı : {randomNumber} , Puanınız {totalPoint}")
        break
    totalPoint -= pointCarculate
if answer != randomNumber:
    print(f"Başka hakkınız kalmadı . Puanınız : {totalPoint} , tahmin edilmeye çalısılan sayı : {randomNumber} ")





