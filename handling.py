# error handling => hata yönetimi

# try:    
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Can't use 0 for y")
# except ValueError:
#     print("U must to input integer for x and y")


# try:    
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print("Check your value")
#     print(e)


# try:    
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except:
#     print("Check your value")

while True:
    try:    
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("Check your value", ex)
    else:
        break
    finally:
        print("try except is over")