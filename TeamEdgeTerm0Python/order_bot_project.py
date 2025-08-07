# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 




# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------


def drinksOrder():
	total=0
	drinks= {
		"coca-cola $5":"A",
		"margarita $13":"B",
		"coffee $7":"C",
		"water $0":"D"
	}
	values = drinks.values()
	items= drinks.items()
	for key, value in items:
		print(f"{value}: {key}")

	print("Choose your option")
	userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
	userList = list(userChoices.split(','))

	if "A" in userList:
		total+=5
	if "B" in userList:
		total+=13
	if "C" in userList:
		total+=7
	if "D" in userList:
		total+=0
	return total



def meals():
	total=0
	meal= {
		"chicken tender $5":"A",
		"hamburger $13":"B",
		"spagetti $7":"C",
		"sandwich $15":"D"
	}
	values = meal.values()
	items= meal.items()
	for key, value in items:
		print(f"{value}: {key}")

	print("Choose your option")
	userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
	userList = list(userChoices.split(','))

	if "A" in userList:
		total+=5
	if "B" in userList:
		total+=13
	if "C" in userList:
		total+=7
	if "D" in userList:
		total+=15
	return total

def desserts():
	total=0
	dessert= {
		"chocolate $5":"A",
		"waffle $13":"B",
		"icecream $7":"C",
		"lavacake $15":"D"
	}
	values = dessert.values()
	items= dessert.items()
	for key, value in items:
		print(f"{value}: {key}")

	print("Choose your option")
	userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
	userList = list(userChoices.split(','))

	if "A" in userList:
		total+=5
	if "B" in userList:
		total+=13
	if "C" in userList:
		total+=7
	if "D" in userList:
		total+=15
	return total

total =drinksOrder()+meals()+desserts()
tax= 0.05*total 
tip= 0.15*total
print("here is your total", total)
print("here is your tax", tax)
print("here is your tip price", tip)










# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 
# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------


  




# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------












# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 












# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 




# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
