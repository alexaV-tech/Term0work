# # -------------------------------------------- 

# 	# You've just learned all about functions. 
# 	# Now take what you've learned to create your own

# 					# CALCULATOR!

# 	# We'll guide you through the first few steps,
# 	# then you'll have a chance to add your own features
# 	# that will make this your new go-to calculator!

#   # -------------------------------------------- 

# print("My Simple Calculator")

# # -------------------------------------------- 

# # Part 1: 

# 	# The first features of any simple calculator is that
# 	# it should be able to perform the basic math operations. 
# 	# Let's start by writing the functions we'll need to execute 
# 	# the following operations:

# 		# Addition
# 		# Subtraction

# # -------------------------------------------- 

# # Write a function called add_numbers that will take two numbers and return the sum.

# def add_numbers(num1,num2):
#      sum = num1+num2
#      print(sum)

# add_numbers(3,2)



# # Write a function called sub_numbers that will take two numbers and return the difference.

# def sub_numbers(num1,num2):
#      diff= num1-num2
#      print(diff)

# sub_numbers(3,2)



# # ------------
# # Testing Code - Uncomment the code below to test your code!

# add_numbers(5, 15)
# add_numbers(3, 18)
# add_numbers(12, 28) 


# sub_numbers(11, 9)
# sub_numbers(18, 21)

# # -------------------------------------------- 

# # Part 2: 

# 	# Now that you have addition and subtraction down, let's add the other operators we learned!

# 	# Finish off your basic calculator by writing the functions 
# 	# for the following operations:

# 		# Multiplication
# 		# Division 

# # -------------------------------------------- 

# # Write a function called multiply_numbers that will take two numbers and return the product.

# def multiply_numbers(num1,num2):
#      product= num1*num2
#      print(product)





# # Write a function called divide_numbers that will take two numbers and return the quotient.

# def divide_numbers(num1,num2):
#      div= num1/num2
#      print(div)




# # ------------
# # Testing Code - Uncomment the code below to test your code!

# multiply_numbers(10, 3)
# multiply_numbers(21, 7)
# multiply_numbers(4, 16)

# divide_numbers(24, 100)
# divide_numbers(21, 7)
# divide_numbers(15, 4)
# # -------------------------------------------- 

# # Part 3: 

# 	# Now that you have your basic functions in place, you need to get some user input.
# 	# What's a calculator for if no one is using it?

# # Write a function that will prompt the user for the operation they want to call and the values they are inputting.

# # -------------------------------------------- 

# x= input("What type of operation do you want to call, +, -, *, / :")
# number1= int(input("Enter the first number"))
# number2= int(input("Enter the second number"))
# def operator(usage,input1,input2):
#      if(usage=="+"):
#           add_numbers(input1,input2)
#      elif(usage=="-"):
#           sub_numbers(input1,input2)
#      elif(usage=="*"):
#           multiply_numbers(input1,input2)
#      else:
#           divide_numbers(input1,input2)
           
# operator(x,number1, number2)


# def modulas (num1,num2):
#      print(num1%num2)
# modulas(3,4)


          















# -------------------------------------------- 

# Part 4: 

	# Now that you have all of the basic four operations completed, you get to add your own features!
	# What will you add to make this your go-to calculator? 

	# Stuck? : Think about what you count/calculate on a (almost) daily basis.
	# Can you write a function that will take in the data you need and do the calculation for you? 

	# (I know I calculate how many hours of sleep I get every day... ｡(*^▽^*)ゞ )

# -------------------------------------------- 

# Write a function or functions that will add some unique features to your calculator. 
# Don't forget to:
		# Give your function an name and parameters that are self explanatory and written in camelcase!
		# Use comments throughout your code
		# Test your code!
  
# -------------------------------------------- 


# info = {"name": "Alexa", "age": 17, "pets": "zuzu", "status":"slightly tired", "favword":"fatous"}
# print(info["name"], "is great")
# print("Hello my name is", info["name"], "I am", info["age"], "years old. I have a pet named", info["pets"], "who can be very", info["favword"])

# #a dictionary inside of a dictionary, there is barely any ()
# info2= {"family": {"mother": "floriberta", "father": "maurino"}}

celeb = {"name":"Naruto Uzumaki", "family":{"mother": "Kushina Uzumaki", "father":"Minato Namikaze"}, "position": "Konohagakure's Hokage", "power":"Kurama the Nine-Tailed Fox " }
print(celeb["name"], "is an orphan who has a dangerous fox-like entity known as",celeb["power"],"sealed within his body by his father,", celeb["family"]["father"], ".",celeb["name"], "dreams of becoming", celeb["position"])


# foods= {"apples": "pears", "bears": "meet"}
# #before the ':' key
# #after is the corresponding guest
# #they are paired

# #accessing
# fruit = foods["apples"]
# print(fruit)

# #updating
# foods["apples"] = "banana"
# print(foods["apples"])
# length= len(foods)

# #to delete the key
# del foods["apples"]


#set is curly
#tulple is ()







my_dict={"name": "alice", "age":15}
update= {"city":"Ny", "age":20}
my_dict.update(update)
print(my_dict)
#this combines while also replacing













# -------------------------------------------- 
# Ignore this section. This is just for checking your work

# def check_answers(gen_answer, correct_answer):
#     if gen_answer == correct_answer:
#         print("Your code works!")
#     else:
# 	    print(f"Try again, your code generated {gen_answer} but the correct answer is {correct_answer}")