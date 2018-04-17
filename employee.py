"""display employee details"""
class emp:
    totalemp=0
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        emp.totalemp+=1

    def displaycount(self):
        print 'total employee',emp.totalemp

    def displayemp(self):
        print 'name:',self.name,'salary:',self.salary

e1=emp('raj',50000)
e1.displayemp()

e2=emp('ravan',10000)
e2.displayemp()
e2.displaycount()
