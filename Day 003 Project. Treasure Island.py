print("Welcome to Treasure Island \n Your mission is to find treasure. \n --------------------")
print("You\'r at a cross road. Where you want to go \"Left\" or \"Right\" ")
stage1 = (input()).lower()
if stage1=="left":
    print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    stage2=(input()).lower()
    if stage2=="wait":
        print("You arrived at the island unharmed. There is a house with 3 doors. One Read, one Yellow & one Blue. Which colour do you choose?")
        stage3=(input()).lower()
        if stage3=="yellow":
            print("**************** \n You found treasure, You win \n ****************")
        elif stage3=="red":
            print("**************** \n There is hungry lion in red room, It ate you. Game Over \n ****************")
        elif stage3=="blue":
            print("**************** \n There is big fire in blue room, you got burned. Game Over \n ****************")
        else:
            print("Wrong Input, Game Over")
    elif stage2 == "swim":
        print("**************** \n There is high tide, you sunk in ocean \n ****************")
    else:
        print("Wrong Input, Game Over")
elif stage1=="right":
    print("**************** \n You fell into a hole. Game Over \n ****************")
else:
    print("Wrong Input, Game Over")