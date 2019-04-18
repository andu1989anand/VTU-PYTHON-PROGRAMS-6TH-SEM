"""
Using Regular Expressions Create a python program to find and display average marks obtained in each subjects of 15 series students only.
file name: averagemarks.txt
YASH  4MH16CS103  OS  15  16  14  kgf@gmail.com
YOGARAJ_BATTRU  4MH15CS010  SE  28  15  26  yoga@gmail.com
JAGGESH  4MH15CS001  PP  15  25  29  jaggesh@gmail.com
KURI_PRATHAP  4MH16CS102  CG  10  11  14  kuri@gmail.com
CHIKANNA  4MH15CS100  CNS  10  11  14  chikanna@gmail.com

"""

import re
import math
fd=open('a.txt','r')
for line in fd:
    words=line.split()
    if re.search('15CS',line):
        a=re.findall(' [0-9][0-9]',line)
        if len(a)>0:
            x=list()
            for i in a:
                x.append(float(i))
                avg=math.ceil((sum(x))/len(x))
            print ("name=",words[0],'usn=',words[1],'sub=',words[2],'avg=',avg)

"""
name= YOGARAJ_BATTRU usn= 4MH15CS010 sub= SE avg= 23
name= JAGGESH usn= 4MH15CS001 sub= PP avg= 23
name= CHIKANNA usn= 4MH15CS100 sub= CNS avg= 12
"""
