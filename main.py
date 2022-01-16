from types import resolve_bases
from unittest import result
import mymod
import math


# result = help(mymod)
# result = help(mymod.func)
result = mymod.number
result = mymod.numbers
result = mymod.person["name"]
result = mymod.person["age"]
result = mymod.func(10)

p = mymod.Person()
p.speak()



print(result)
