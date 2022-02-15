# dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adı,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirler.

# "w" : (Write) yazma modu. Dosyayı konumda oluşturur.
#       ** dosyayı konumda oluşturur
#       ** dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w",encoding= "utf-8")
# file.write("Ahmet Özcan")
# file.close()

# "a" : (Append) ekleme. Dosya konumda yoksa oluşturur.

# file = open("newfile.txt","a",encoding= "utf-8")
# file.write("Ahmet Özcan")
# file.write("\nAhmet ")
# file.close()


# "x" : (Create) oluşturma.Dosya zaten varsa hata verir.
# file = open("newfile2.txt","x",encoding= "utf-8")

# "r" : (read) okuma. varsayılan. dosya konumda yoksa hata veir.
