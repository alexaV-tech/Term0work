option1= input("Player 1 enter your choice")
option2= input("Player 2 enter your choice")
def game_simulation (choice1, choice2):
    #path 0
    if choice1 == choice2 :
        print("Its a tie")
        return "game over"
    #path 1
    if choice1 =="rock" and choice2 =="scissor":
        print("player 1 wins")
    elif choice1=="rock" and choice2 =="paper":
        print("player 2 wins")
    #path 2   
    if choice1 == "paper" and choice2== "rock":
        print("Player 1 wins")
    elif choice1 =="paper" and choice2== "scissor":
        print("Player 2 wins")
    #path 3
    if choice1=="scissor" and choice2== "paper":
        print("Player 1 wins")
    elif choice1=="scissor" and choice2=="rock":
        print("Player 2 wins")
    return "game over"
game_simulation(option1, option2)

#.lower() <-- to make it open to muliple respones