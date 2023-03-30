# Simple program to count pyramid levels
# The program takes a first number of blocks, and increase the levels one by one blocks
# The objective is to check the height of the pyramid and do an exercise using While Loop
blocks = int(input("Enter the number of blocks: "))
height = 0
#
#	
while (blocks > height): # if the blocks left are not higher than the height, it will not be enough blocks for the next level
    height += 1
    blocks -= height
    print(height*"#") # print function to print a "real" pyramid, to visually see the blocks and levels
print("The height of the pyramid:", height)
