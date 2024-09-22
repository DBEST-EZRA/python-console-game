def make_a_decision(prompt, options):
    while True:
        print(prompt)
        for index, option in enumerate(options, 1):
            print(f"{index}. {option}")
        try:
            your_choice = int(input("Select an option "))
            if 1 <= your_choice <= len(options):
                return options[your_choice - 1]
        except ValueError:
            print("Your choice is not valid! ")


def first_option():
    first_decision = make_a_decision("What do you do when you find a diverging road", ["Go to the left", "Go to the right"])
    if first_decision == "Go left":
        print("Ahead of you there is a pond.")
        second_decision = make_a_decision("Do you swim across or walk alongside?", ["Swim across", "Walk alongside the pond"])
    else:
        print("You enter a fruit yard")
        second_decision = make_a_decision("Do you pick a fruit or keep exploring?", ["Pick a fruit", "Keep exploring"])
    return first_decision, second_decision


def second_option():
    decision3 = make_a_decision("You hear a lion roar, do you hide or ignore it?", ["Hide", "Ignore the sound"])
    return decision3


def final_option():
    decision4 = make_a_decision("You find an abandoned pet. What do you do?", ["Take it Home", "Leave it there"])
    if decision4 == "Take it Home":
        print("You have a kind heart buddy")
    else:
        print("You leave it there, keep exploring")
    return decision4


def game_loop():
    print("Its play time")
    first_decision, second_decision = first_option()
    third_decision = second_option()
    fourth_decision = final_option()
    print(f"This is a summary of your choices: {first_decision}, {second_decision}, {third_decision}, {fourth_decision}")



def main():
    while True:
        game_loop()
        replay = input("Replay? (yes/no): ").lower()
        if replay == "no":
            print("Thank you for participating")
            break
        elif replay == "yes":
            continue
        else:
            print("invalid input")
main()


