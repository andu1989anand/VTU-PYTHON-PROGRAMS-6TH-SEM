ec=0
oc=0

while 1:
    x=raw_input("enter a number")
    if x=='done':
        print "even=",ec,"odd",oc
        break
    else:
        y=int(x)
        if y%2==0:
            ec=ec+1
        else:
            oc=oc+1
                
