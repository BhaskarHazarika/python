menu = """
Pick a shape(1-3):
1) Square
2) Rectangle
3) Triangle

4) Quit
"""
shape = int(raw_input(menu))
while shape != 4:
	if shape == 1:
		length = float(raw_input("Length: "))
		print "Area of square = ", length ** 2
	elif shape == 2:
		length = float(raw_input("Length: "))
		width = float(raw_input("Width: "))
		print "Area of rectanglr = ", length * width
	elif shape == 3:
		length = float(raw_input("Length: "))
		width = float(raw_input("Width: "))
		print "Area of triangle = ", length * width / 2
	else:
		print "Not a valid shape, try again"
		shape = int(raw_input(menu))	

