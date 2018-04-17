"""python program to print mathematical table"""

num=input("enter a number")
for i in range(1,num+1):
    for j in range(1,11):
        print i,"X",j,"=",j*i
