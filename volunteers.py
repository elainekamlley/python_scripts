#Volunteers.py
#This script asks the user for their volunteer goal 
#and their current number of volunteer,
#Then, it check s to see whether or not you have met your goal
# and gives you the appropriate message, depending on the result
#of that check

#Section 1.
# Ask the user for the goal nunber of volunteers and store it as a vol_goal

vol_goals = input("What is your volunteer goal? ")

#You can add tests in the between like print vol_goals

#Section 2.
#Next, it asks for the current number of colunteers 
#and stores it as a current_volunteers

current_vol = input("How many current volunteers do you have now? ")

#Section 3. 
#If current_vol is greater than or equal to vol_goal, it prints "Awesome!"
#Otherwise it prints, "you betta work!"

if current_vol >= vol_goals:
	print "awesome!"
else: 
	print "you betta work!"