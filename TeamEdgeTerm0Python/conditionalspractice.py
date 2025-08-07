age = int(input("What is your age"))
#the conditional after if must be a statement
if age >=16 :
    #the executed is here (could be a function inside)
    print ("You are eligble")
else:
    print("you are not eligible")

if age >=16 : 
    print("get a job")
elif age<=16:
    print("you should go outside")


#if
#elif
#else
#if none of the if and ifel statments are met the last else will execute

#UNO GAME
points = int()
color= input("What is the color of your card")
symbol = input("What is the symbol of your card")
number = input("What is the number on your card")
ogcolor = "red"
ognumber = 10
ogsymbol= "clubs"
if sorted(ogsymbol) == sorted(symbol):
    if sorted(ogcolor) == sorted (color):
