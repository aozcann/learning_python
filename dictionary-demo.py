
ogrenciler = {}
print("İlk öğrenci bilgileri".center(50,"*"))
studentNumber = input("Öğrenci numaranızı giriniz = ")
studentName = input("Öğrenci adınızı giriniz = ")
studentLastName = input("Öğrenci soyadınızı giriniz = ")
studentPhone = input("Öğrenci telefon numaranızı giriniz = ")

studentInfo = {
    "ad": studentName,
    "soyad": studentLastName,
    "telefon": studentPhone
}
ogrenciler[studentNumber] = studentInfo

print("İkinci öğrenci bilgileri".center(50,"*"))
studentNumber = input("Öğrenci numaranızı giriniz = ")
studentName = input("Öğrenci adınızı giriniz = ")
studentLastName = input("Öğrenci soyadınızı giriniz = ")
studentPhone = input("Öğrenci telefon numaranızı giriniz = ")
studentInfo = {
    "ad": studentName,
    "soyad": studentLastName,
    "telefon": studentPhone
}
ogrenciler[studentNumber] = studentInfo
print("Üçüncü öğrenci bilgileri".center(50,"*"))

studentNumber = input("Öğrenci numaranızı giriniz = ")
studentName = input("Öğrenci adınızı giriniz = ")
studentLastName = input("Öğrenci soyadınızı giriniz = ")
studentPhone = input("Öğrenci telefon numaranızı giriniz = ")
studentInfo = {
    "ad": studentName,
    "soyad": studentLastName,
    "telefon": studentPhone
}
ogrenciler[studentNumber] = studentInfo
print(ogrenciler)
StudenWantNumber = input("Bilgi almak istedğiniz öğrencinin numarasını giriniz =" )
print(ogrenciler[StudenWantNumber]["ad"])