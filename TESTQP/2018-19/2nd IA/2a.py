"""
With example code explain Dictionary in python. Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary. Figure out who has sent the most messages by displaying the name and count.
From: hodcse@mitmysore.in mon 11 Feb 10:23:15 2019
From: hodmech@mitmysore.in sat 15 Feb 12:28:25 2019
From: hodcse@mitmysore.in sun 17 Feb 11:25:55 2019
……

"""

import re
d=dict()
fd=open('mail.txt','r')
for line in fd:
    if line.startswith('From: '):
        mail=re.findall('\S+@\S+',line)        
        if len(mail)>0:
            for x in mail:
                if x not in d:
                    d[x]=1
                else:
                    d[x]=d[x]+1
print('histogram is:',d)

lst=[]
for k,v in d.items():
    lst.append((v,k))
lst.sort(reverse=True)
m=lst[0][1]
name,domain=m.split('@')
print ('most msgs sent by:',name)
print ('number of msgs are:',lst[0][0])

"""
histogram is: {'hodcse@mitmysore.in': 2, 'hodmech@mitmysore.in': 1}
most msgs sent by: hodcse
number of msgs are: 2

"""
