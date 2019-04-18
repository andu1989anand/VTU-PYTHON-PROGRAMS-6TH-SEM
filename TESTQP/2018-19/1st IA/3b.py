sen=input("enter a sentence")
maxx=None;
words=sen.split()
for w in words:
        if maxx is None:
            maxx=w
        elif len(w)>len(maxx):
            maxx=w

print("longest word=",maxx,"length=",len(maxx))

"""
OUTPUT:
enter a sentencemit mysore is a very good place, all the departments are working good
longest word= departments length= 11
"""
