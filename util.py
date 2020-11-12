import random

from color import Color
from scrambles import get_scrambles, get_scramble


# get a random offical wca scramble
def get_random_scramble():
    return get_scramble(random.randint(0, len(get_scrambles()) - 1))


# generate random (non-wca) scramble with given length
def get_random_scramble_by_length(length):
    if length is None or type(length) is not int or length <= 0:
        raise Exception("Length must be valid int")
    scramble = []
    moves = get_available_moves()
    for i in range(0, length):
        scramble.append(moves[random.randint(0, len(moves) - 1)])
    return scramble


# format list of moves to str
def scramble_to_str(scramble):
    if scramble is None or type(scramble) is not list:
        raise Exception("Scramble must be list of strings")
    scramble_as_str = ""
    for i in range(0, len(scramble)):
        if scramble[i] is None or type(scramble[i]) is not str:
            raise Exception("Move in scramble must be string, was " + str(type(scramble[i])))
        if i is 0:
            scramble_as_str += scramble[i].upper()
        else:
            scramble_as_str += " " + scramble[i].upper()
    return scramble_as_str


# get all moves possible on cube
def get_available_moves():
    valid_moves = []
    for valid_move in ["r", "l", "f", "b", "u", "d"]:
        valid_moves.append(valid_move)
        valid_moves.append(valid_move + "'")
        valid_moves.append(valid_move + "2")
    return valid_moves


# print a cube to terminal
def print_cube(cube):
    if cube is None:
        raise Exception("Parameter must be a valid cube")
    # BACK
    print("             _____________")
    print(
        "             | {0} | {1} | {2} |".format(cube.corners[5][1].value.upper(), cube.edges[10][0].value.upper(),
                                                  cube.corners[6][0].value.upper()))
    print("             _____________")
    print("             | {0} | B | {1} |".format(cube.edges[5][1].value.upper(), cube.edges[6][0].value.upper()))
    print("             _____________")
    print(
        "             | {0} | {1} | {2} |".format(cube.corners[1][2].value.upper(), cube.edges[2][1].value.upper(),
                                                  cube.corners[2][1].value.upper()))
    print("             _____________")
    # LEFT UP RIGHT
    print("_______________________________________")
    print(
        "| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} |".format(cube.corners[5][0].value.upper(),
                                                                           cube.edges[5][0].value.upper(),
                                                                           cube.corners[1][1].value.upper(),
                                                                           cube.corners[1][0].value.upper(),
                                                                           cube.edges[2][0].value.upper(),
                                                                           cube.corners[2][0].value.upper(),
                                                                           cube.corners[2][2].value.upper(),
                                                                           cube.edges[6][1].value.upper(),
                                                                           cube.corners[6][1].value.upper()))
    print("_______________________________________")
    print(
        "| {0} | O | {1} || {2} | W | {3} || {4} | R | {5} |".format(cube.edges[9][0].value.upper(),
                                                                     cube.edges[1][1].value.upper(),
                                                                     cube.edges[1][0].value.upper(),
                                                                     cube.edges[3][0].value.upper(),
                                                                     cube.edges[3][1].value.upper(),
                                                                     cube.edges[11][0].value.upper()))
    print("_______________________________________")
    print("| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} |".format(cube.corners[4][1].value.upper(),
                                                                             cube.edges[4][1].value.upper(),
                                                                             cube.corners[0][2].value.upper(),
                                                                             cube.corners[0][0].value.upper(),
                                                                             cube.edges[0][0].value.upper(),
                                                                             cube.corners[3][0].value.upper(),
                                                                             cube.corners[3][2].value.upper(),
                                                                             cube.edges[7][1].value.upper(),
                                                                             cube.corners[7][1].value.upper()))
    print("_______________________________________")
    # FRONT
    print("             _____________")
    print(
        "             | {0} | {1} | {2} |".format(cube.corners[0][1].value.upper(), cube.edges[0][1].value.upper(),
                                                  cube.corners[3][1].value.upper()))
    print("             _____________")
    print("             | {0} | G | {1} |".format(cube.edges[4][0].value.upper(), cube.edges[7][0].value.upper()))
    print("             _____________")
    print(
        "             | {0} | {1} | {2} |".format(cube.corners[4][0].value.upper(), cube.edges[8][0].value.upper(),
                                                  cube.corners[7][0].value.upper()))
    print("             _____________")
    # DOWN
    print("             _____________")
    print(
        "             | {0} | {1} | {2} |".format(cube.corners[4][2].value.upper(), cube.edges[8][1].value.upper(),
                                                  cube.corners[7][2].value.upper()))
    print("             _____________")
    print("             | {0} | Y | {1} |".format(cube.edges[9][1].value.upper(), cube.edges[11][1].value.upper()))
    print("             _____________")
    print(
        "             | {0} | {1} | {2} |".format(cube.corners[5][2].value.upper(), cube.edges[10][1].value.upper(),
                                                  cube.corners[6][2].value.upper()))
    print("             _____________")


# check if two edges are the same
def edges_are_equal(edge1, edge2):
    if not edge_valid(edge1) or not edge_valid(edge2):
        raise Exception("Edges invalid")
    return (edge1[0] == edge2[0] and edge1[1] == edge2[1]) or (edge1[0] == edge2[1] and edge1[1] == edge2[0])


# check if two corners are the same
def corners_are_equal(corner1, corner2):
    if not corner_valid(corner1) or not corner_valid(corner2):
        raise Exception("Corners invalid")
    if corner1[0] == corner2[0]:
        return (corner1[1] == corner2[1] and corner1[2] == corner2[2]) or (
                corner1[1] == corner2[2] and corner1[2] == corner2[1])
    elif corner1[1] == corner2[1]:
        return (corner1[0] == corner2[0] and corner1[2] == corner2[2]) or (
                corner1[0] == corner2[2] and corner1[2] == corner2[0])
    elif corner1[2] == corner2[2]:
        return (corner1[0] == corner2[0] and corner1[1] == corner2[1]) or (
                corner1[0] == corner2[1] and corner1[1] == corner2[0])
    elif corner1[0] == corner2[1]:
        return corner1[1] == corner2[2] and corner1[2] == corner2[0]
    elif corner1[0] == corner2[2]:
        return corner1[1] == corner2[0] and corner1[2] == corner2[1]
    return False


# check if edge could exist on real cube
def edge_valid(edge):
    if edge is None:
        raise Exception("Edge must not be None")
    if type(edge) is not list:
        raise Exception("Edge must be a lists")
    if len(edge) is not 2:
        raise Exception("Edge must have exactly 2 colors")
    edge_set = set(edge)
    if Color.white in edge_set and Color.yellow in edge_set:
        return False
    if Color.green in edge_set and Color.blue in edge_set:
        return False
    if Color.red in edge_set and Color.orange in edge_set:
        return False
    return True


# check if corner could exist on real cube
def corner_valid(corner):
    if corner is None:
        raise Exception("Corner must not be None")
    if type(corner) is not list:
        raise Exception("Corner must be a list")
    if len(corner) is not 3:
        raise Exception("Corners must have exactly 3 colors")
    corner_set = set(corner)
    if Color.white in corner_set:
        if Color.green in corner_set:
            return Color.red in corner_set or Color.orange in corner_set
        if Color.blue in corner_set:
            return Color.red in corner_set or Color.orange in corner_set
        return False
    if Color.yellow in corner_set:
        if Color.green in corner_set:
            return Color.red in corner_set or Color.orange in corner_set
        if Color.blue in corner_set:
            return Color.red in corner_set or Color.orange in corner_set
        return False
    return False


# invert move
def inverse_move(move):
    if move is None:
        return None
    if type(move) is not str:
        raise Exception("Move must be a string")
    if move not in get_available_moves():
        raise Exception("Move must be valid")
    if len(move) is not 2:
        return move.lower() + "'"
    elif move[1] is "2":
        return move.lower()
    return move[0]
