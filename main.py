from player import Player
from game import Game
import art
import os


def game_intro():
    """ Displays the game intro and provides a choice of 1 or 2 player game. """
    print(art.title)
    print("Welcome to Tic Tac Toe.\n")
    while True:
        amount = input("One or Two Player game? (Type 1 or 2): ")
        if amount in ["1", "2"]:
            break
        else:
            print("Sorry, that's not a valid number.")
            continue
    return int(amount)


def set_player_names(num_players):
    """ Get names of players and assign markers for each. Adds computer as 2nd player if 1 Player selected.
    Returns the list of 2 players. """
    markers = ["X", "O"]
    players_list = []
    for n in range(num_players):
        new_player = Player(input(f"Player {markers[n]}, what is your name? "), markers[n])
        players_list.append(new_player)
    if num_players == 1:
        computer_player = Player("Computer", markers[1])
        players_list.append(computer_player)
    return players_list


def display_scores(heading):
    """ Display the current player scores taking a header as an argument. """
    print(heading)
    for player in players:
        print(f"{player.name}: {player.score}")
    print(f"Ties: {draw_count}")
    print("\n")


def play_again():
    """ Checks if players wish to continue. """
    while True:
        next_game = input("Would you like to play again? Y/N ").upper()
        if next_game in ["Y", "N"]:
            if next_game == "N":
                os.system("clear")
                print(art.title)
                display_scores("\nFinal scores:")
                print("\nThank you for playing! Goodbye.")
                return False
            else:
                return True
        else:
            print("Please enter only Y or N.")
            continue


how_many_players = game_intro()

# Initialize players and their states
players = set_player_names(how_many_players)
starting_player = players[0]
non_start_player = players[1]
active_player = starting_player
passive_player = non_start_player
draw_count = 0
session_active = True

while session_active:

    game_over = False

    game = Game(starting_player)
    game.display_board(game.markers)
    print(f"{game.starting_player.name} starts!")

    # Reset active player according to new starting player
    active_player, passive_player = starting_player, non_start_player

    while not game_over:
        position = game.choose_position(active_player)
        game.update_board(position, active_player.marker)

        if game.check_for_win(active_player):
            print(f"{active_player.name} is the winner!")
            active_player.score += 1
            game_over = True
        elif game.move_count == 9:
            print("It's a draw!")
            draw_count += 1
            game_over = True
        if game_over:
            display_scores("\nCurrent scores:")

        # Switch active player for turns
        active_player, passive_player = passive_player, active_player

    # Switch starting player for new game
    starting_player, non_start_player = non_start_player, starting_player

    if not play_again():
        session_active = False
