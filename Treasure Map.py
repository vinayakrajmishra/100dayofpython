line1 = ["☐", "☐", "☐"]
line2 = ["☐", "☐", "☐"]
line3 = ["☐", "☐", "☐"]
map = [line1, line2, line3]
print("Hiding your treasure X  marks the spot")
position = input("Where you want to put the treasure: ")
if int(position[1]) == 1:
    if (position[0]).lower() == "a":
        line1[0] = "X"
    elif (position[0]).lower() == "b":
        line1[1] = "X"
    elif (position[0]).lower() == "c":
        line1[2] = "X"
    else:
        print(f"You entered wrong position. Restart the program{exit()}")
elif int(position[1]) == 2:
    if (position[0]).lower() == "a":
        line2[0] = "X"
    elif (position[0]).lower() == "b":
        line2[1] = "X"
    elif (position[0]).lower() == "c":
        line2[2] = "X"
    else:
        print(f"You entered wrong position. Restart the program{exit()}")
elif int(position[1]) == 3:
    if (position[0]).lower() == "a":
        line3[0] = "X"
    elif (position[0]).lower() == "b":
        line3[1] = "X"
    elif (position[0]).lower() == "c":
        line3[2] = "X"
    else:
        print(f"You entered wrong position. Restart the program{exit()}")
else:
    print(f"You entered wrong position. Restart the program{exit()}")
print(f"{line1}\n{line2}\n{line3}")

