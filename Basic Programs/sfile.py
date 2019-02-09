while :
    fname=raw_input("enter a file name:")

    try:
        fd=open(fname)
    except:
        print "enter valid file name"
        continue
    print fd
    content=fd.read()
    print content
