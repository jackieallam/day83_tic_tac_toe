import os
import random
import art


class Game:
    def __init__(self, start_player):
        self.markers = [" "] * 9
        self.positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.winning_rows = ((1, 2, 3),
                             (4, 5, 6),
                             (7, 8, 9),
                             (1, 4, 7),
                             (2, 5, 8),
                             (3, 6, 9),
                             (1, 5, 9),
                             (3, 5, 7))
        self.move_count = 0
        self.starting_player = start_player

    def display_board(self, marks):
        """ Displays the current game board as well as a guide to choose a position. """
        os.system("clear")
        print(art.title)
        print("Enter a number corresponding to the game as follows: \n")
        print("     |     |     " + "              " + "     |     |      ")
        print("  1  |  2  |  3  " + "              " + f"  {marks[0]}  |  {marks[1]}  |  {marks[2]}  ")
        print("_____|_____|_____" + "              " + "_____|_____|_____")
        print("     |     |     " + "              " + "     |     |     ")
        print("  4  |  5  |  6  " + "              " + f"  {marks[3]}  |  {marks[4]}  |  {marks[5]}  ")
        print("_____|_____|_____" + "              " + "_____|_____|_____")
        print("     |     |     " + "              " + "     |     |     ")
        print("  7  |  8  |  9  " + "              " + f"  {marks[6]}  |  {marks[7]}  |  {marks[8]}  ")
        print("     |     |     " + "              " + "     |     |     \n")

    def choose_position(self, player):
        """Asks user for a position, or chooses a random one if playing against computer.
        Returns the position as an integer."""
        invalid = "Please enter a valid position."
        if player.name == "Computer":
            return random.choice(self.positions)
        else:
            # Test if input is a valid position
            while True:
                try:
                    chosen_position = int(input(f"{player.name}, enter position: "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    if chosen_position in self.positions:
                        return chosen_position
                    else:
                        print(invalid)

    def update_board(self, pos, marker):
        """Takes a position and active marker as arguments. Places the active player's marker onto the game board at
         given position and displays the updated board."""
        # Update game board with marker at specified position
        self.markers[pos - 1] = marker
        self.positions.remove(pos)
        self.move_count += 1
        self.display_board(self.markers)

    def check_for_win(self, player):
        """ Checks for any completed winning row. """
        for row in self.winning_rows:
            # Check if all positions in any winning row are filled by current player's marker
            if all(player.marker == self.markers[position - 1] for position in row):
                return True
