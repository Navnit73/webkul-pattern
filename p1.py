# Input : 3
# Output : 
#                             @
#                            @@@
#                           @@@@@
#                           *   *
#                          **@@@**
#                           *   *
# Input : 5
# Output : 
#                             @
#                            @@@
#                           @@@@@
#                          @@@@@@@
#                          *     *
#                         **     **
#                        ***@@@@@***
#                         **     **
#                          *     *

n=3
for i in range(n//2+2):
    for j in  range(n-i):
        print(" ",end='')
    for j in range(1+2*i):
        print('@',end='')
    print()
for i in range(1,n//2+1):
    if(i<n//2+1):
        for j in range(n//2-i+1):
            print(' ',end='')
        for j in range(i):
            print("*",end="")
        for j in range(n):
            print(" ",end='')
        for j in range(i):
            print("*",end="")
    print()
for i in range(1):
    for j in range(n+2*(n//2+1)):
        if(j<n//2+1 or j>n+n//2):
            print("*",end='')
        else:
            print('@',end='')
    print()
for i in range(n//2):
    for j in range(i+1):
        print(' ',end='')
    for j in range(n//2-i):
        print('*',end='')
    for j in range(n):
        print(' ',end='')
    for j in range(n//2-i):
        print('*',end='')
    print()