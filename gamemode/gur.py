import os
from time import sleep, time


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
            return f"{round(playTime, 2)} {'seconds' if playTime > 1 else 'second'}"
        else:
            return f"{round(playtimeInMin, 2)} {'minutes' if playtimeInMin > 1 else 'minute'}"
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
