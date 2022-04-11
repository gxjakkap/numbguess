import os
import sys
from time import sleep, time
import requests


def strtobool(message: str) -> bool:  # take y/n string and returns boolean value
    lm = message.lower()
    if lm in ["y", "n"]:
        if lm == "y":
            return True
        elif lm == "n":
            return False
    else:
        return True  # default value always be y


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


def multiplayer(ans: int, playercount: int) -> None:
    # clear terminal screen and print out title
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============ Multiplayer ============")
    # create list to store data
    pans = []
    pdiff = []
    winners = []

    # gather players' guess
    for i in range(playercount):
        pinp = int(input(f"Player {i+1}, Enter your guess: "))
        if pinp < 1 or pinp > 100:
            print("Invalid Value")
            pans.append(9999)
        else:
            pans.append(pinp)

    # calculate players' diff
    for i in range(playercount):
        diff = abs(ans - pans[i])
        pdiff.append(diff)

    # store winners name
    for i in range(playercount):
        if pdiff[i] == 0:
            winners.append(f"Player {i+1}")

    # check if there's no winner, one winner, or multiple winners
    print("\n============== Results ==============")
    if len(winners) == 0:  # no winner
        print(f'No one win this round. The answer was "{ans}"\n')

    elif len(winners) == 1:  # one winner
        print(f'{"".join(winners)} wins this round. The answer was {ans}')

    else:  # multiple winners
        print(f'{", ".join(winners)} win this round. The answer was {ans}')

    # print out players' diff
    print("==== Scoreboard (Less is better) ====")
    for i in range(playercount):
        print(f"Player {i+1}: {'FFL' if pans[i]==9999 else pdiff[i]}")
    print("=====================================")
    return  # return to main function


def guessuntilright(ans: int) -> None:
    # print out recap
    def recap(t: int) -> None:
        print("\n=============== Recap ===============")
        for i in range(t):
            print(f"{i+1}. Guessed: {guesses[i]} Diff: {diffs[i]}")
    # calculate playtime and determine if it should be displayed in seconds or minutes

    def playtimeDisplay(st, et):
        playTime = endTime - startTime
        playtimeInMin = playTime / 60
        if playtimeInMin < 1:
            return f"{playTime}s"
        else:
            return f"{playtimeInMin}m"
    # clear terminal screen and print out title
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========= Guess until right =========")
    print("Rules: Guess until you get the number right.")
    i = 3
    while i > 0:  # print a countdown from 3
        print(i)
        sleep(1)
        i -= 1
    print("Go!")
    startTime = time()
    i = 0
    guesses = []
    diffs = []
    while(True):
        i += 1
        # gather player's guess
        playerinput = input("Enter your guess: ")
        # allow player to chicken out
        if playerinput == "ff":
            guesses.append("ff")
            diffs.append("ff")
            endTime = time()
            print("\n============== Results ==============")
            tot = "times" if i > 1 else "time"  # just to get the grammar right
            print(
                f"'You tried for {i} {tot}, took {playtimeDisplay(startTime, endTime)} and you can't guess the number {ans}.'")
            recap(i)
            return
        # push player's guess to the list
        guesses.append(playerinput)
        # try to convert input to int
        try:
            playerinput = int(playerinput)
        except:
            pass  # pass to let below if deal with it
        # check for invalid value
        if playerinput == "" or not isinstance(playerinput, int) or 0 > playerinput or 100 < playerinput:
            diffs.append("INVAL")
            print("Invalid Value!")
            continue  # continue at the start of the loop
        # calculate player's diff
        diff = abs(ans - int(playerinput))
        # check if player wins or not
        if diff == 0:  # wins
            diffs.append(f'{diff} Win!')
            endTime = time()
            break
        else:
            diffs.append(diff)
            print("Not yet!")
    # print out results
    print("\n============== Results ==============")
    tot = "tries" if i > 1 else "try"  # just to get the grammar right
    print(
        f"It took you {i} {tot} in {playtimeDisplay(startTime, endTime)} to guess the number {ans}")
    recap(i)
    return  # return to main function


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
        singleplayer(ans)

    elif mode == 2:  # multiplayer
        # gather playercount for multiplayer mode
        playercount = int(
            input("How many players is playing? (Limit: 5): "))
        if playercount <= 0:  # catch 0 or negative player input
            print("How the fuck are you playing with less than 1 player?")
            sys.exit(0)
        elif playercount == 1:  # send 1 player input to singleplayer mode
            print("Then choose singleplayer you idiot.")
            singleplayer(ans)
        elif 1 < playercount < 6:  # multiplater mode
            multiplayer(ans, playercount)
        else:  # >5 players is not allowed. i just dont feel like it
            print("I said the limit is 5. I don't like you you have too many friends.")
            sys.exit(0)

    else:  # guess until right
        guessuntilright(ans)

    # check if player wanna play again. if not then terminate process
    if not strtobool(str(input("Play again? [y/n]: "))):
        sys.exit(0)


def main() -> None:  # main process
    while(True):  # endless loop
        gameloop()


if __name__ == "__main__":
    main()
