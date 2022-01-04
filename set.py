from typing import Set


fruits = { "orenge", "apple" , "banana"}

# print(fruits[0]) İndekselenemez

for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango","grape","apple"])
fruits.remove("mango")
fruits.discard("apple")
print(fruits)

fruits.clear()
# fruits.pop()
print(fruits)

# mylist = [1,2,5,4,4,2]

# print(mylist)
# print(set(mylist))