# global scope
x = "global x"

def function():
    #local scope
    x = "local x"
    print(x)

function()
print(x)

################################

name = "Ahmet"

def changeName(new_name):
    name = new_name
    print(name)

changeName("Sevil")
print(name)

#############################

name = "Global string"

def greeting():
    # name = "Ayşe"

    def hello():
        # name = "İlknur"
        print("hello " + name)

    hello()

greeting()
print(name)

#########################

x = 50
print(x)
def test():
    global x
    print(f"x : {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)