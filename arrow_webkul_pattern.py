

# n=3
# *
# **    *
# ********
# **    *
# *

# n=5

# *             
# **           
# ***         
# ****      *
# ************
# ****      *
# ***
# **
# *

n=5
for i in range(n-2):
    for j in range(i+1):
        print("*",end='')
    print()
print("*"*(n-1),end='')
print(" "*(n+1),end='')
print("*")
print("*"*(2*n+2))
print("*"*(n-1),end='')
print(" "*(n+1),end='')
print("*")

for i in range(n):
    for j in range(n-i-2):
        print("*",end='')
    print()
            
            
            
            
            
            
            
            
            
            
