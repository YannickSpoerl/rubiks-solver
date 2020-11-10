import os
import pickle

from cube import Cube
from util import get_available_moves

FILE_NAME = ".db"
SEARCH_DEPTH = 4


class Solver:

    def __init__(self):
        self.already_solved_cubes = {}
        self.load_already_solved_cubes()

    def load_already_solved_cubes(self):
        if not os.path.exists(FILE_NAME):
            os.mknod(FILE_NAME)
            with open(FILE_NAME, 'wb') as file:
                solved_cube = Cube()
                self.already_solved_cubes[solved_cube.get_id()] = []
                pickle.dump(self.already_solved_cubes, file)
                return
        with open(FILE_NAME, 'rb') as file:
            self.already_solved_cubes = pickle.load(file)
            return

    def save_solution(self, cube_to_solve, solution):
        self.already_solved_cubes[cube_to_solve.get_id()] = solution
        with open(FILE_NAME, 'wb') as file:
            pickle.dump(self.already_solved_cubes, file)

    def try_to_solve(self, cube_to_solve):
        if cube_to_solve is None or type(cube_to_solve) is not Cube:
            raise Exception("Parameter must be a valid cube")
        success, setup, key = self.find_possible_match(cube_to_solve, SEARCH_DEPTH, [])
        if not success:
            print("No similar cube found, cube could not be solved.")
            return False, None
        setup.extend(self.already_solved_cubes.get(key))
        self.save_solution(cube_to_solve, setup)
        return True, setup

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
