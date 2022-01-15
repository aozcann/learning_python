import random

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
result = random.random() * 100 # 0.0 - 1.0
result = int(random.uniform(10,100))
result = random.randint(1,100)

greeting = "Hello there"
names = ["ahmet","yağmur","sevil","ayşe","ali","cenk"]
result = names[random.randint(0,len(names)-1)]

result = random.choice(names)
result = random.choice(greeting)

lst = list(range(10))
random.shuffle(lst)

result = lst

lst = range(100)
result = random.sample(lst,7)
result = random.sample(names,2)


print(result)