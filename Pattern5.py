n=int(input("Enter a number : "))
for i in range(n,0,-1):
	for j in range(0,n-i):
		print(end=" ")
	for j in range(0,i):
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