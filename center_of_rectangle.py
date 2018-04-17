"""program to find center of rectangle"""
class point:
    x=0
    y=0
    
class box:
    width=0
    height=0
    corner=point()
    
    def find_center(obj):
        cen=point()
        cen.x=obj.corner.x+obj.width/2
        cen.y=obj.corner.y+obj.height/2
        return cen
    
    
rect1=box()
rect1.width=200
rect1.height=100
rect1.corner.x=50
rect1.corner.y=100

print 'width=',rect1.width,'height=',rect1.height,'position=',rect1.corner.x,rect1.corner.y


center=rect1.find_center()
print 'center point of rectangle is=',center.x,center.y
