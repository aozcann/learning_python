from email import generator, iterators


def cube():

    for i in range(5):
        yield i ** 3

iterator = cube()

# iterator = iter(generator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)

liste = [i**3 for i in range(5)]
print(liste)
generator = (i**3 for i in range(5))

for i in generator:
    print(i)