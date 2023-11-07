import random

while True:
    choices = ["rock", "paper", "scissor"]

    user = None

    while user not in choices:
        user = input("rock, paper or scissor?: ").lower()

    system = random.choice(choices)  # Move this inside the while loop

    if user == system:
        print("system: ", system)
        print("user: ", user)
        print("Tie!!")

    elif user == "rock":
        if system == "paper":
            print("system: ", system)
            print("user: ", user)
            print("You Lost!!!")
        elif system == "scissor":
            print("system: ", system)
            print("user: ", user)
            print("You Won!!!")

    elif user == "paper":
        if system == "scissor":
            print("system: ", system)
            print("user: ", user)
            print("You Lost!!!")
        elif system == "rock":
            print("system: ", system)
            print("user: ", user)
            print("You Win!!!")

    elif user == "scissor":
        if system == "rock":
            print("system: ", system)
            print("user: ", user)
            print("You Lost!!!")
        elif system == "paper":
            print("system: ", system)
            print("user: ", user)
            print("You Won!!!")
    continue
    # play_again = input("Play Again? (y/n): ").lower()
    #
    # if play_again != "y":
    #     break

print("End of Program. Bye!!!")
