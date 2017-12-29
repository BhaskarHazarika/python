import time
# Create daily menu based on MENU.TXT
# First open the files to read(r) and write(w)
inp = open(r"C:/Projects/python/menu.txt","r")
outp = open(r"C:/Projects/python/menu.prn","w")


#Create today's day string
today = time.localtime(time.time())
theDate = time.strftime("%A %B %d", today)

#Add banner text and a blank line
outp.write("Menu for %s\n\n" % theDate)

#Copy each line of menu.txt to new file
for line in inp:
	outp.write(line)

print "Menu create for %s...\n" % theDate


#Now close the files
inp.close()
outp.close()


#testing to append in file
error_msg = "This is an error msg"
err = open(r"C:/Projects/python/menu.prn","a")
err_msg = err.write(error_msg)
print "Error Printed im menu.prn on %s" % theDate
err.close()
