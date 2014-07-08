#name_function.py
#This is a program called "Name" and its going to print a name in three different ways
#Its a program written to do a few things with an user's first name, middle #name, middle name, and last name.
#	(1) It first asks a person's name
#	(2) It then does three functions:
#		-Their full name, with no middle name (Elaine Kamlley)
#		-Their first and middle initials followed by their last name (E.M. Kamlley)
#		-Their last name followed by first name (Kamlley, Elaine)
#=================================================================

#Section 1: Function Definitions:
#================================
#The ask_info_function finds out the first name, middle name, and last name.
#	Name: ask_for_info
#	Input:
#	Output: first, middle, last name

def ask_for_info():
	first_name= raw_input("What is your first name? ")
	middle_name= raw_input("What is your middle name? ")
	last_name= raw_input("What is your last name? ")
	return [first_name, middle_name, last_name]

full_name = ask_for_info()


#(2a) In this section it will print the full name, with no middle name (ex Elaine Kamlley)
#	Name: name_nomiddle 
#	Input full name
#	Output: first_name and last_name

def no_middle(full_name):
	no_middle = full_name[0]+" "+full_name[2]
	return no_middle


#(2b) Their first and middle initials followed by their last name (E.M. Kamlley)
#	Name: initial_name
#	Input:full_name
#	Output: first and middle initial along with the last name

def initial(full_name):
	initial = full_name[0][0]+". "+full_name[1][0]+". "+full_name[2]
	return initial

#(2c) Their last name followed by first initial (Kamlley, E.)
#	Name: bond_name
#	Input: full_name
#	Output: last_name, first_name

def bond_name(full_name):
	bond_name = full_name[2]+", "+full_name[0][0]+"."
	return bond_name


#Section 3 Test Cases
#===============================================
test_case_1 = no_middle(full_name)
print test_case_1

test_case_2 = initial(full_name)
print test_case_2

test_case_3 = bond_name(full_name)
print test_case_3