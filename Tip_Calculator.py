'''This is a simple Tip + Meal Calculator. This was created as a personal project to develop funadamental skills
in Python Programming Language'''

name = raw_input("What was the name of the resturant that you visited?") #Ask user for resturant name.
meal = raw_input("What was the value of your meal excluding taxes") #Ask user for value of meal w/o taxes.
tax = raw_input("What is the Tax in your location?") #Ask user for value of tax in their area.
totalwtax = float(meal) + float(meal) * float(tax) #Calculate total value of meal with tax.
tip = raw_input("How was the service on a scale of 1 to 5?") #Ask for level of service.

value = float(tip)

if value == float(1) or value == float(2): #If serivce was within 1 & 2
    print float(totalwtax) + float(meal) * 0.15
if value >= float(3) and value <= float (5): #If service was within 3 & 5
        print float(totalwtax) + float(meal) * 0.50
else:
    print "Remember this is a scale of 1 to 5! Please try again!"
