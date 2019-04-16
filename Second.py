from array import array

matrix = [[1,0,0,1,1,1],[1,0,1,1,0,1],[0,0,1,1,1,1],[0,1,1,1,1,1]]

cumulativeSum= [0] * len(matrix[0])

for r in range(len(matrix)):

    i=0
    for c in range(len(matrix[r])):

        if (matrix[r][c])>0:
            x = cumulativeSum[i] + 1
            cumulativeSum[i]=x

        if (matrix[r][c])==0:
            cumulativeSum[i]=0

        i+=1

print(cumulativeSum)


length = 0
previous = 0
maxArea = []
for i in cumulativeSum:
    
    if i>0:
        length+=1

    else:
        length = 0
        continue

cumulativeSum.sort()
print(cumulativeSum)
print(length)

#area = low*length
#print("The biggest rectangle has an area of: ", area)
