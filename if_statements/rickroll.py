#rickroll.py 
# This is a script cleaning a phone number input and tracks any errors.

#Section 1
#This section is the import the string package to use on the for loop
import string

#Section 2
#This section allows the user to input their phone number

phone = raw_input("Your number: " )

#print phone <--Test 1

#Section 3 
#This section will track punctuations and take them out

for number in phone:
	if number in string.punctuation or number in string.ascii_letters:
		phone = phone.replace(number,"")
		
#Section 4
#This section measures the length of the phone to equal 10
if len(phone)==10:
	print phone
else:
	print "false"



