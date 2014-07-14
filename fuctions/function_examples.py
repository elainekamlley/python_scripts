# function_examples.py
# A page of example functions

#Define the function
#def excitify(word): #name(input)
#	new_word = word+"!"
#	boring_word = word+"..."
#	return boring_word, new_word #output

#Call the function

#print excitify("flowers")


#Define the function

def volume_calculator(height, width, length):
	volume = height*width*length
	return volume

def area_calculator(width, length):
	area = width*length
	return area

#Call the function
room_area = area_calculator(20,6)
room_volume = volume_calculator(10,20,6)

print "The volume of this room is "+ str(room_volume)+ " cubic feet."
print "The area of this room is "+ str(room_area)+ " square feet."