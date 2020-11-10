from cube import Cube
from solver import Solver
from util import scramble_to_str, print_cube, get_random_scramble_by_length

TRAIN_START_LENGTH = 3
TRAIN_UNTIL_LENGTH = 5
TRAIN_CASES = 10


def train():
    successful_trainings = 0
    print("Start training...")
    training_solver = Solver()
    for i in range(TRAIN_START_LENGTH, TRAIN_UNTIL_LENGTH + 1):
        print("Training scrambles length " + str(i) + "...")
        successful_trainings_by_length = 0
        for j in range(0, TRAIN_CASES):
            random_cube = Cube()
            scramble = get_random_scramble_by_length(i)
            random_cube.apply_notation(scramble)
            training_success = training_solver.try_to_solve(random_cube)
            if training_success:
                successful_trainings_by_length += 1
        print("Success on training length " + str(i) + ": " + str(successful_trainings_by_length) + "/" + str(
            TRAIN_CASES))
        successful_trainings += successful_trainings_by_length
    print("Overall training success: " + str(successful_trainings) + "/" + str(
        TRAIN_CASES * (TRAIN_UNTIL_LENGTH - TRAIN_START_LENGTH)))


def generate_and_scramble_cube():
    random_cube = Cube()
    scramble = get_random_scramble_by_length(7)
    print("Applying scramble: " + scramble_to_str(scramble))
    random_cube.apply_notation(scramble)
    print_cube(random_cube)
    return random_cube


if __name__ == '__main__':
    train()
    cube = generate_and_scramble_cube()
    solver = Solver()
    success, solution = solver.try_to_solve(cube)
    if success:
        print("Success! Solution: " + scramble_to_str(solution))
