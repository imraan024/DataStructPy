blocks = int(input("Enter the number of blocks: "))

height = 0
sum = 0
if blocks == 0:
    print("The height of the pyramid:", height)
else:
    for i in range(1, blocks):
        sum = sum + i
        if sum <= blocks:
            height = height+1
        else:
            break
    
    print("The height of the pyramid:", height)
