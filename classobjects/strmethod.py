class timer:
    hr=0
    minn=0
    sec=0
    
    def __init__(self,h,m,s):
        self.hr=h
        self.minn=m
        self.sec=s
    
    def __str__(self):
        return '%d : %d : %d' %(self.hr,self.minn,self.sec)

t1=timer(2,30,54)

t2=timer(5,34,23)

print t1.hr,':',t1.minn,':',t1.sec
print t2.hr,':',t2.minn,':',t2.sec

print 'using __str__ method'

print t1
print t2

