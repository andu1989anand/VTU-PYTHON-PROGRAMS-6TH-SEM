"""type based dispatch"""

class box:
    width=0
    height=0
    area=0

    def __init__(self,w,h):
        self.width=w
        self.height=h
        self.area=w*h
       
    def show(self):
        print 'area of box is',self.width*self.height
    
    def __add__(self,other):
        if isinstance(other,box):
            return self.addbox(other)
        else:
            return self.increment(other)

    def addbox(self,other):
        return self.area+other.area

    def increment(self,other):
        self.width=self.width+other
        self.height+=other

b1=box(30,20)
b1.show()
b2=box(45,23)
b2.show()
print b1+b2
b1+100
b1.show()




