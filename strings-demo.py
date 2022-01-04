website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python programlama rehberiniz (40 saat)"

result = len(course)
length = len(website)
print(result)
result = website[7:10]
print(result)
result = website[length-3:length]
print(result)
result = course[:15]
print(result)
result = course[-15:]
print(result)
result = course[::-1]
print(result)

name, surname, age, job = "Bora","Yılmaz", 32,"mühendis"

print(f"Benim adım {name} {surname}, Yaşım {age} ve Mesleğim {job}.")

s = 'Hello world'
# s = s[0:6] + "W" + s[-4:]
print(s)
s =s.replace('w','W')
print(s)
print("abc "*3)
