#=========================== 
#fellowsloop.py  
#is a script prints "_____ is a Code For Progress fellow." to the screen for all 
# for all 2014 Code For Progress Fellows.  
#It uses a list of names (as strings) and a for loop to do that. 
#========================

#if ____ is a Code For Progress Fellow prints for each name in the list, pass

# Define a list that holds the names of all 2014 fellows as strings 
fellows = ["Terri", "Cassidy","Dago", "Jason", "Bobby Joe", "Aurea", "Kathy",
"Mariella", "Pam", "Selina", "Elaine", "Angie"]

#write a for loop through loop through the fellows list and print the desired
#sentence to the screen

for people in fellows:     
	print people + " is a Code For Progress Fellow"
	print people[0]

print people[-1]

#when you break off a print from the loop but still want to use the variable (people)
#when it exits the loop it remember the last name in the list. ex Dago 