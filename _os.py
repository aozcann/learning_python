import os
from datetime import datetime 

result = dir(os)
result = os.name

# klasör oluşturma
# os.mkdir("newdirectors") 
# os.makedirs("newdirectors/yeniklasör")
# os.rename("newdirectors","yeni klosör")
# os.rmdir("newdirectory")
# os.removedirs("yeni klosör\yeniklasör")

#dizin değiştirme
# os.chdir("C:\\")
# os.chdir('..')
# os.chdir('../..')

# etkin dizin öğrenme
# result = os.getcwd()

# listeme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

result = os.stat("date.py")
# result = result.st_size/1024
# result = datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi
# result = datetime.fromtimestamp(result.st_atime)    # son erişilme tarihi
# result = datetime.fromtimestamp(result.st_mtime)    # değiştirime tarihi

# os.system("notepad.exe")

# path

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/Users/AEO/Desktop/python_temelleri/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("C:/Users/AEO/Desktop/python_temelleri/_os1.py")
result = os.path.exists("C:/Users/AEO/Desktop/python_temelleri")
result = os.path.isdir("C:/Users/AEO/Desktop/python_temelleri")
result = os.path.isfile("C:/Users/AEO/Desktop/python_temelleri/_os.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]

print(result)