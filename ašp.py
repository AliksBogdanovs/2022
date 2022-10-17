import random

CHOICES = 'ašp'


def get_player_choice():
    """Saņemt lietotāja ievadi un apstiprināt to ir viena no iepriekš minētajām iespējām"""
    player_choice = None
    while player_choice is None:
        player_choice = input('Choices: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            player_choice = None
    return player_choice.lower()


def get_computer_choice():
    """Lieciet datoram pēc nejaušības principa izvēlēties vienu no derīgajām izvēlēm"""
    computer_choice = random.randint(0, 2)
    computer_choice = CHOICES[computer_choice]
    return computer_choice


def is_draw(player_choice, computer_choice):
    """Pārbaudiet, vai spēle bija neizšķirta"""
    if player_choice == computer_choice:
        return True


def print_winner(player_choice, computer_choice):
    """Pārbaudiet, lai redzētu, kurš uzvarēja"""
    if player_choice == 'r' and computer_choice == 's':
        print('Spēlētājs uzvar!')
    elif player_choice == 's' and computer_choice == 'p':
        print('Spēlētājs uzvar!')
    elif player_choice == 'p' and computer_choice == 'r':
        print('Spēlētājs uzvar!')
    else:
        print('Dators uzvar!')
        print('%s beats %s' % (computer_choice, player_choice))


def play_game():
    """spēle spēli"""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if is_draw(player_choice, computer_choice):
        print("Tas ir neizšķirts, abi spēlētāji izvēlējās %s: " % player_choice)
    else:
        print("Dators izvēlēts: %s" % computer_choice)
        print("Spēlētājs izvēlēts: %s" % player_choice)
        print_winner(player_choice, computer_choice)


if __name__ == "__main__":
    play_game()
