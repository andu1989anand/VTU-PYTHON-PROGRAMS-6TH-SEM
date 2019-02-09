fname=raw_input("enter a file name:")
fd=open(fname)
email=dict()
for line in fd:
    if line.startswith('From:'):
        line=line.split()
        e=line[1]
        if e not in email:
            email[e]=1
        else:
            email[e]+=1

print email

maxx=0
maxemail=' '
for k in email:
    if email[k]>maxx:
        maxx=email[k]
        maxemail=k
        
print maxemail,maxx
