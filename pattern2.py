n= int(input("enter only odd number"))

for i in range(n//2+1):
    for j in range(n//2):
        print("-",end="")
    for j in range(i):
        print("1",end="")
    for j in range(n-2*i):
        print("@",end="")
    print()

for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or j==0:
            print("*",end="")
        else:
            print("-",end="")
        
    

    print()