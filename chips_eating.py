#chips_eating.py

#Section 1: Set out current values

chips_in_bag = 30
print "There are "+ str(chips_in_bag)+ " chips in the bag."


#Section 2: Inside a while loop, ask the user how many chips they want to eat until the bag is gone.
#Ask the user how many chips they want to eat a time, until the bag is gone. When the 
#bag is empty, print "The bag is empty!"

while chips_in_bag > 0:
	chips_ate = input("How many chips do you want to eat?: ")
	chips_in_bag = chips_in_bag - chips_ate
	print "\n (Munching Sounds) \n"
	print "There are "+ str(chips_in_bag)+ " chips in the bag."
print "The bag is empty. sad."