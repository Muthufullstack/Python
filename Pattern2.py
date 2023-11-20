m=int(input("Enter a number of rows"))
for i in range(1,m + 1,1):
    for j in range(1,(m-i)+1,1):
        print("*",end=" ")
    print()