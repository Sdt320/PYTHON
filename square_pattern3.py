print("hi welcome to coding")
'''

*  *  *  *  *  
*           *
*           *
*           *
*  *  *  *  *
'''
k=0
for x in range(5):
    for j in range(5):
        if x==0 or x==4 or j==0 or j==4:
            k +=1
            print("*",end="  ")
        else:
            print(" ",end="  ")
        
    print()
