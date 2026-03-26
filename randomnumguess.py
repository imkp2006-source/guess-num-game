import random 

num = 0
target = random.randint(1,100)


while (num != target):
    num = input("Enter your choice or Quit(Q)")
    
    if(num == "Q" or num == "Quit"):
        break
    num = int(num)
    if (num == target):
        print("COngratulations! you gussed correctly ")
        break
    elif (num < target) :
        print("enter a bigger number")
    elif (num > target) :
        print("enter a smaller number")

print("----GAME OVER----")
