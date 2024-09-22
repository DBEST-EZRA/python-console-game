def make_decision(prompt, choices):
    while True:
        print(prompt)
        for index, choice in enumerate(choices, 1):
            print(f"{index}. {choice}")
        try:
            selection = int(input("Choose an option: "))
            if 1 <= selection <= len(choices):
                return choices[selection - 1]
        except ValueError:
            print("Invalid input. Please enter a number.")


def game_loop():
    print("Welcome to the Adventure Game!")

    # First loop
    decision1 = make_decision("You find a fork in the road. What do you do?", ["Go left", "Go right"])
    if decision1 == "Go left":
        print("You encounter a river.")
        decision2 = make_decision("Do you swim across or walk along the bank?", ["Swim", "Walk along the bank"])
    else:
        print("You enter a forest.")
        decision2 = make_decision("Do you climb a tree or keep walking?", ["Climb", "Keep walking"])

    # Second loop
    decision3 = make_decision("You hear a strange sound. What do you do?", ["Investigate", "Ignore it"])
    print(f"Your choices: {decision1}, {decision2}, {decision3}")
    print("The adventure continues...")


def main():
    while True:
        game_loop()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")


main()

