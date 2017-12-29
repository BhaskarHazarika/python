#Difference between print and sys.stdout.write()-- no spaces
import sys
x = raw_input("Type any thing here: ")
for item in ['one','is',1]: 
    print str(item) + str(x),  # comma suppresses newline

for item in ['one','is',str(1)]: # must explicitly convert to strings
    y = str(item) + str(x)
    sys.stdout.write(y)  # no spaces!