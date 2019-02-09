def prime(n):
    for i in range(2,n):
        if n%i==0: 
            return 0
        else:
            continue
    return n

num=input("enter a number:")
result=prime(num)
if result!=0:
    print num," is a prime number"
else:
    print num, "is not a prime number"
