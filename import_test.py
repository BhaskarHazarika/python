def print_table(multiplier):
	print "--- Printing the %d times table ---" % multiplier
	for n in range(1,13):
		print "%d x %d = %d" % (n, multiplier, n*multiplier)

#	>>> on cmd prmpt
#	>>> import import_test
#   >>> import_test.print_table(12)	