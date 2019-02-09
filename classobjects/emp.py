class complex:
    real=0
    img=0

    def show(self):
        print self.real,"+i",self.img

    def __init__(self,r,i):
        self.real=r
        self.img=i

    def __mul__(self,other):
        c3=complex(0,0)
        c3.real=self.real*other.real
        c3.img=self.img*other.img
        return c3
    
    def __div__(self,other):
        c3=complex(0,0)
        c3.real=self.real/other.real
        c3.img=self.img/other.img
        return c3


c1=complex(33,45)
c1.show()

c2=complex(44,99)
c2.show()

c4=c1*c2
c4.show()

c5=c1/c2
c5.show()

