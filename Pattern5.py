n=int(input("Enter a number : "))
for i in range(n,0,-1):
	for j in range(1,n-i):
		print(end=" ")
	for j in range(1,i):
		print("*",end=" ")
	print()
'''
      n=5
Output:
    * * * * *
     * * * *
      * * *
       * *
        *