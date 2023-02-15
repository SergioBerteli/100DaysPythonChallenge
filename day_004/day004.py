import random


def main():
    choices = ["Rock", "Paper", "Scissors"]
    choice = None
    if choice is None:
        while choice is None:
            try:
                choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
            except ValueError:
                print("Please select a valid option")

    compute_choice = random.choice(range(3))
    print(f"You choose {choices[choice]} and  the computer choose {choices[compute_choice]}")

    match = {choices[choice]: 'player', choices[compute_choice]: "computer"}
    if compute_choice == choice:
        print("its a draw!")
        return
    elif "Rock" in match and "Paper" in match:
        winner = match['Paper']
    elif "Rock" in match and "Scissors" in match:
        winner = match['Rock']
    else:
        winner = match['Scissors']
    print(f'\nThe winner is the {winner}')


if __name__ == '__main__':
    main()
