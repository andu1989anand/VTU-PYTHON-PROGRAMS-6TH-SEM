"""
Program to copy all lines beginning with vowels
from input.txt file to vowel.txt file retaining the other lines
"""


v=('a','e','i','o','u')
fname=input("enter a file name:")
fd=open(fname,'r')
for line in fd:
    line=line.lower()
    if line.startswith(v):
        fw=open("output.txt",'a')
        fw.write(line)
        fw.close()
    
