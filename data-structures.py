import sys

class treeNode:
    #Create binary tree
    def __init__(self,input):
        self.leftLeaf = None
        self.rightLeaf = None
        self.input = input

    #Print out the entire tree, prints out root, leaf leaf, right leaf
    def printTree(self):
        print(self.input)
        if self.leftLeaf:
            self.leftLeaf.printTree()
        if self.rightLeaf:
            self.rightLeaf.printTree()

    #Insert a value into a leaf of the the input/root
    def insert(self,input):
        if self.input:
            if not self.leftLeaf:
                self.leftLeaf = treeNode(input)
            elif not self.rightLeaf:
                self.rightLeaf = treeNode(input)
        else:
            self.input = input

    #Returns the root value
    def getRoot(self):
        return self.input

    #Returns the left leaf
    def getLeaf(self):
        if self.leftLeaf:
            return self.leftLeaf.input

    #Sets the left leaf to x
    def setLeaf(self,x):
        self.leafLeaf = x



# Prints to standard output.
def findStartAndEndLocations(pairs):

  #Create x as a placeholder
  x = treeNode(0)
  #Create a list to store the binary trees in
  list = []
  #Iterate through pairs, which as two columns so use two variables
  for i,j in pairs:

    #To account for if the list is equal to 1
    if len(pairs)==1:
      x = treeNode(i)
      x.insert(j)
      print("%s: %s" % (x.getRoot(), x.getLeaf()))

    #If the next root is not equal to the previous root, insert a new root,
    #and add a leaf
    if i!=x.getRoot():
      x = treeNode(i)
      x.insert(j)

      list.append(x)



  #Create a new list for the end locations
  newList = []
  for i in list:
    for j in list[1:]:

      #If the leaf of the i node is equal to the leaf of the j node,
      #set j as the new leaf for the i root node
      if i.getLeaf() == j.getRoot():
        y = treeNode(i.getRoot())
        y.insert(j.getLeaf())
        newList.append(y)

  #Print out the list in proper formatting
  for z in newList:
    print("%s: %s" % (z.getRoot(), z.getLeaf()))

# DO NOT MODIFY BELOW THIS LINE
def main():
  pairs = []

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()

    pairs.append(line.split(" "))

  findStartAndEndLocations(pairs)

main()
