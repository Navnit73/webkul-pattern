# #webkul pattern program round 1 
# #pattern runs for odd number like min 3 , 5, 7 etc
# #here is ther pattern
# #for n==3
# *       *
# **     **
# ***@@@***
#    @@@
#    @@@
#    ***
#     *
# #for n==5 
# *             *
# **           **
# ***         ***
# ****       ****
# *****@@@@@*****
#      @@@@@
#      @@@@@
#      @@@@@
#      @@@@@
#      *****
#       ***
#        *
# #and so on for n==7.....
# #here is the program


n=5
for i in range(n+1):
    for j in range(i):
        print('*',end='')
    for j in range(n-i):
        print(' ',end='')
    for j in range(n):
        if(i==n):
            print('@',end='')
        else:
            print(' ',end='')
    for j in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in range(n-1):
    for j in range(3*n):
        if(j<n or j>2*n-1):
            print(' ',end='')
        else:
            print('@',end='')
    print()
for i in range(n//2+1):
    for j in range(n):
        print(' ',end='')
    for j in range(i):
        print(' ',end='')
    for j in range(n-2*i):
        print('*',end='')
    for j in range(i):
        print(' ',end='')
    for j in range(n):
        print(' ',end='')
    print()
    