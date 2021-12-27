import random

print("1 = Rock")
print("2 = Paper")
print("3 = Scissors")
print("4 = Lizard")
print("5 = Spock")


def get_player_choice():

    choice = int(input("What is your choice ?: "))
    if choice > 5:
        print("Invalid number please try again....")
        get_player_choice()
    elif choice < 1:
        print("Invalid number please try again....")
        get_player_choice()
    elif choice == 1:
        print("You picked Rock")
    elif choice == 2:
        print("You picked Paper")
    elif choice == 3:
        print("You picked Scissors")
    elif choice == 4:
        print("You picked Lizard")
    elif choice == 5:
        print("You picked Spock")
    return choice


def get_computer_choice():

    choice = random.randint(1, 5)
    if choice == 1:
        print("Computer picked Rock")
    elif choice == 2:
        print("Computer picked Paper")
    elif choice == 3:
        print("Computer picked Scissors")
    elif choice == 4:
        print("Computer picked Lizard")
    elif choice == 5:
        print("Computer picked Spock")
    return choice


def winner(player_choice, computer_choice, player_wins, computer_wins, ties):

    if player_choice == 1 and computer_choice == 3 or computer_choice == 4:
        print("Player won !!!")
        player_wins.append(1)
    elif player_choice == 2 and computer_choice == 1 or computer_choice == 5:
        print("Player won !!!")
        player_wins.append(1)
    elif player_choice == 3 and computer_choice == 2 or computer_choice == 4:
        print("Player won !!!")
        player_wins.append(1)
    elif player_choice == 4 and computer_choice == 2 or computer_choice == 5:
        print("Player won !!!")
        player_wins.append(1)
    elif player_choice == 5 and computer_choice == 1 or computer_choice == 3:
        print("Player won !!!")
        player_wins.append(1)
    elif player_choice == computer_choice:
        print("It's a tie!")
        ties.append(1)
    else:
        print("Computer won !!!")
        computer_wins.append(1)
    return


def game_total(player_wins, computer_wins, ties):

    player_wins = sum(player_wins)
    computer_wins = sum(computer_wins)
    ties = sum(ties)
    print("Player final score: ", player_wins)
    print("Computer final Score: ", computer_wins)
    print("Total ties: ", ties)


def main():

    player_wins = []
    computer_wins = []
    ties = []
    continuation = 'y'
    while continuation == 'y':
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner(player_choice, computer_choice, player_wins, computer_wins, ties)
        continuation = input("Would you like to play again (y/n):").lower()
        if continuation == 'n':
            print("Printing final scores.")
            break
    game_total(player_wins, computer_wins, ties)


main()
