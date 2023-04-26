n=int(input("enter the number of terms"))

a=0
b=1
c=a+b
if(n==1):
    print("0")
else:
    print("0 1 ",end=" ")
    for i in range (n-2):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
    print()
    
