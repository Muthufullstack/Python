n = int(input("Enter the value of n "))
for i in range(0,n+1,1):
    for j in range(-n,n+1,1):
        if(-i<j and j<i):
            print(" ",end="")
        else:
            print("*",end="")
    print()

'''
output:
    n=4
*********
**** ****
***   ***
**     **
*       *
'''