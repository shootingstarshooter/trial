def quad(a,b,c):
    disc=b*b-4*a*c
    if(disc==0):
        print("disc is 0")
    elif(disc>0):
        print("disc is +ve")
    else:
        print("dis is -ve")
a=int(input("enter the coeff"))
b=int(input("enter the coeff"))
c=int(input("enter the coeff"))
quad(a,b,c)
