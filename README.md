# Rubik's Cube Solver

## Table of Contents

* [About the Project](#about-the-project)
* [How to use the Solver](#how-to-use-the-solver)
* [How the Solver works](#how-the-solver-works)
* [Training](#training)
* [This is just a prototype](#this-is-just-a-prototype)
* [License](#license)
* [Contact](#contact)



## About The Project

I like solving Rubik's Cubes myself and have spent quite some time with them.
There are a lot of efficient and fast solvers out there, but I wanted to
implement my own approach. This solver is more of a prototype and test, not
a fast, efficient or reliable solver.

## How to use the solver

* Get familiar with the [Rubik's Cube Notation](https://en.wikipedia.org/wiki/Rubik's_Cube#Move_notation)

* Create a solver instance
```python
from solver import Solver
solver = Solver()
```
* Train the solver for scramble-lengths 1 to 4, 500 each
```python
solver.train(1, 4, 500)
```
* Get a scrambled cube
```python
from cube import Cube
from util import get_random_scramble_by_length
random_cube = Cube()
scramble = get_random_scramble_by_length(10)
random_cube.apply_notation(scramble)
```
* Try to solve the cube ("True" meaning he will find the best solution but will take more time)
```python
is_success, solution = solver.try_to_solve(cube, True)
```

### How the solver works

There are two relevant files for the solver, that are loaded and updated during every run.
* *".db"* keeps track of solved cubes and what each solution was applied.
* *".stats"* keeps track on the training process of the solver

The solver views a scrambled cube as the root of a tree. Every possible move
(see [Cube-Notation](https://en.wikipedia.org/wiki/Rubik's_Cube#Move_notation)) progresses one layer further into the tree, meaning the 1st Layer
has only one node (the scrambled one), the 2nd layer 18 nodes, the 3rd 18² and so on and
so on.

The solver will search the tree (by default 4 layers deep, meaning 18⁴ nodes)
for any cubes that he already knows how to solve. Should he find at least one,
he will know how to solve the new cube (by combing setup-moves and the already known solution).
He will also persist the new cube and will from that point on know more cubes.

That means the solver starts out very "dumb" but will learn by solving more and more cubes,
meaning the files will grow, but the solver will become smarter and being able
to solve more difficult cubes.

### Training
Since the solver starts up with being only able to solve cubes scrambled by four moves,
you want to train the solver not only by giving it cubes to solve but in a more
structured way. Therefore the solver can be trained. As there are 18 possible moves,
there are at most 18 cubes scrambled by one move, 18² cubes scrambled by two moves
and so on. 

The solver can be trained, by telling him on what move-count he should start and
end and how many cubes scrambled with the move-count he shall try to solve.
So to train the solver on scrambles from length 3 to 5, we give that as parameters.
Also there are 1889568 possible scrambles with length 5, training all of them would be a bit much.
We will therefore tell the solver to only train 100 differenct scrambles that he does not know yet.
Should the solver already know all scrambles with a given length he will just skip that length.
```python
solver.train(3, 5, 100)
```
This gives us good control over how the solver will behave and should be tweaked and tuned.
I myself have also not yet figured out the best way to train the solver yet, so
make sure to tweak those settings a bit.

## This is just a prototype
As mentioned, this solver is not very fast nor always finding optimal solutions. Futher Im quite sure
that even if trained a lot a cleverly tweaked solver will never be able to solve every cube you throw
at it. This project is more to explore a possible approach of solving a rubik's cubes by computation and learning
instead of simply implementing a solving-method that humans might use. Im able to solve the cube faster than
the solver and will always be able to solve, not matter the length of the scramble, something that this solver
is not able to do (even though Im a dumb human and he is a smart computer). But Im happy with the outcome and
Im convinced of the effectiveness of this approach and think when implemented right and optimized this approach
is very powerful.

## License

Distributed under the MIT License. See [LICENSE](https://github.com/YannickSpoerl/rubiks-solver/blob/master/LICENSE.md) for more information.

## Contact

Yannick Spoerl - [@yannickspoerl](https://twitter.com/yannickspoerl)

Project Link - [https://github.com/YannickSpoerl/blog](https://github.com/YannickSpoerl/rubiks-solver)
