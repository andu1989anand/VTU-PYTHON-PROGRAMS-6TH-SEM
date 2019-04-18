"""
Using Regular Expressions create a python program to find maximum seats obtained in ELECTION of 2018, and congratulate the PARTY and PM Candidate with a message by extracting it.
file name: seatcount.txt
BJP  ELE2018  282  NAMO
CONGRESS  ELE2018  044  RAHUL_GANDHI
AIADMK  ELE2018  037  JAYA
TRINAMOOL  ELE2018  034  MAMATA
SHIVSENA  ELE2018  018  THACKERAY
BJP  ELE2019  445  NAMO
CONGRESS  ELE2019  000  RAHUL_GANDHI
AIADMK  ELE2019  030  RAJINI
TRINAMOOL  ELE2019  030  MAMATA
SHIVSENA  ELE2019  040  THACKERAY
"""
import re
d=[]
fd=open('seatcount.txt','r')
for line in fd:
        seats=re.findall('ELE2018 ([0-9][0-9][0-9])',line)
        if len(seats)>0:
            for x in seats:
                d.append(int(x))
s=max(d)
print ('maximum seats obtained is:',s)

fd=open('seatcount.txt','r')
for line in fd:
    if re.search(str(s),line):
        winner=line.split()
        print('congratulations to winning party:',winner[0]) 
        print('congratulations to PM candidate:',winner[3])
"""
maximum seats obtained is: 282
congratulations to winning party: BJP
congratulations to PM candidate: NAMO

"""
