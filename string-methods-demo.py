from types import resolve_bases


website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python programlama rehberiniz (40 saat)"

# result = " Hello World ".strip()
# result = " Hello World ".lstrip()
# result = " Hello World ".rstrip()

# result = "www.sadikturan.com".strip('w.com')

# result = course.lower()
# result = course.upper()
# result = course.capitalize()

# result = website.count("a")
# result = website.startswith("www"),website.endswith(".com")

# result = website.find(".com")

# result = course.isalpha()

# result = "Contents".center(50,"*")

# result = course.replace(" ","-")
# result = "Hello World".replace("World","There")
result = course.split(" ")
result = result[5]
print(result)

