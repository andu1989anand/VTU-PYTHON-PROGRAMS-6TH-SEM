filee=raw_input("enter a file name:")
try:
    fd=open(filee)
except:
    print "enter valid file name"
    exit()
c=fd.read()
f=c.find('anand')
print f

