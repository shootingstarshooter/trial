n=int(input("enter"))
m=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if (m==s):
    print("palin")
else:
    print("not palin")

    
