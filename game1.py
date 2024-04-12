# Given the initial position of a number of players (no limit on the number of players)
# and a destination position, at each turn each player can specify the horizontal and
# vertical movements with the goal to reach the destination.
# If after a specified number of turns no player has reached the destination the player
# closes to the destination wins.

from math import sqrt, inf
from random import randint

# Types,
type GameState = dict[str, tuple[int, int]]
type Position = tuple[int, int]

# Return random 2D coordinates.
def rand_coord(max_coord: int) -> tuple[int, int]:
    return (randint(-max_coord, max_coord), randint(-max_coord, max_coord))

# Compute the square of the distance between two points (Pythagora's theorem).
def distance_sq(a: Position, b: Position) -> float:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

# Compute the distamce between two points.
def distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    return sqrt(distance_sq(a, b))

# Check if a player has won by checking if the current position is same as destination.
def won(state: dict[str, tuple[int, int]], destination: tuple[int, int]) -> str:
    for name, position in state.items():
        if position == destination:
            return name
    return ""

# Initialise game state with random positions for players and destination.
def init_game_state(players:list[str], max_coord: int) -> GameState:
    state:GameState = dict()
    for p in players:
        state[p] = rand_coord(max_coord)
    return state

# Print current state: Players' positions, destination and number of turns left.
def print_state(state: GameState, destination: Position, turns_left: int) -> None:
    print()
    print("=" * 30)
    print(state)
    print("Turns left: " + str(turns_left))
    print(f"Destination: {destination}")
    for (player, position) in state.items():
        print(f"{player}'s distance from destination: {int(distance(position, destination))}")
    print("=" * 30)

# Validate input also verifying that the entered numbers are a pefect triple.
def check_input(line:str) -> bool:
    if len(line) == 0:
        return False
    l = str.split(line)
    if len(l) != 2:
        return False
    return True

# Return player input as (x,y) coordinate.
def get_player_input(player: str, position: Position, max_coord: int) -> Position:
    line = input(f"{player}>\nEnter movement along horizontal and vertical directions as two number 'x y': ")
    if not check_input(line):
        print("Input error, please enter two numbers between {-max_coord} and {+max_coord}")
        get_player_input(player, position, max_coord)
    l = list(map(int, str.split(line)))
    assert len(l) == 2
    return (l[0], l[1])

# Main function implementing the game logic.
def main(destination: Position, max_coord: int, max_number_of_turns: int):
    players = list(str.split(input("Enter the players' names separate by ','"), ','))
    # remove blank spaces
    players = list(map(str.strip, players))
    if len(players) < 2:
        print("Please enter at least two players")
        main(destination, max_coord, max_number_of_turns)
    state = init_game_state(players, max_coord)
    turns_left = max_number_of_turns
    while not won(state, destination) and turns_left > 0:
        print_state(state, destination, turns_left)
        for (player, position) in state.items():
            (new_x, new_y) = get_player_input(player, position, max_coord)
            state[player] = (position[0] + new_x, position[1] + new_y)
        turns_left -= 1

    player_won = won(state, destination)
    if player_won != "":
        print("Player " + player_won + " WON !!!")
    else:
        m = inf
        winner = ""
        for (player, position) in state.items():
            if distance_sq(position, destination) < m:
                winner = player
        print("Player " + winner + " WON")

# Entry point when invoked on the command line.
if __name__ == "__main__":
    max_coord = 800 # from -800 to +800 in x and y
    max_number_of_turns = 10
    destination = rand_coord(max_coord)
    main(destination, max_coord, max_number_of_turns)
