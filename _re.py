import re
from turtle import st

result =dir(re)

# re module

str = 'Python öğreniyorum: Python programlama dili bitmiyordu 15 saat oldu ama eğlenceli. '

# re.findall()

# result = re.findall("Python",str)
# result = len(result)

# re.split()

# result = re.split(":",str)

#  re.sub

# result = re.sub(" ","-",str)
# result = re.sub("\s","-",str)

# re.search

# result = re.search("Python",str)

# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string()

# regular expression

result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[1-9]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)

result = re.findall("...",str)
result = re.findall("Py..on",str)

result = re.findall("^P",str) # ile başlıyor mu


result = re.findall("Python$",str) # ile biten
result = re.findall("t$",str)

result = re.findall("sa*t",str) # bir karakterin sıfır ya da daha fazla olmasını kontrol eder

result = re.findall("sa+t",str) #+ bir karakterin bir ya dadaha fazla sayıda olmasını kontrol eder.

result = re.findall("sa?t",str) #? 0 yada bir kere
# eşleşme olmaz "sat" yapmamız gerekir eşleşme için

"""
    {} - karakter sayısını kontrol eder.

        al{2} => a karakterinin arkasına l karakteri 2 kez tekrarlanır
        al{2,3} => a karakterinin arkasına l karakteri en az 2 kez en falza 3 kere tekrarlanır
        [0-9]{2,4} => en az 2 en fazla 4 basamaklı sayılar.

"""
result = re.findall("a{2}",str) # aa
result = re.findall("[0-9]{2,4}",str)   # sayi

result = re.findall("a|b",str) # a ya da b

result = re.findall("(c|e|s)aat",str) # () gruplama

""" 
    \ - özel karakter aramamızı sağlar.

    \A - Berlitilen karakter string in aşında mı?
        \Athe => the string in başında mı

    \Z - Berlitilen karakter string in sonunda mı?
        the\Z => the string in sonunda mı

    \b - Berlitilen karakter kelimenin başında mı sonunda mı?
        \bthe => the kelimenin başında mı?
        the\b => the kelimenin sonunda mı?

    \B - Belirtilen karakter kelimenin başında ya da sonunda değil mi?
        \Bthe => the kelimenin başında değil mi?
        the\B => the kelimenin sonunda değil mi?

    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
        \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
        \D => 1ab44_50

    \s - Boşluk karakterini arar.
    \S - Boşluk karakteri dışındakiler.
    \w - Alfabetik karakterler,rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi 

"""

result = re.findall("\APython",str)
result = re.findall("eğlenceli. \Z",str)
result = re.findall("\d",str)
result = re.findall("\D",str)
result = re.findall("\w",str)


print(result)