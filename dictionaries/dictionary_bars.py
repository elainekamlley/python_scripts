#dictionary_bars.py

#(1) Define three DC restaurants/bars as dictionary items with 4 keys: name, type of food, neighborhood, and wheather #or not it is open for lunch. 

first_dine = {'name': 'the pig', 'type': 'New American','neighborhood': 'Logan Circle', 'lunch':False}
second_dine = {'name': 'Pho 14', 'type': 'Vietnamese','neighborhood': 'Adams Morgan', 'lunch': True}
third_dine = {'name': 'Mellow Mushroom', 'type': 'Pizza','neighborhood': 'Adams Morgan', 'lunch':True }
fourth_dine = {'name': 'Tryst', 'type': 'American','neighborhood': 'Adams Morgan', 'lunch':True }

#(2) Put those restaurants into a list.

restaurants = [first_dine, second_dine, third_dine, fourth_dine]

#(3) Use a for loop to iterate through the list of restaurants and print out its name

#for x in restaurants:
	#print x['name']

#(4) Use a for loop to iterate through the list of restaurnts and print out its neighborhood

#for x in restaurants:
	#print x['neighborhood']

#(5) Challenge: Use a for loop to iterate through the list of restaurants and prints its name if it is open for lunch

#for x in restaurants:
#	if x['lunch'] == True:
#		print x['name']

#(6) Challenge 2: Use a for loop to print out
	#_[name]_ is open for lunch

for x in restaurants:
	if x['lunch'] == True:
		print x['name'] + " is open for lunch"