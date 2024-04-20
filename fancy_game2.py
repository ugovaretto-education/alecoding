# Given the initial position of a number of players (no limit on the number of players)
# and a destination position, at each turn each player can specify the horizontal and
# vertical movements with the goal to reach the destination.
# If after a specified number of turns no player has reached the destination the player
# closes to the destination wins.

# Add local direactory to PYTHONPATH to be able to load code from other files.
import sys
sys.path.insert(0,'.')

from math import sqrt, inf
from random import randint
from cartesian import * 
from pythagora import *

# Types,
type GameState = dict[str, tuple[int, int]]
type PlayerInput = tuple[int, int] # units and direction

# Check if a player has won by checking if the current position is same as destination.
def won(state: dict[str, tuple[int, int]], destination: tuple[int, int], min_dist: float = 0.0) -> str:
    for name, position in state.items():
        if distance(destination, position) <= min_dist:
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
        print()
        print(f"{player}'s distance from destination: {int(distance(position, destination))}")
        dydx = (destination[1] - position[1]) / (destination[0]-position[0])
        print(f"{player}'s gradient with destination: {dydx:.2f}")
        # (units, dir) = reverse_grad(position, destination)
        # print(f"{player}'s optimal move: {units} {dir}")
        for (player2, position2) in state.items():
            if player2 == player:
                continue
            mp = ((position[0] + position2[0])/2.0, (position[1] + position2[1])/2.0)
            print(f"{player} - {player2} midpoint = ({mp[0]:.2f}, {mp[1]:.2f})")
    print("=" * 30)

# Validate input also verifying that the entered numbers are a pefect triple.
def check_input(line:str) -> bool:
    if len(line) == 0:
        return False
    l = str.split(line)
    if len(l) != 2:
        return False
    l = list(map(int, str.split(line)))
    if len(l) != 2:
        return False
    if l[1] < 1 or l[1] > 8:
        return False
    if l[0] <= 0:
        return False
    return True

# Return player input as (x,y) coordinate.
def get_player_input(player: str) -> PlayerInput:
    line = input(f"{player}>\nEnter units of movements and directions(1-8) as two numbers separated with space': ")
    if not check_input(line):
        print("Input error, please enter two numbers separated by space")
        get_player_input(player)
    l = list(map(int, str.split(line)))
    return (l[0], l[1])

# Main function implementing the game logic.
def main(destination: Position, max_coord: int, max_number_of_turns: int):
    X = 40 # column
    Y = 40 # row
    grid = gen_grid(X, Y)
    sd = scale(destination, (-800, -800), (800, 800), (0,0), (40, 40))
    grid = set_grid_elem(- sd[0], sd[1], 'D', grid)
    print("Generating Pythagorean triples...")
    triples = generate_triples(127, 2000)
    players = ["player1", "player2"]
    state = init_game_state(players, max_coord)
    turns_left = max_number_of_turns
    while not won(state, destination) and turns_left > 0:
        print_state(state, destination, turns_left)
        for (player, position) in state.items():
            (units, direction) = get_player_input(player)
            # Retrieve triple with hypotenuse having length closest to units
            abc = closest_triple(triples_dict(triples), units) 
            print(f"Triple: {abc[0]}, {abc[1]}, {abc[2]}")
            # Map triangle sides to x,y coordinates depending on direction
            (dx, dy) = ab_to_xy((abc[0], abc[1]), direction)
            print(f"Movement: ({dx}, {dy})")
            sp = scale(position, (-800, -800), (800, 800), (0,0), (40, 40))
            grid = set_grid_elem(Y - sp[0], sp[1], '.', grid)
            # Move player
            state[player] = (position[0] + dx, position[1] + dy)
        turns_left -= 1
        for (player, position) in state.items():
            sp = scale(position, (-800, -800), (800, 800), (0,0), (40, 40))
            grid = set_grid_elem(Y - sp[0], sp[1], player[-1], grid)
        
        print_grid(grid)
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
