class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return("%s is %s years old" % (self.name, self.age))

    def isOld(self):
        if self.age > 4:
            return("%s is old" % (self.name))

class Golden(Dog):
    def __init__(self,name,age,fur):
        Dog.__init__(self,name,age)
        self.fur = fur

    def stuff(self):
        print(self.fur)

class BullDog(Dog):
    def __init__(self,name,age, fur):
        Dog.__init__(self,name,age)
        self.fur = fur

    def furry(self):
        print(self.fur)


idiot1 = Golden("Golden Retrievre", 5, "gold")
idiot2 = BullDog("Bulldog", 5, "brown")

idiot1.stuff()
