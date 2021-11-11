import re
v=0
pw=input("enter the password:")
print('you have entered:',pw)
if len(pw)>=8:
    x=re.findall('[a-z]+',pw)
    if len(x)>0:
        y=re.findall('[A-Z]+',pw)
        if len(y)>0:
            z=re.findall('[0-9]+',pw)
            if len(z)>0:
                ss=re.findall('\W+',pw)
                if len(ss)>0:
                    v=1

if v==1:
    print("valid password>>>",pw)
    
else:
    print("Invalid Password>>>",pw)
