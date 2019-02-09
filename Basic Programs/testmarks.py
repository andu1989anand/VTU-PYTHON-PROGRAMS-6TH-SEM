a=input("enter test1:")
b=input("enter test2:")
c=input("enter test3:")
if a>b and a>c:
    big=a
    if b>c:
        print (a+b)/2.0
    else:
        print (a+c)/2.0
elif b>a and b>c:
    big=b
    if a>c:
        print (b+a)/2.0
    else:
        print (b+c)/2.0
else:
    big=c
    if a>b:
        print (c+a)/2.0
    else:
        print (c+b)/2.0

