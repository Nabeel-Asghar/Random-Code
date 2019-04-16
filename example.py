#How to do classes and objects
class myClass(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getEverything(self):
        return(self.name, self.age, self.gender)


stuff = myClass("Nabeel Asghar", 20, "Male")
stuff.setName("Nabdeel Asghar")
#print(stuff.getEverything())

#for i in range(10):
    #print("The number is:",i)

ourList = ["Hello", "World", "This", "Is", "Nabeel"]
ourDict = {"Brand:" : "Toyota", "Model:" : "Camry", "Year:" : 2018}

#for i in range(len(ourList)):
#    print(ourList[i])
#for i in ourList:
#    print(i)
x = ourDict.get("Model:")
print(x)
for i in ourDict:
    print(i, ourDict[i])



def max(a,b):
    max = (a+b)/2 + abs(a-b)/2
    return max
a,b= input("Enter two numbers: ")
print(a,b)
print("The max of %s and %s is %s" % (a, b, max(a,b)))




#employee = "Mr. Patel"
#print("Employee of the month is %s" % employee)





n = 10
array = [1,2,3,4,5,6,7,8,9,10,3]
x = len(array)
if x>n:
    print("The array has a duplicate")
