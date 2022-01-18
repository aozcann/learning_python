# x = 10

# if x > 5:
#     raise Exception("x cannot greater than 5")

from ast import Try


# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Password cannot shorter than 8 characters")
#     elif not re.search("[a-z]",psw):
#         raise Exception("The password must incluad lower case.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("The password must incluad Upper case.")
#     elif not re.search("[0-9]",psw):
#         raise Exception("The password must incluad Number.")
#     elif not re.search("[_@$]",psw):
#         raise Exception("The password must incluad alpha numeric character.")
#     elif re.search("\s",psw):
#         raise Exception("The password not incluad a space.")
#     else:
#         print("correct password")

# password = "12345678aA_"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("correct password come from try else")
# finally:
#     print("validation completed")

class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("Name cannot longer than 10 characters")
        else:
            self.name = name

p = Person("Ahmettttttttt", 2020)