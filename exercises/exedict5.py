fname=raw_input("enter a file name:")
fd=open(fname)
email=dict()
for line in fd:
    if line.startswith('From:'):
        line=line.split()
        e=line[1]
        pos=e.find('@')
        domain=e[pos+1:]
        if domain not in email:
            email[domain]=1
        else:
            email[domain]+=1

print email
