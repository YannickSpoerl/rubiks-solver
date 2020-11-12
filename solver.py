import os
import pickle

from cube import Cube
from util import get_available_moves, get_random_scramble_by_length, scramble_to_str

# specify names of files
DB_FILE_NAME = ".db"
STATS_FILE_NAME = ".stats"

# define depth for search
SEARCH_DEPTH = 4


# specify default training parameters
TRAIN_START_LENGTH = 1
TRAIN_UNTIL_LENGTH = 5
TRAIN_CASES = 10


class Solver:

    # try to find cube in neighbourhood, solve by:
    # transforming current cube into known cube
    # solve known cube by known solution
    # TODO: make search-depth parameter
    def try_to_solve(self, cube_to_solve, best_solution=False):
        if cube_to_solve is None or type(cube_to_solve) is not Cube:
            raise Exception("Parameter must be a valid cube")
        if not best_solution:
            success, setup, key = self.find_possible_match(cube_to_solve, SEARCH_DEPTH, [])
            if not success:
                return False, None
            setup.extend(self.already_solved_cubes.get(key))
            self.save_solution(cube_to_solve, setup)
            return True, setup
        else:
            matches = []
            self.find_all_possible_matches(cube_to_solve, SEARCH_DEPTH, [], matches)
            best_match = None
            best_match_length = None
            for match in matches:
                length = len(match[0]) + len(self.already_solved_cubes.get(match[1]))
                if best_match_length is None or length < best_match_length:
                    best_match = match
                    best_match_length = length
            if best_match is None:
                return False, None
            else:
                best_match[0].extend(self.already_solved_cubes.get(best_match[1]))
                return True, best_match[0]

    # find any cube that is in neighbourhood
    def find_possible_match(self, cube_to_solve, depth, pre_moves):
        if cube_to_solve.get_id() in self.already_solved_cubes:
            return True, pre_moves, cube_to_solve.get_id()
        if depth <= 0:
            return False, None, None
        for possible_move in get_available_moves():
            cube_copy = cube_to_solve.get_copy()
            cube_copy.apply_move(possible_move)
            setup = []
            setup.extend(pre_moves)
            setup.append(possible_move)
            found_solution, setup, key = self.find_possible_match(cube_copy, depth - 1, setup)
            if found_solution:
                return True, setup, key
        return False, None, None

    # find all cubes that are in neighbourhood
    def find_all_possible_matches(self, cube_to_solve, depth, pre_moves=None, matches=None):
        if pre_moves is None:
            pre_moves = []
        if matches is None:
            matches = []
        if cube_to_solve.get_id() in self.already_solved_cubes:
            matches.append([pre_moves, cube_to_solve.get_id()])
        if depth > 0:
            for possible_move in get_available_moves():
                cube_copy = cube_to_solve.get_copy()
                cube_copy.apply_move(possible_move)
                setup = []
                setup.extend(pre_moves)
                setup.append(possible_move)
                self.find_all_possible_matches(cube_copy, depth - 1, setup, matches)

    # TODO: allow traingin for optimal solutions
    # for every length generate unkown scrambles and try to solve cube, persist all solved cubes and solved scrambles
    def train(self, start_length=TRAIN_START_LENGTH, end_length=TRAIN_UNTIL_LENGTH, cases=TRAIN_CASES):
        successful_trainings = 0
        print("Start training...")
        for i in range(start_length, end_length + 1):
            print("Training scrambles with length " + str(i) + "...")
            successful_trainings_by_length = 0
            for j in range(0, cases):
                random_cube = Cube()
                scramble = self.find_unknown_scramble(i)
                if scramble is None:
                    print("Skipping length " + str(i) + ", all scrambles already known.")
                    successful_trainings_by_length = cases
                    break
                random_cube.apply_notation(scramble)
                training_success = self.try_to_solve(random_cube)
                if training_success:
                    self.persist_scramble(scramble)
                    successful_trainings_by_length += 1
            print("Success on training length " + str(i) + ": " + str(successful_trainings_by_length) + "/" + str(
                cases))
            successful_trainings += successful_trainings_by_length
        print("TRAINING REPORT:")
        print("Overall success: " + str(successful_trainings) + "/" + str(
            cases * (end_length + 1 - start_length)))
        print("Scrambles known:")
        for key in self.known_scrambles.keys():
            print("Length " + str(key) + ": " + str(len(self.known_scrambles.get(key))) + "/" + str(18**key))

    # TODO: gets stuck on high numbers of known scrambles, make not-random
    # if all scrambles of length are know, abort, else try to generate unknown scramble with length
    def find_unknown_scramble(self, length):
        if self.known_scrambles.get(length) is None:
            self.known_scrambles[length] = []
        if len(self.known_scrambles.get(length)) is 18**length:
            return None
        scramble = None
        while scramble is None:
            possible_scramble = get_random_scramble_by_length(length)
            if scramble_to_str(possible_scramble) not in self.known_scrambles.get(length):
                scramble = possible_scramble
        return scramble

    # initialized the solver
    def __init__(self):
        self.known_scrambles = {}
        self.load_known_scrambles()
        self.already_solved_cubes = {}
        self.load_already_solved_cubes()

    # if scrambles-file does not exist, create, else read scrambles from file
    def load_known_scrambles(self):
        if not os.path.exists(STATS_FILE_NAME):
            os.mknod(STATS_FILE_NAME)
            with open(STATS_FILE_NAME, 'wb') as file:
                self.known_scrambles[0] = [""]
                pickle.dump(self.known_scrambles, file)
                return
        with open(STATS_FILE_NAME, 'rb') as file:
            self.known_scrambles = pickle.load(file)
            return

    # if solved-cubes-file does not exist, create, else read solvec-cubes from file
    def load_already_solved_cubes(self):
        if not os.path.exists(DB_FILE_NAME):
            os.mknod(DB_FILE_NAME)
            with open(DB_FILE_NAME, 'wb') as file:
                solved_cube = Cube()
                self.already_solved_cubes[solved_cube.get_id()] = []
                pickle.dump(self.already_solved_cubes, file)
                return
        with open(DB_FILE_NAME, 'rb') as file:
            self.already_solved_cubes = pickle.load(file)
            return

    # write all solved-cubes to file
    def save_solution(self, cube_to_solve, solution):
        self.already_solved_cubes[cube_to_solve.get_id()] = solution
        with open(DB_FILE_NAME, 'wb') as file:
            pickle.dump(self.already_solved_cubes, file)

    # write all known-scrambles to file
    def persist_scramble(self, scramble):
        if not len(scramble) in self.known_scrambles:
            self.known_scrambles[len(scramble)] = []
        self.known_scrambles.get(len(scramble)).append(scramble_to_str(scramble))
        with open(STATS_FILE_NAME, 'wb') as file:
            pickle.dump(self.known_scrambles, file)
