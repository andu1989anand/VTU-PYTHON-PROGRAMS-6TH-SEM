class timer:
    hr=0
    minn=0
    sec=34

    def __init__(self,h,m,s):
        self.hr=h
        self.minn=m
        self.sec=s
           
    def show(self):
        print 'TIME:',self.hr,':',self.minn,':',self.sec

t1=timer(3,45,34)

t1.show()
t2=timer(2,12,56)
t2.show()


