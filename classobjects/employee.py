class emp:
    name=' '
    salary=0
    totalemp=0
    dept=' '
    
    def __init__(self,n,s):
        self.name=n
        self.salary=s
        emp.totalemp+=1
        self.dept='Marketing'

    def displaycount(self):
        print 'total employee',emp.totalemp

    def displayemp(self):
        print 'name:',self.name,'salary:',self.salary,'dept:',self.dept

e1=emp('kumar',45000)
e1.displayemp()

e2=emp('ravan',10000)
e2.displayemp()
e2.displaycount()
