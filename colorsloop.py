#====================
#colorsloop.py
#Developer: Elaine Kamlley
#This scrip prints out colors using one list definition and one for loop:
#Test 1: if script prints ____ is a color, and it's pretty, then pass
#Test 2: if script print "The last color I thought was pretty was Green" last, then pass
#=====================

colors = ["Red", "Blue", "Yellow", "Green"]

for each_color in colors:
	print each_color + " is a color, and it's pretty."
#print "The last color I thought was pretty was " + colors[3]. you can use either the list (color) or the loop variable (each_color)
print "The last color I thought was pretty was " + each_color
