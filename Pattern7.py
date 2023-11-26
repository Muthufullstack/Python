r = int(input("Enter a number : "))
c = int(input("Enter a number : "))
for i in range(r):
      if i == 0 or i == r - 1:
           print("*" * c)
      else:
           print("*" + " " * (c- 2) + "*")
            
'''
Output:
     r=3 and c=3

     * * *
     *   *
     * * *
'''