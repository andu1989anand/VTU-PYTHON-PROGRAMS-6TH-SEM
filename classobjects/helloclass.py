class hello:
    msg='welcome to my class hello'

    def show(self,n):
        print n,self.msg

name=raw_input("enter your name:")
h1=hello()
h1.show(name)
