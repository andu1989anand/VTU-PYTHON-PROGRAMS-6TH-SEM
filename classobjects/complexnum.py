"""program to add two complex numbers"""
class complex:
    real=0
    img=0
    
    def __init__(self):
        real=0
        img=0
    
    def __init__(self,r,i):
        self.real=r
        self.img=i

    def show(self):
        print "complex number=",self.real,'+i',self.img

    def add(self,n1):
        n3=complex(0,0)
        n3.real=self.real+n1.real
        n3.img=self.img+n1.img
        return n3

    def __add__(self,n1):
        n3=complex(0,0)
        n3.real=self.real+n1.real
        n3.img=self.img+n1.img
        return n3


c1=complex(22,55)
c1.show()
c2=complex(45,90)
c2.show()
c3=c1.add(c2)
c3.show()

c4=c1+c2
c4.show()

