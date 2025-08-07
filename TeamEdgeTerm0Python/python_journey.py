# Journey Challenge:
# Create your own survival story by being creative in your story telling and create ways of surviving your simulation!
# Input at least 10 key-value pairs in your new dictionary and have more than 2 tool to help you survive!
# Make sure the conditions match with the bad and good decision making behind the template!

# BONUS: Create a functions within the program to make it more efficient and clean!


# dictionary for the tools
dress = {
  "ragged old dress": "A",
  "short mini skirt": "B",
  "simple brown drop dress": "C",
  "derby gown": "D"
}




print("Welcome to the princess path \n")
print("------------------------------------------------------------------------")
print("You're currently the princess in a very strict kingdom. You must be proper") 
print("WHAT DRESS WILL YOU WEAR. Apperences are veryy importent") 

values = dress.values()

# Get all key-value pairs
items = dress.items()

# Print each key-value pair
for key, value in items:
  print(f"{value}: {key}")


print("Choose your option")
userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
userList = list(userChoices.split(','))

# create a variable that holds on to the correct amount of tools needed to win the game
correctItems = 1

# each condition where if the right items aren't chosen, you describe the reason why you need it
if "D" not in userList:
  print("You have died")


# condition where you will the right choices were there BUT there are other options that were chosen
if "A" in userList:
  print("Your childhood bullies see you in this dress. While bullying you, they knock you off the balcony \n")
  # nested condition where you will win the game if you have the right tools 
if "B" in userList:
  print("Your dress is too scandolous for high society. An old conservative duchess decides to slap you in FACE \n")
if "C" in userList:
  print("The dress is too boring, you have been forgotten \n")

if "D" in userList:
    print("Congrats you have passed this test and is shocked by your new look. Look at you trend-setter\n")
    print("======= YOU WON THE FIRST TRAIL=======")
    print("You must choose a husband") 
    print("WHAT husband will you choose.") 
    husbands= {
  "Bakery Boy, he throws pennies at you hoping to catch you're line of sight": "A",
  "Prince, he offers your family a large dowry, but he cheats": "B",
  "Archmage, he controls the magic tower but is completely insane": "C",
  "Knight, just came back from the Great War, is plotting to overthrow the kingdom": "D"
}
    values= husbands.values()
    items = husbands.items()
    for key, values in items:
      print(f"{values}: {key}")
      print("Choose your option")
      userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
      userList = list(userChoices.split(','))
      correctItems2 = 1
    if "D" not in userList:
        print("You have died")
        # condition where you will the right choices were there BUT there are other options that were chosen
    if "A" in userList:
          print("Your family hunts you for marrying a commoner. Sucks to suck\n")
    if "B" in userList:
          print("You live a life of luxury but the princes mistresses poison your tea. \n")
    if "C" in userList:
          print("The archmage ignores you and you rott unfortunately \n")
    if "D" in userList:
       print("Congrats you have passed this test and you are now the new queen with a decent husband\n")
       print("======= YOU WON =======")
    else:
       print("u lost")

else:
  print("Try again, press play again, don't move foward\n")





