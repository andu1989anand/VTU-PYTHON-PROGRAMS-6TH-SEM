import string
ca=0
ce=0
ci=0
co=0
cu=0
cc=0

fd=open('verybig.txt')
for line in fd:
    line=line.lower()
    for c in line:
        cc+=1
        if c == 'a': ca+=1
        if c == 'e': ce+=1
        if c == 'i': ci+=1
        if c == 'o': co+=1
        if c == 'u': cu+=1
print "a,e,i,o,u,total characters"
print ca,ce,ci,co,cu,cc
