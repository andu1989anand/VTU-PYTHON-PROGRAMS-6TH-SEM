x=list()
count=0
fd=open('b.txt','r')
for line in fd:
    count=count+1
    if line.startswith('From:'):
         a=line.find('Amount')
         c=line.find(':',a)
         sp=line.find(' ',c)
         num=line[c+1:sp]
         x.append(float(num))
print ('sum=',sum(x),'avg=',sum(x)/len(x))
print ('no of lines=',count)


"""
From:  Darshan Amount:34500.00  Webnesday Jan 02 2019
Available Balance: 534500.00	
From:  Sudeep Amount:23999.70  Sunday Jan 20 2019
Available Balance: 558499.70
From:  Punith Amount:17899.99  Thursday Feb 14 2019
Available Balance: 576399.69
From:  Sudeep Amount:12999.70 Wednesday Mar 20 2019
"""

"""

OUTPUT:
sum= 89399.39 avg= 22349.8475
no of lines= 7
"""
