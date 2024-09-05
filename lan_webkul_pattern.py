# n=3
#     *
#   ***
#   @ @   
# ***@ @***
#  *     *


# n=5
#       *
#       ***
#      *****
#      @   @     
#      @   @     
#      @   @     
# *****@   @*****
#  ***       ***
#   *         *



n=5
for i in range(n//2+1):
    for j in range(n):
        print(' ',end='')
    for j in range(n//2-i):
        print(' ',end='')
    for j in range(1+2*i):
        print('*',end='')
    print()
for i in range(n-1):
    for j in range(3*n):
        if(j==n or j==2*n-1):
            print('@',end='')
        elif(i==n-2 and(j<n or j>2*n-1)):
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(n//2):
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-2-2*i):
        print('*',end='')
    for j in range(i+1):
        print(' ',end='')
    for j in range(n):
        print(' ',end='')
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-2-2*i):
        print('*',end='')
    print()



