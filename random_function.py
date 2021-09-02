from random import randint
hands = ["rock", "paper", "scissor"]
computer = hands[randint(0,2)]
player = False

while player == False:
    player = input("Choose your choice among rock, paper, scissors")

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("You lose!")
        else:
            print("You win!")
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = hands[randint(0, 2)]
