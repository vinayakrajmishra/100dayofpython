target = int(input("Enter a target number: "))
sumofeven = 0
for i in range(0, target+1):
    if i % 2 == 0:
        sumofeven = sumofeven + i

print(f"Sum of all even numbers b/w 0 and {target} is: {sumofeven}")
