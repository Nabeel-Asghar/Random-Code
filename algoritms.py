#algoritm to find if array has duplicates in linear time
#array is 1 to n
n = 10
array = [1,2,3,4,5,6,7,8,9,10,3]
x = len(array)
if x>n:
    print("The array has a duplicate")

#Given two strings representing integer numbers ("123" , "30") return a string representing the sum of the two numbers ("153")
a = "123"
b = "30"
a = int(a)
b = int(b)
c = a + b
c = str(c)
print(c)

#splitting a string
a = "123.456"
b,c = a.split(".")
print(b,c)

#Generate an array from numbers to number of that numbers, 2 1s, 3 2s, 1 3s
array = [1,1,2,2,2,3,3]

newArray = set(array)
newDict = dict(zip(newArray,range(len(newArray))))
newDict = dict.fromkeys(newDict, 0)
for i in array:
    if i in newDict:
        newDict[i]+=1

array = []
for i,v in newDict.items():
    array.append(v)
    array.append(i)
print(array)



#function in linear time to find max of 2 numbers
#def max(a,b):
#    max = (a+b)/2 + abs(a-b)/2
#    return max
#a,b= input("Enter two numbers: ")
#
#print("The max of %s and %s is %s" % (a, b, max(a,b)))
#
#Find min and max values in array
array = [5,6,7,8,23,0,120,1,12]

min = 1000
max = 0

for i in array:
    if i<min:
        min = i
    if i>max:
        max = i

print("The max is %s and the min is %s" %(max, min))
