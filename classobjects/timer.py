class timer:
    hr=0
    minn=0
    sec=0
    
    def add(self,t1,t2):
        t3=timer()
        t3.hr=t1.hr+t2.hr
        t3.minn=t1.minn+t2.minn
        t3.sec=t1.sec+t2.sec
                
        if t3.sec>=60:
            t3.sec=t3.sec-60
            t3.minn=t3.minn+1

        if t3.minn>=60:
            t3.minn=t3.minn-60
            t3.hr=t3.hr+1
    
        return t3

t1=timer()
t1.hr=2
t1.minn=30
t1.sec=54

t2=timer()
t2.hr=5
t2.minn=45
t2.sec=10

t3=timer()
t3=t3.add(t1,t2)

print t1.hr,':',t1.minn,':',t1.sec
print t2.hr,':',t2.minn,':',t2.sec
print t3.hr,':',t3.minn,':',t3.sec



