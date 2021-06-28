import random

while True:

    options=['rock','paper','scissor']
    user_action=input("Enter your choice (rock/paper/scissor):")
    print("You selected: ",user_action)
    computer_action=random.choice(options)
    print("The computers choice is: ",computer_action)

    if user_action==computer_action:
        print("Player and Computer selected same Options. Its a tie")

    elif user_action=='rock':
        if computer_action=='scissor':
            print("You win, Computer loses ! Rock beats the scissor.")
        else:
            print("Computer wins, You lose ! Paper covers the rock.")

    elif user_action=='paper':
            if computer_action=='rock':
                print("You win, Computer loses ! Paper covers the rock.")
            else:
                print("Computer wins, You lose ! Scissor cuts the paper.")

    elif user_action=='scissor':
                if computer_action=='rock':
                    print("Computer wins, You lose ! Rock beats the scissor.")
                else:
                    print("You win, , Computer loses ! Scissor cuts the Paper.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
