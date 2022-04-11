import os


def singleplayer(ans: int) -> None:
    # clear terminal screen and print out title
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=========== Singleplayer ============")

    # gather player's guess
    playerinput = int(input("Enter your guess: "))
    if playerinput < 1 and playerinput > 100:
        print("Invalid Value")
        print(f"You lose. The answer was {str(ans)}.")

    # calculate player's diff
    diff = abs(ans - playerinput)

    # check if player wins or not
    if diff == 0:
        print(f"You win! the answer was indeed {str(ans)}.")
    else:
        print(f"You lose. You were {str(diff)} off from {str(ans)}.")
    return  # return to main function
