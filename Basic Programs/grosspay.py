def computepay(h,r):
    if h>40:
        return h*r*1.5
    else:
        return h*r


hour=input("enter hours")
rate=input("enter rate")
result=computepay(hour,rate)
print 'gross pay=',result
