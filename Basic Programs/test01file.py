linecount=0
linesubject=0

fd=open("verybig.txt")
for line in fd:
    linecount=linecount+1
    if line.startswith("subject:"):
        linesubject=linesubject+1
print "number of lines in this file:",linecount
print "number of lines starts with subject:",linesubject
