# Inheritance (kalıtım): Miras alma

# Person => name, lastname , age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal) , Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("I am a Person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self ,fname ,lname, Number):
        Person.__init__(self ,fname ,lname)
        self.studentNumber = Number
        print("Student Created")

    

    # override
    def who_am_i(self):
        print("I am a Student")

    def sayHello(self):
        print("Hello I am a stundent")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("Ahmet","ÖZCAN")
s1 = Student("Hasan","SEVER",1234)
t1 = Teacher("Sevil","Toprak","Physic")

print(f"My first name : {p1.firstName} and surname : {p1.lastName} ")
print(f"My first name : {s1.firstName} and surname : {s1.lastName} and My number {s1.studentNumber} ")


p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
t1.who_am_i()