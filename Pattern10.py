m=int(input("Enter a number   :"))
for i in range(1, m + 1,1):
   for j in range(1,i+1,1):
                  print("*", end=" ")
   print()
for i in range(1,m + 1,1):
    for j in range(1,(m-i)+1,1):
        print("*",end=" ")
    print()
'''
Output:
   n=3
   *
   * *
   * * *
   * *
   *
   
'''