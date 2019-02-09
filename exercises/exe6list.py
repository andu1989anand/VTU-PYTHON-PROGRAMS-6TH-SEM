values=[]
while True:
    num=raw_input("enter a value/enter done to finish::")
    
    if num=='done':
        print 'max=',max(values)
        print 'min=',min(values)
        print 'sum=',sum(values)
        print 'len=',len(values)
        print 'avg=',sum(values)/len(values)
        break
    else:
        temp=float(num)
        values.append(temp)
