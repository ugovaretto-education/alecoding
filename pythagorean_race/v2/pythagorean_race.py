import pygame  # Engine for Visual Mathematical Modeling
import sys  # Allows exiting of the app
import random  # Generates random coordinates
import math  # sqrt

# Pythagorean triples (a,b,c) where c = sqrt(a*a + b*b)
triples = [
    [3, 4, 5],
    [5, 12, 13],
    [8, 15, 17],
    [7, 24, 25],
    [20, 21, 29],
    [12, 35, 37],
    [9, 40, 41],
    [28, 45, 53],
    [11, 60, 61],
    [33, 56, 65],
    [16, 63, 65],
    [48, 55, 73],
    [13, 84, 85],
    [36, 77, 85],
    [39, 80, 89],
    [65, 72, 97],
    [20, 99, 101],
    [60, 91, 109],
    [15, 112, 113],
    [44, 117, 125],
    [88, 105, 137],
    [17, 144, 145],
    [24, 143, 145],
    [51, 140, 149],
    [85, 132, 157],
    [119, 120, 169],
    [52, 165, 173],
    [19, 180, 181],
    [57, 176, 185],
    [104, 153, 185],
    [95, 168, 193],
    [28, 195, 197],
    [133, 156, 205],
    [84, 187, 205],
    [21, 220, 221],
    [140, 171, 221],
    [60, 221, 229],
    [105, 208, 233],
    [120, 209, 241],
    [32, 255, 257],
    [23, 264, 265],
    [96, 247, 265],
    [69, 260, 269],
    [115, 252, 277],
    [160, 231, 281],
    [161, 240, 289],
    [68, 285, 293],
    [207, 224, 305],
    [136, 273, 305],
    [25, 312, 313],
    [75, 308, 317],
    [204, 253, 325],
    [36, 323, 325],
    [175, 288, 337],
    [180, 299, 349],
    [225, 272, 353],
    [27, 364, 365],
    [76, 357, 365],
    [252, 275, 373],
    [135, 352, 377],
    [152, 345, 377],
    [189, 340, 389],
    [228, 325, 397],
    [40, 399, 401],
    [120, 391, 409],
    [29, 420, 421],
    [87, 416, 425],
    [297, 304, 425],
    [145, 408, 433],
    [203, 396, 445],
    [84, 437, 445],
    [280, 351, 449],
    [168, 425, 457],
    [261, 380, 461],
    [31, 480, 481],
    [319, 360, 481],
    [93, 476, 485],
    [44, 483, 485],
    [155, 468, 493],
    [132, 475, 493],
    [217, 456, 505],
    [336, 377, 505],
    [220, 459, 509],
    [279, 440, 521],
    [308, 435, 533],
    [92, 525, 533],
    [341, 420, 541],
    [33, 544, 545],
    [184, 513, 545],
    [165, 532, 557],
    [396, 403, 565],
    [276, 493, 565],
    [231, 520, 569],
    [48, 575, 577],
    [368, 465, 593],
    [240, 551, 601],
    [35, 612, 613],
    [105, 608, 617],
    [336, 527, 625],
    [429, 460, 629],
    [100, 621, 629],
    [200, 609, 641],
    [315, 572, 653],
    [300, 589, 661],
    [385, 552, 673],
    [52, 675, 677],
    [37, 684, 685],
    [156, 667, 685],
    [111, 680, 689],
    [400, 561, 689],
    [185, 672, 697],
    [455, 528, 697],
    [260, 651, 701],
    [259, 660, 709],
    [333, 644, 725],
    [364, 627, 725],
    [108, 725, 733],
    [407, 624, 745],
    [216, 713, 745],
    [468, 595, 757],
    [39, 760, 761],
    [481, 600, 769],
    [195, 748, 773],
    [273, 736, 785],
    [56, 783, 785],
    [432, 665, 793],
    [168, 775, 793],
    [555, 572, 797],
]

pygame.init()  # starts the engine/program
app_clock = pygame.time.Clock()  # sets the refresh rate

print(
    """Welcome to the pythagorean triples movement game!
2  players will be placed randomly on an imaginary cartiesian plane.
You will take turns moving towards your destination, by entering the amount
of units and direction to move
The player that reaches the end destination first wins!
There is a distance buffer of 10, so players will only need to be within that
amount units of the destination to win"""
)


# Open window
def create_app_window(width, height):
    print(
        f"\n The plane goes from -{width/2} to {width / 2}"
        + " in both the x and y directions"
    )
    pygame.display.set_caption(
        "Pythagorean Race"
    )  # Email me with a suggestion of what we should name this app/game.
    app_dimensions = (
        width + 10,
        height + 10,
    )  # to give a bit of margin. -400 to 400 both ways
    app_surf = pygame.display.set_mode(
        app_dimensions
    )  # create the main display surface for us to draw on
    app_surf_rect = (
        app_surf.get_rect()
    )  # get a rectangle with important coordinates of the display surface.
    return (
        app_surf,
        app_surf_rect,
    )  # so that they can be used outside the function. At the moment they are
    # local variables


# Render surface
def app_surf_update(destination, player_one, player_two):
    # fill the display surface with white background colour
    app_surf.fill("white")

    # draw the x-axis and the y-axis
    # pygame.draw.line() needs the display surface to draw on, colour of the
    # line, starting coordinates and ending coordinates
    pygame.draw.line(
        app_surf,
        "grey",
        (0, app_surf_rect.height / 2),
        (app_surf_rect.width, app_surf_rect.height / 2),
        width=1,
    )
    pygame.draw.line(
        app_surf,
        "grey",
        (app_surf_rect.width / 2, 0),
        (app_surf_rect.width / 2, app_surf_rect.height),
        width=1,
    )

    # draw destination
    # pygame.draw.circle() needs the surface to draw on, colour, coordinates,
    # circle radius and line width
    pygame.draw.circle(
        app_surf, "black", destination["pygame_coords"], radius=3, width=3
    )

    # draw player one and player two
    pygame.draw.circle(
        app_surf, player_one["colour"], player_one["pygame_coords"], radius=3, width=2
    )
    pygame.draw.circle(
        app_surf, player_two["colour"], player_two["pygame_coords"], radius=3, width=2
    )


# Redraw window.
def refresh_window():
    # refresh the screen with what we drew inside the app_surf_update()
    # function
    pygame.display.update()
    app_clock.tick(24)  # tell pygame to refresh the screen 24 times per second


# Convert cartesian coordinates to window coordinates.
def conv_cartesian_to_pygame_coords(x, y):
    # pygame's coordinate system has the origin at the top left corner which
    # is weird (they have good reasons for this)
    # x values increase to the right and y values increase going DOWN which
    # is backwards! we need to move the x coordinate to the center which is
    # easy - just add half a window width
    # for the y coordinate, we need to first negate it, then move it down half
    # a window height
    pygame_x = x + app_surf_rect.width / 2
    # y coordinates grow from top to bottom and therefore the y coordinate
    # needs to be inverted
    pygame_y = -y + app_surf_rect.height / 2
    # return the 'weird' coordinates that pygame can use
    return (pygame_x, pygame_y)


MAX_COORD = 400

def initialise_entities():
    # initially set the requested coordinates to random values
    # each time you call randint() you get new random coords
    p1_rand_x, p1_rand_y = random.randint(-MAX_COORD, MAX_COORD), random.randint(-MAX_COORD, MAX_COORD)
    player_one["cartesian_coords"] = (
        p1_rand_x,
        p1_rand_y,
    )  # store the random cartesian coordinates
    player_one["pygame_coords"] = conv_cartesian_to_pygame_coords(
        p1_rand_x, p1_rand_y
    )  # convert and store pygame coordinates

    p2_rand_x, p2_rand_y = random.randint(-MAX_COORD, MAX_COORD), random.randint(-MAX_COORD, MAX_COORD)
    player_two["cartesian_coords"] = (p2_rand_x, p2_rand_y)
    player_two["pygame_coords"] = conv_cartesian_to_pygame_coords(p2_rand_x, p2_rand_y)

    dest_rand_x, dest_rand_y = random.randint(-MAX_COORD, MAX_COORD), random.randint(-MAX_COORD, MAX_COORD)
    destination["cartesian_coords"] = (dest_rand_x, dest_rand_y)
    destination["pygame_coords"] = conv_cartesian_to_pygame_coords(
        dest_rand_x, dest_rand_y
    )
    # no need to return entities. They are dictionaries so the function can
    # modify them directly (see the Python Functions tutorial on
    # Connect Notices)


# ********** MAIN PROGRAM ************* #

MAX_BUFFER_RADIUS = 10

destination_buffer = MAX_BUFFER_RADIUS 
player1_buffer = MAX_BUFFER_RADIUS
player2_buffer = MAX_BUFFER_RADIUS


player_one = {
    "name": "Player One",
    "cartesian_coords": None,  # not set yet. 'None' is special in Python.
    "pygame_coords": None,
    "colour": "red",
    "distance_from_dest": None,
    "midpoint": None,
    "gradient": None,
    "space_buffer": player1_buffer,
}

player_two = {
    "name": "Player Two",
    "cartesian_coords": None,
    "pygame_coords": None,
    "colour": "blue",
    "distance_from_dest": None,
    "midpoint": None,
    "gradient": None,
    "space_buffer": player2_buffer,
}

destination = {
    "name": "Destination",
    "cartesian_coords": None,
    "pygame_coords": None,
    "colour": "black",
    "current_coords": None,
    "space_buffer": destination_buffer,
}

# Print information about player.
def print_status(player):
    print()
    print(player["name"])
    (x, y) = player['cartesian_coords']
    print(f"Location: ({x}, {y})")
    print(f"Distance to destination: {player['distance_from_dest']:.1f} units")
    print(f"Gradient: {player['gradient']:.1f}")
    (x, y) = player['midpoint']
    msg = f"Midpoint with Player Two: ({x:.1f},{y:.1f})"
    if player["name"] == "Player Two":
        msg = f"Midpoint with Player One: ({x:.1f},{y:.1f})"
    print(msg)


# create the app window
app_surf, app_surf_rect = create_app_window(800, 800)
# these two are now global variables that everyone can access
initialise_entities()

print("\nThree entities initialised... here is a raw printout of their dictionaries")
print(destination)
print(player_one)
print(player_two)
print("\nLEFT click inside the window to make player ONE move")
print("RIGHT click inside the window to make player TWO move")
print(
    "You might need to first click the window to select it, then L/R click to make a move"
)


# Convert triple list to dict with key equal to the hypotenuse and value equsl
# to the other two sides of a right triangle.
def triples_dict(triples: list[tuple[int, int, int]]) -> dict[int, tuple[int, int]]:
    d = dict()
    for t in triples:
        d[t[2]] = (t[0], t[1])
    return d


# Given a number returns the triple with the hypotenuse length closest to the
# passed number.
def select_triple(
    triples: dict[int, tuple[int, int]], min_dist: int
) -> tuple[int, int, int]:
    hyps = list(triples.keys())  # extract hypotenuse lenghts
    dist = map(
        lambda i: abs(i - min_dist), hyps
    )  # compute distance between each hypotenuse length and passed values
    # find the index of the item with minimum distance

    index = min(enumerate(dist), key=lambda x: x[1])[0]
    # return closest triple matching hypotenuse length
    c = hyps[index]
    return (triples[c][0], triples[c][1], c)


# Given a number returns the triple with the hypotenuse length closest to the
# passed number.
def select_triple_simple(
    triples: dict[int, tuple[int, int]], dist: int
) -> tuple[int, int, int]:
    mindist = 600  # assign the maximum value do the minimum distance variable
    t = (0, 0, 0)  # initialise the tuple to return
    for hypothenuse, (a, b) in triples.items():
        d = abs(
            dist - hypothenuse
        )  # compute the distance between the distance the player wants to move
        # and the size of the hypothenuse in the triple
        if d < mindist:  # if the computed distance is smaller than the current minimum
            # distance store the newly computed value into the minimum
            # distance variable
            mindist = d
            t = (a, b, hypothenuse)  # update the triple
    # return the triple with the hypothenuse (3rd element in the tuple)
    # with size closest to requested distance
    return t


def select_coordinates(ab: tuple[int, int], octant: int) -> tuple[int, int]:
    assert octant >= 1 and octant <= 8
    a, b = ab

    if octant == 1:  # 0-45 degrees
        if a > b:
            return (a, b)
        else:
            return (b, a)
    elif octant == 2:  # 45-90 degrees
        if b > a:
            return (a, b)
        else:
            return (b, a)
    elif octant == 3:  # 90 - 135 degrees
        if b > a:
            return (-a, b)
        else:
            return (-b, a)
    elif octant == 4:  # 135 - 180 degrees
        if a > b:
            return (-a, b)
        else:
            return (-b, a)
    elif octant == 5:  # 180 - 225 degrees
        if a > b:
            return (-a, -b)
        else:
            return (-b, -a)
    elif octant == 6:  # 225 - 270 degrees
        if b > a:
            return (-a, -b)
        else:
            return (-b, -a)
    elif octant == 7:  # 270 - 315 degrees
        if b > a:
            return (a, -b)
        else:
            return (b, -a)
    elif octant == 8:  # 270 - 360 degrees
        if a > b:
            return (a, -b)
        else:
            return (b, -a)

    # We never get here, just to make the warning about returning from all
    # code paths go away
    return (0, 0)


def distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    return math.sqrt(a * a + b * b)


# Check if the distance between the player's position and the destination is
# lower than minimum distance required to win
def check_winner(winning_player, other_player) -> bool:
    min_dist = destination["space_buffer"]
    # distance between player and destination
    d = distance(destination["cartesian_coords"], winning_player["cartesian_coords"])
    # check if distance between player and destination is smaller than
    # destination buffer size
    if d <= min_dist:
        return True

    d = distance(winning_player["cartesian_coords"], other_player["cartesian_coords"])

    if d <= other_player["space_buffer"]:
        return True

    return False


# Compute the gradient as ratio of differences between y coordinates and x
# coordinates.
def gradient(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


# Compute the mid point between two points
def midpoint(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    x = (
        p1[0] + p2[0]
    ) // 2  # force integer division, a single '/' would return a float
    y = (p1[1] + p2[1]) // 2
    return (x, y)

# Check if input is correct.
# Input is correct if the text contains two numbers, the direction value
# is between 1 and 8 and the distance is greater than zero.
# We are not checking if the player can move in a specific direction by the
# passed amount and stay within the window boundary; such check if performed
# when the player moves. 
def validate_input(text: str) -> bool:
    # split string containing multiple elements separated by space into
    # array of elements
    values = text.split(' ')
    # check that we have two values
    if len(values) < 2:
        return False
    try:
        # check that the text elements can be converted to integer;
        # if not possible to convert to integers an exception is thrown
        distance = int(values[0])
        direction = int(values[1])
        # check that direction is valid
        if direction < 1 or direction > 8:
            return False
        # check that distance is greated than zero
        if distance <= 0:
            return False
        return True
    except:
        # if we jump to here is because the passed text does not contain
        # two numbers
        return False
    

# GAME LOOP #
while True:  # The gameplay happens in here. Infinite loop until the user quits or a
    # player wins"
    for (
        event
    ) in (
        pygame.event.get()
    ):  # scan through all 'events' happening to the window such as mouse
        # clicks and key presses
        # must have this else the user can't quit!
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # if a mouse button is down
            left_button, middle_button, right_button = (
                pygame.mouse.get_pressed()
            )  # get the state of the mouse buttons
            if left_button:
                # if the left button was pressed, ask for player 1 new
                # coordinates (for you, you must ask for distance and
                # direction!)

                player_input = input(
                    "Player 1> Enter new distance/amount you want to move and direction (which way) as two numbers separated by space: "
                )                
                if not validate_input(player_input):
                    print("Error, enter values again (press the mouse button again)")
                    continue
                dist, direction = player_input.split(" ")  
                # You neeed to ask for distance and direction
                dist = int(dist)
                direction = int(direction)
                # convert triple list to dict
                tri_dict = triples_dict(triples)
                # select the triple with the hypothenuse length as close as
                # possible to the 'direction' number
                triple = select_triple(tri_dict, dist)
                # extract the first two numbers of the triple
                (a, b, _) = triple
                # select which of the two numbers to use for X and which for Y
                # and decide if you need to add a minus sign
                (dx, dy) = select_coordinates((a, b), direction)
                # update the position and other parameters in the dictionary
                # for player one
                (x, y) = player_one["cartesian_coords"]
                (new_x, new_y) = (x + dx, y + dy)
                # check if new position is within boundaries, if not
                if (new_x <= -MAX_COORD or new_x >= MAX_COORD
                    or new_y <= -MAX_COORD or new_y >= MAX_COORD):
                    print("Distance too large, position out of bound")
                    print("Enter new values (press mouse button again)")
                    continue # go back to beginning of while loop 
                player_one["cartesian_coords"] = (new_x, new_y)
                player_one["pygame_coords"] = conv_cartesian_to_pygame_coords(new_x, new_y)
                dest = destination["cartesian_coords"]
                min_dist = destination["space_buffer"]
                if check_winner(player_one, player_two):
                    print("Player 1 won")
                    break
                position = player_one["cartesian_coords"]
                player_one["distance_from_dest"] = distance(position, dest)
                player_one["gradient"] = gradient((x, y), (new_x, new_y))
                position2 = player_two["cartesian_coords"]
                player_one["midpoint"] = midpoint(position, position2)
                print_status(player_one)
            elif right_button:
                player_input = input(
                    "Player 2> Enter new distance/amount you want to move and direction (which way) as two numbers separated by space: "
                )
                if not validate_input(player_input):
                    print("Error, enter the values again (press the mouse button again)")
                    continue
                dist, direction = player_input.split(" ") 
                # You neeed to ask for distance and direction
                dist = int(dist)
                direction = int(direction)
                # convert triple list to dict
                tri_dict = triples_dict(triples)
                # select the triple with the hypothenuse length as close as
                # possible to the 'dist' number
                triple = select_triple(tri_dict, dist)
                # extract the first two numbers of the triple
                (a, b, _) = triple
                # select which of the two numbers to use for X and which for Y
                # and decide if you need to add a minus sign
                (dx, dy) = select_coordinates((a, b), direction)
                # update the position and other parameters in the dictionary
                # for player one
                (x, y) = player_two["cartesian_coords"]
                (new_x, new_y) = (x + dx, y + dy)
                if (new_x <= -MAX_COORD or new_x >= MAX_COORD
                    or new_y <= -MAX_COORD or new_y >= MAX_COORD):
                    print("Distance too large, position out of bound")
                    print("Enter new values (press mouse button again)")
                    continue # go back to beginning of while loop 
                player_two["cartesian_coords"] = (new_x, new_y)
                player_two["pygame_coords"] = conv_cartesian_to_pygame_coords(new_x, new_y)
                dest = destination["cartesian_coords"]
                min_dist = destination["space_buffer"]
                if check_winner(player_two, player_one):
                    print("Player 2 won")
                    break
                position = player_two["cartesian_coords"]
                player_two["distance_from_dest"] = distance(position, dest)
                player_two["gradient"] = gradient((x, y), (new_x, new_y))
                position1 = player_one["cartesian_coords"]
                player_two["midpoint"] = midpoint(position, position1)
                print_status(player_two)

    app_surf_update(
        destination, player_one, player_two
    )  # Call the function to update the app surface with the new coordinates.
    # Send it the entities
    # now refresh the window so that our changes are visible.
    # Loop back to while True.
    refresh_window()
