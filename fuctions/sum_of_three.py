#sum_of_three.py
#This function takes in three integers as inputs and outputs the total of the three integers. 
#Note: This is an example of passing inputs into the function
#==========================================


#Section 1 Functon Definitions
#=============================	
#This function will pass in three integer then print the total of the three integers.
#	Name: sum_of_three
#	Inputs: Three integers 
#	Outputs: The the total of the three integers (as an integer)

def sum_of_three(a,b,c):
	total = a+b+c
	return total

#This function will pass in three integers then print the product of the three
#	Name: product_of_three
#	Input: Three numbers as integers
#	Output: product of the three integer (as an integer)

def product_of_three(x,y,z):
	total = x*y*z 
	return total

#The full_name function will pass in two inputs, one first name and one last name both as strings
#and then returns a string contains the full name
#	Name: full_name
#	Input: two words that are names as strings, first_name, last_name
#	Output: full_name (as a string)

def full_name(first_name, last_name):
	full_name = first_name+" "+last_name
	return full_name 

#The nick_name_adder function will pass in two inputs, one first name, one last name both and a nickname as strings
#and then returns the full name with nickname in the middle.
#	Name: nick_name
#	Input: two words that are names as strings, first_name, last_name, nick_name
#	Output: nick_name (as a string)

def nick_name_adder(first_name, nick_name, last_name):
	nick_name = first_name+" "+nick_name+" "+last_name
	return nick_name

#The make_initial function which takes a string as an input and returns a string containing
#that word's first letter followed by a period. So, for example, if I passed in the input
#"Frodo", it would return 'F'
#	Name: make_initial
#	Input: name (as a string)
#	Output: initial (as a string)

def make_initial(word):
	initial = word[0] + "."
	return initial


#Section 2: Test Cases
#====================
#test_case_1 will call the sum_of_three function and passing in the integers 7,8,9
#print its results

test_case_1 = sum_of_three(7,8,9)

print test_case_1	


#test_case_2: calling the sum_of_three function, "pass in" the integers 21,3,5 and 
#store the output to the variable titled test_case_2. Then, print test_case_2

test_case_2 = sum_of_three(21,3,5)

print test_case_2

#test_case_3 will call the sum_of_three function, pass in 41,-2,0 store the output to the
#variable called test_case_3, and print the output.

test_case_3 = sum_of_three(41,-2,0)
print test_case_3

#test_case_4: calling the sum_of_three function, pass in inputs 15,15,5 store the output to the
#test_case_4 variable then print

test_case_4 = sum_of_three(15,15,5)
print test_case_4

#test_case_5: calling the product_of_three function, pass in inputs 2,4,5 stores the output to the 
#test_case_5 variable then print.

test_case_5 = product_of_three(2,4,5)
print test_case_5

#test_case_6: calling the product_of_three function, pass in inputs 5,6,7. Store and print the 
#output.

test_case_6 = product_of_three(5,6,7)
print test_case_6

#test_case_7: calling the sum_of_three, passes the info stored from test case 1-3, then prints.

test_case_7 = sum_of_three(test_case_1, test_case_2, test_case_3)
print test_case_7

#test_case_8: callign the product_of_three, passes the info stored from test_case_1-3, then prints.

test_case_8 = product_of_three(test_case_1, test_case_2, test_case_3)
print test_case_8

#test_case_9: calling the full_name function, "Aurea" as the first_name and "Martinez" as the
#last_name. Store the output then print it.

test_case_9 = full_name("Aurea","Martinez")
print test_case_9

#test_case_10: calling the full_name function, "Bayard" as the first name and "Rustin" as the 
#last_name. Store the output then print it.

test_case_10 = full_name("Bayard","Rustin")
print test_case_10

#test_case_11: calling the nick_name_adder, "Elaine" as the first name, "NotAMuggle" as the nick_name,
#and "Elaine" as the last name. Store the output then print it.

test_case_11 = nick_name_adder("Elaine","NotAMuggle","Kamlley")
print test_case_11

#test_cast_12: calling the nick_name_adder, giving it "Jason" as a first_name, "SnapChatLies"
#as a middle_name, and "Towns" as a last_name.

test_case_12 = nick_name_adder("Jason","SnapChatLies","Towns")
print test_case_12

#test_case_13: calling the make_initial function, passing "Beyonce" as a word. Store it
#and then print the first initial. 

test_case_13 = make_initial("Beyonce")
print test_case_13