from cube import Cube
from solver import Solver
from util import scramble_to_str, print_cube, get_random_scramble_by_length


# generate random scramble, apply scramble to cube and print cube
def generate_and_scramble_cube():
    random_cube = Cube()
    scramble = get_random_scramble_by_length(10)
    print("Applying scramble: " + scramble_to_str(scramble))
    random_cube.apply_notation(scramble)
    print_cube(random_cube)
    return random_cube


# train the solver a bit, try to solve a randomly scrambled cube
if __name__ == '__main__':
    solver = Solver()
    solver.train(1, 4, 500)
    cube = generate_and_scramble_cube()
    success, solution = solver.try_to_solve(cube, True)
    if success:
        print("Success! Solution: " + scramble_to_str(solution))
        cube.apply_notation(solution)
        print_cube(cube)
    else:
        print("Failure! No similar cubes found, could not solve cube.")
