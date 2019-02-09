"""1. Write a program to open the file and read it line by line. For each line split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the word is not in the list add it to the list.When the program completes, sort and print the resulting words in  alphabetical order."""


fname=raw_input("enter a file name:")
fd=open(fname)
words=[]
for line in fd:
    line=line.lower()
    line=line.split()
    for word in line:
        if word not in words:
            words.append(word)

print words
print 'sorted list is:'
words.sort()
print words
