filee=raw_input("enter a file name:")
try:
    fd=open(filee)
except:
    print "enter valid file name"
    exit()
for l in fd:
    l=l.rstrip()
    if l.find('professor')==-1:
        continue
    print l
