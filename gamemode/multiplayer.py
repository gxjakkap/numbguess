
import os


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
