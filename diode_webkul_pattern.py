
# n=3

# @       
# @@      @@@
# @@@*****@@@
# @@      @@@
# @       


# n=5

# @          
# @@         @@@@@
# @@@        @@@@@
# @@@@*******@@@@@
# @@@        @@@@@
# @@         @@@@@
# @     


n=5
for i in range(n-1):
    for j in range(i+1):
        print('@',end='')
    for j in range(n-2-i):
        print('_',end='')
    for j in range(n+2):
        if(i==n-2):
            print('*',end='')
        else:
            print('_',end='')
    for j in range(n):
        if(i>0):
            print('@',end='')
        else:
            print('_',end='')
    print()

for i in range(n//2+1):
    for j in range(n//2+1-i):
        print('@',end='')
    for j in range(i):
        print('_',end='')
    for j in range(n+3):
        print('_',end='')
    for j in range (n):
        if(i<n//2):
            print('@',end='')
        else:
            print(' ',end='')
    print()
