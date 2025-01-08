minimum=0
maximum=0
for a in range(0,5):
    x=int(input("ent"))
    if(a==0):
        minimum=maximum=x
    if(x<minimum):
        minimum=x
    if(x>maximum):
        maximum=x
print("min and max are:",minimum,maximum)
