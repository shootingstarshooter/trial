minimum=0
maximum=0
for a in range(0,5):
    x=int(input("enter the number"))
    if (x<minimum):
        minimum=x
    if(x>maximum):
        maximum=x

print("max and min of given nos is:",maximum,minimum)
