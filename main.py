import os
import sys
import requests
import gamemode


def strtobool(message: str) -> bool:  # take y/n string and returns boolean value
    lm = message.lower()
    if lm in ["y", "n"]:
        if lm == "y":
            return True
        elif lm == "n":
            return False
    else:
        return True  # default value always be y


def gameloop() -> None:
    # clear terminal screen and print out title
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======= Number Guessing Game ========")
    print("Welcome to number guessing game.")

    # generate answer with random.org api which is a true random number service that generates randomness via atmospheric noise.
    r = requests.get(
        'https://www.random.org/integers/?num=1&min=1&max=100&format=plain&rnd=new&col=1&base=10')
    ans = int(r.text)

    # mode selection
    print("========== Choose game mode =========")
    print("== 1. Singleplayer                 ==")
    print("== 2. Multiplayer                  ==")
    print("== 3. Guess until right            ==")
    print("=====================================")
    mode = int(input("Which mode you gonna play in?: ")) or 1

    if mode < 1 and mode > 3:  # invalid value
        print("Invalid mode.")
        sys.exit(0)

    elif mode == 1:  # singleplayer mode
        gamemode.singleplayer(ans)

    elif mode == 2:  # multiplayer
        # gather playercount for multiplayer mode
        playercount = int(
            input("How many players is playing? (Limit: 5): "))
        if playercount <= 0:  # catch 0 or negative player input
            print("How the fuck are you playing with less than 1 player?")
            sys.exit(0)
        elif playercount == 1:  # send 1 player input to singleplayer mode
            print("Then choose singleplayer you idiot.")
            gamemode.singleplayer(ans)
        elif 1 < playercount < 6:  # multiplater mode
            gamemode.multiplayer(ans, playercount)
        else:  # >5 players is not allowed. i just dont feel like it
            print("I said the limit is 5. I don't like you you have too many friends.")
            sys.exit(0)

    else:  # guess until right
        gamemode.guessuntilright(ans)

    # check if player wanna play again. if not then terminate process
    if not strtobool(str(input("Play again? [y/n]: "))):
        sys.exit(0)


def main() -> None:  # main process
    while(True):  # endless loop
        gameloop()


if __name__ == "__main__":
    main()
