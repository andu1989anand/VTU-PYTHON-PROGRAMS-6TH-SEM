"""program to find center of rectangle"""
import copy
class point:
    x=0
    y=0
    
class box:
    width=0
    height=0
    corner=point()
    
       
    
rect1=box()
rect1.width=200
rect1.height=100
rect1.corner.x=50
rect1.corner.y=100
import copy
rect2=copy.deepcopy(rect1)
print 'width=',rect2.width,'height=',rect2.height,'position=',rect2.corner.x,rect2.corner.y

rect1.width=20
rect1.height=10
rect1.corner.x=5
rect1.corner.y=10
print 'width=',rect2.width,'height=',rect2.height,'position=',rect2.corner.x,rect2.corner.y
