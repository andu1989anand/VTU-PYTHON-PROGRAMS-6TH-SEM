"""

Create a program to look for lines of the form:
We just received $50.00 for 10 cookies.
We just received $20.00 for 2 dolls.
We just received $30.00 for 5 bats.
We just received $15.00 for 11 tattoos.
and extract the amount with dollar sign from
each of the lines using a regular expression.
Count and print the number of total items,
total amount they have received.

"""
import re
sum=0
c=0
fd=open('4b.txt','r')
for line in fd:
    x=re.findall('(\$[0-9]+.[0-9]+)',line)
    for i in x:
        print (i)
    x=re.findall('([0-9]+.[0-9]+) for ([0-9]+)',line)
    for i,j in x:
        sum=sum+float(i)
        c=c+float(j)
print ('Total items:',c)
print ('Total Amount Received:',sum)


"""
$50.00
$20.00
$30.00
$15.00
Total items: 28.0
Total Amount Received: 115.0
"""
