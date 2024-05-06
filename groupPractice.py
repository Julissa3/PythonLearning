dietaryrestrictions = input("Do you have any dietay restrictions?")
if dietaryrestrictions == "yes":
    type = (input("What kind?"))
else:
    print("Thank you.")
if type == "Vegetarian":
    print("You can eat a salad.")
elif type == "gluten-free":
    print("You can eat gluten-free pasta")
elif type == "nut-free":
    print("You can eat a burger")
meal = input("What meal would you like? ")
print("The meal fits your preference")
payment = (input("Do you have a payment plan? "))
if payment == "yes":
    print("its been successfully paid.")
else:
    amount = int(input("Enter the amount of payment "))

outside = input("Would you like to go outside? ")
outside = True
if outside:
    print("You can go eat at the picnic table.")
else:
    print("Stay inside")
