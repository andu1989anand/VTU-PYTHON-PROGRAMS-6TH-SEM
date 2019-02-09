
try:
    temp=input("enter temperature in celsius:")
    tcel=float(temp)
    tfahr=tcel*1.8+32
    print "temperature in Fahrenheit is:",tfahr
except:
    print "enter a valid temperature"
    
