#This is a simple Tip + Meal Calculator

name = raw_input("What was the name of the resturant that visited?")
meal = raw_input("What was the value of your meal excluding taxes")
tax = raw_input("What is the Tax in your location?")
totalwtax = meal + meal * tax
tip = raw_input("How was the service on a scale of 1 to 5?")

print name
print totalwtax

tip = raw_input("How was the service on a scale of 1 to 5?")
value = str(tip)

if value == 1 or value == 2:
    print totalwtax + meal * 0.15
    
if value == 3 or value == 4:
    print totalwtax + meal * 0.30

else:
    print totalwtax + meal * 0.50


