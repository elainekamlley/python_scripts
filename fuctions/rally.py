#rally.py
#We are going to write a program called "The Rally"

#It's a program written for an organizer who is putting together the rally, and it does a few things.
# (1)First it asks for the goal attendees, the current number of confirmed #attendees, and how many days are left until the rally.
#(2) Next, it cycles through the number of days and asks how many volunteers have been recruited each day.
#(3) Finally, when the days have run out, it checks to see if we have met our goal.
#=========================================================================

#(1) The ask_for_info function finds out the goal number, current number, and days left.
#	Name: asks_for_info
#	Inputs: 
#	Outputs: goals_attendees, confirmed_attendees, days_left

def ask_for_info():
	goal_attendees = input("How many people do you need at this rally? ")
	confirmed_attendees = input("How many people do you have confirmed? ")
	days_left = input("How many days are left till the rally? ")
	return [goal_attendees, confirmed_attendees, days_left]


#(2) The update numbers function asks how many people were recruited today, adds that to the total.
#	Name: update_numbers
#	Input: confirmed_attendees
#	Output: confirmed_attendees

def update_numbers(confirmed_attendees):
	print "\nOne more day passes....\n"
	confirmed_today = input("How many people did you recruit today? ")
	confirmed_attendees = confirmed_today+confirmed_attendees
	return confirmed_attendees

#(3) Function goal_is met checks to see if we have met, exceeded, or undershot our goal.
#Name: goal_is_met 
#Inputs:goal_attendees, confirmed_attendees
#Outputs: True/False (True if goal is met, Flase if its not)

def goal_is_met(confirmed_attendees,goal_attendees):
	estimated_attendees = float(confirmed_attendees)/2.00
	if estimated_attendees < float(goal_attendees):
		return False
	else:
		return True
 
#Test this function: print goal_is_met (800,400) 

#Here we check to see if that info is good enough!

organizer_answers = ask_for_info()
goal_attendees = organizer_answers[0]
confirmed_attendees = organizer_answers[1]
days_left = organizer_answers[2]


#Then, we check to see if that info is good enough!
are_we_there_yet = goal_is_met(confirmed_attendees, goal_attendees)

#Then, we print a message based on the outputfrom goal_is_met

if are_we_there_yet==True:
	print "Whoooohooo!!"
else:
	for day in range(1,days_left):
		confirmed_attendees=update_numbers(confirmed_attendees)
		print ""