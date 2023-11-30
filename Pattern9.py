n=int(input("Enter a number : "))
for i in range(n,0,-1):
        for j in range(0,n-i):
                print(end=" ")
        for j in range(0,i):
                print("*",end=" ")
        print()
for i in range(2,n+1,1):
        for j in range(1,n-i+1,1):
                     print(end=" ")
        for k in range(1,i+1):
              print("*",end=" ")
        print()

'''
Output:
    n=3
    * * *
     * *
      *
     * *
    * * *
'''