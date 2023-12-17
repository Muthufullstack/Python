r = int(input("Enter r: "))
for i in range(r+1):
    line = ""
    for j in range(r+1):
        if abs(i - r//2) + abs(j - r//2) == r//2:
            line += "* "
        else:
            line += "  "
    print(line)
    
'''
Output 
       r=4
           *
         *   *
       *       *
         *   *
           *
'''