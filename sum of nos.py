n=int(input("enter"))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print("sum o digits is:",s)
