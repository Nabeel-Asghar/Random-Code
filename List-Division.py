#Given two lists, outputs a number from the first list if it is divisable
#by at least half of the numbers in the second list

def divisionFunc(listA, listB, c):
    listAnswer = []

    for i in listA:
        count = 0
        for j in listB:
            if i%j == 0:
                count+=1
        if count >= c:
            listAnswer.append(i)

    listAnswer = set(listAnswer)
    print(listAnswer)



inputA = input("Enter a list of numbers seperated by a space: ")
listA =  list(map(int,inputA.split(' ')))

inputB = input("Enter a list of numbers seperated by a space: ")
listB =  list(map(int,inputB.split(' ')))

c = len(listB)/2

divisionFunc(listA, listB, c)

k = input("Press any key to exit ")
