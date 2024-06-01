#Flipping coin for a toss
import random
toss = random.randint(0,1)
print(toss)

userchoice =(input("Choose head or tails by typing H or T: ")).lower()
if userchoice == "h":
    if toss ==0:
        print("You Win")
    elif toss == 1:
        print("You Loose")
    else:
        print("You pressed wrong key")
elif userchoice == "t":
    if toss ==1:
        print("You Win")
    elif toss == 0:
        print("You Loose")
    else:
        print("You pressed wrong key")
