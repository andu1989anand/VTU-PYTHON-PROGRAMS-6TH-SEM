import re
import math
fd=open('a.txt','r')
for line in fd:
    words=line.split()
    a=re.findall(' [0-9][0-9]',line)
    if len(a)>0:
        x=list()
        for i in a:
            x.append(float(i))
        avg=math.ceil((sum(x)-min(x))/2)
        print ("name=",words[0],'usn=',words[1],'avg=',avg)

""" 
SAMPLE INPUT
RAMU 4MH15CS001 12 15 17
RAJU 4MH18CS003 19 18 12
"""

""" OUTPUT

name= RAMU usn= 4MH15CS001 avg= 16
name= RAJU usn= 4MH18CS003 avg= 19

"""
