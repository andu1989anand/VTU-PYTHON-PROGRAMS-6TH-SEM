class student:
    name=' '
    usn=0

    
def read(s):   
    print 'enter student name and usn'
    s.name=raw_input('enter name')
    s.usn=raw_input('enter usn')

def show(s):
    print 'name=',s.name,'usn=',s.usn

s2=student()
read(s2)
show(s2)
