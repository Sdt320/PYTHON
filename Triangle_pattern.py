print("hi welcome to coding")
'''
hi welcome to coding
          *   
        *   *
      *   *   *
    *   *   *   *
  *   *   *   *   *
'''

for x in range(0,5):
    for j in range(5-x):
        print(" ",end=" ")
    for k in range(x+1):
        print("*",end="   ")
        
        
    print()
