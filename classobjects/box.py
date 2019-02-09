class box:
    width=0
    height=0
    area=0

    def __init__(self,w,h):
        self.width=w
        self.height=h
        self.area=w*h

    def show(self):
        print 'area of box is',self.area

    def __str__(self):
        return '%d %d %d' %(self.width,self.height,self.area)

b1=box(30,20)
b1.show()

print b1
