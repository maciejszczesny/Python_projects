space = ' '
star = '*'
number = 1
numberMemory = 0
heightOfTree = 15
spacesFromHeight = heightOfTree

while numberMemory <= heightOfTree:
    print(space*spacesFromHeight + star*number + space)
    #icrease number of stars to get 1,3,5,7.... numbers
    number += 2
    #Increase memory to get to height of tree declared from user
    numberMemory += 1
    #Decrease number of spaces to print to get shape of christmas tree, without this will receive "half" tree
    spacesFromHeight -= 1

