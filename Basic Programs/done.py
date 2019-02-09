"""program to take numbers and print count,sum,avg"""

count=0
sum=0

while 1:
    x=raw_input("enter a number")
    if x=='done':
        print count,sum,sum/float(count)
        break
    else:
        try:
            y=float(x)
            count=count+1
            sum=sum+y        
        except:
            print "enter valid string"
