class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setjob(self, job):
        self.job = job

    def getjob(self):
        print("My job is", self.job)

    def random(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")

per1 = Person('Joe', 21)
per2 = Person('Ann', 45)

per1.random()
per2.random()

per1.setjob('Artist')
per1.getjob()