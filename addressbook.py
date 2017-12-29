
#Loading the Address book
filename = "addressbook.dat"

def readBook(book):
	import os
	if os.path.exists(filename):
		store = open(filename,"r")
		for line in store:
			name = line.rstrip()
			entry = store.next().rstrip()
			book[name] = entry
		store.close()	


#Saving the address book
def saveBook(book):
	store = open(filename,"w")
	for name,entry in book.items():
		store.write(name + '\n')
		store.write(entry + '\n')
	store.close()


#Get user input
def getChoice(menu):
	print menu
	choice = int(raw_input("Select a choice 1-4): "))
	return choice

#Adding an entry
def addEntry(book):
	name = raw_input("Enter a name: ")
	entry = raw_input("Enter street, town and phone number: ")
	book[name] = entry


#Removing an entry
def removeEntry(book):
	name = raw_input("Enter a name: ")
	del(book[name])

#Finding an entry
def findEntry(book):
	name = raw_input("Enter a name: ")
	if name in book:
		print name, book[name]
	else: print "Sorry, no entry for: ", name	


#Quitting the program	
def main():
	theMenu = '''
	1) Add Entry
	2) Remove Entry
	3) Find Entry
	4) Quit and save
	'''
	theBook = {}
	readBook(theBook)
	choice = getChoice(theMenu)
	while choice != 4:
		if choice == 1:
			addEntry(theBook)
		elif choice == 2:
			removeEntry(theBook)
		elif choice == 3:
			findEntry(theBook)
		else: print "Invalid choice, try again"
		choice = getChoice(theMenu)
		saveBook(theBook)


#the python magic
if __name__ == '__main__':
	main()    		




