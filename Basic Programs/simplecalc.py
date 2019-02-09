while True:
    n1=input("enter a number:")
    n2=input("enter another number:")
    op=raw_input("enter a operator")
    if op=='+':
        print "answer=",n1+n2
    elif op=='-':
        print "answer=",n1-n2
    elif op=='*':
        print "answer=",n1*n2
    elif op=='/':
        print "answer=",n1/n2
    elif op=='%':
        print "answer=",n1%n2
    elif op=='**':
        print "answer=",n1**n2
    else:
        print "enter valid operator"
    res=input("\n\n\n1.quit\n2.continue\n\n")
    if res==1: exit(0)
    else:
        continue
    
