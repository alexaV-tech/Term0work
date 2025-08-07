# import random
# x= int(input("What would you like to be your max number "))


# def get_user_guess(maxNum):
#     answer =int(input(f"guess a number from 1 through {maxNum} ") )
#     return answer

# def generate_random_number(maxNum):
#     count=0
#     secret=random.randint(1,maxNum)
#     while True:
#         guess = get_user_guess(maxNum)
#         if count < 4:
#             if 1<= guess <=maxNum:
#                 if guess ==secret :
#                     print("You guess it")
#                     break
#                 else:
#                     count+=1
#                     print("Try again")
#             else:
#                 print("YOUR GUESS IS OUT OF RANGE")
#         else :
#             print(f"You have failed. The number was {secret}")

# generate_random_number(x)


def count_spaces(text):
    count=0
    for letters in text:
        if(letters)== " ":
            count+=1
    print(count)

count_spaces("He llo ")


def charater_count(text):
    count=0
    for letters in text:
        count+=1
    print(count)


charater_count("Hello")

def upperCase(text):
    count=0
    for letters in text:
        if letters.isupper():
            count+=1
    print(count)

upperCase("HEllo")


def upperCase(text):
    count=0
    for letters in text:
        if letters.islower():
            count+=1
    print(count)

upperCase("HEllo")

def numOfVowels(text):
    count=0
    vowels = "aeiouAEIOU"
    for letters in text:
        if letters in  vowels:
            count+=1
    print(count)

numOfVowels("ARE")









