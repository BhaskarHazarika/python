# First open the file to read(r)
inp = file("menu.txt","r")
# read the file into a list then print
# each item
for line in inp.readlines():
	print line, str(1)
#noe close it again
inp.close()


#2nd approch	
# First open the file to read(r)
inp = open("menu.txt","r")
# iterate over the file printing each item
for line in inp:
    print line, str(2)
# Now close it again
inp.close()

#2nd approch	
# First open the file to read(r)
inp = open("menu.txt","r")
# iterate over the file printing each item
for line in inp:
    print line.rstrip(), str(3)
# Now close it again
inp.close()