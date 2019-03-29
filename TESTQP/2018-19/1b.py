""" Construct a program which repeatedly prompts the user for numbers until the user enters “done”. 
Once “done” is entered print out total, count and average of the numbers also handle the exception. """


lst=list()
count,sum=0,0
while True:
    try:
        
        inp=input("enter a number:")
        if inp=='done':
            print ("count=",count)
            print ("sum=",sum)
            print ("avg=",sum/count)
            break
        else:
            
            sum=sum+float(inp)
            count=count+1
    except:
        print ("enter valid input")

"""
OUTPUT:
enter a number:1
enter a number:2
enter a number:3
enter a number:fff
enter valid input
enter a number:ggg
enter valid input
enter a number:ddd
enter valid input
enter a number:done
count= 3
sum= 6.0
avg= 2.0
"""
