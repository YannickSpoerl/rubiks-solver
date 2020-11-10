import copy

from color import Color
from util import get_available_moves


# noinspection DuplicatedCode,PyPep8
class Cube:

    def get_id(self):
        id_str = ""
        for edge in self.edges:
            for val in edge:
                id_str += val.value
        for corner in self.corners:
            for val in corner:
                id_str += val.value
        return id_str

    def get_solved_cube(self):
        return self.solved_cube

    def is_solved(self):
        solved_cube = self.get_solved_cube()
        return self.edges == solved_cube.edges and self.corners == solved_cube.corners

    def apply_move(self, move):
        self.apply_notation([move])

    def apply_notation(self, moves):
        if type(moves) is not list:
            raise Exception("Moves must be a list containing moves")
        for move in moves:
            if move not in get_available_moves():
                raise Exception("Move " + str(move) + " is not a valid move")
        switcher = {
            "r": self.r,
            "r'": self.r_inv,
            "r2": self.r2,
            "l": self.l,
            "l'": self.l_inv,
            "l2": self.l2,
            "f": self.f,
            "f'": self.f_inv,
            "f2": self.f2,
            "b": self.b,
            "b'": self.b_inv,
            "b2": self.b2,
            "u": self.u,
            "u'": self.u_inv,
            "u2": self.u2,
            "d": self.d,
            "d'": self.d_inv,
            "d2": self.d2,
        }
        for move in moves:
            move_to_execute = switcher.get(move, None)
            move_to_execute()

    def d(self):
        self.edges[8], self.edges[11], self.edges[10], self.edges[9] = \
            self.edges[9], self.edges[8], self.edges[11], self.edges[10]

        self.corners[7][0], self.corners[7][1] = self.corners[7][1], self.corners[7][0]
        self.corners[4][0], self.corners[4][1] = self.corners[4][1], self.corners[4][0]

        self.corners[4], self.corners[7], self.corners[6], self.corners[5] = \
            self.corners[5], self.corners[4], self.corners[7], self.corners[6]

    def d_inv(self):
        self.d()
        self.d()
        self.d()

    def d2(self):
        self.d()
        self.d()

    def b(self):
        self.edges[5][0], self.edges[5][1] = self.edges[5][1], self.edges[5][0]
        self.edges[6][0], self.edges[6][1] = self.edges[6][1], self.edges[6][0]

        self.edges[2], self.edges[5], self.edges[10], self.edges[6] = \
            self.edges[6], self.edges[2], self.edges[5], self.edges[10]

        self.corners[1][1], self.corners[1][2] = self.corners[1][2], self.corners[1][1]

        self.corners[2][0], self.corners[2][1], self.corners[2][2] = \
            self.corners[2][2], self.corners[2][0], self.corners[2][1]

        self.corners[5][0], self.corners[5][1], self.corners[5][2] = \
            self.corners[5][1], self.corners[5][2], self.corners[5][0]

        self.corners[6][0], self.corners[6][1] = self.corners[6][1], self.corners[6][0]

        self.corners[1], self.corners[2], self.corners[6], self.corners[5] = \
            self.corners[2], self.corners[6], self.corners[5], self.corners[1]

    def b_inv(self):
        self.b()
        self.b()
        self.b()

    def b2(self):
        self.b()
        self.b()

    def u(self):
        self.edges[0], self.edges[3], self.edges[2], self.edges[1] = \
            self.edges[3], self.edges[2], self.edges[1], self.edges[0]

        self.corners[2][1], self.corners[2][2] = self.corners[2][2], self.corners[2][1]
        self.corners[3][1], self.corners[3][2] = self.corners[3][2], self.corners[3][1]

        self.corners[0], self.corners[1], self.corners[2], self.corners[3] = \
            self.corners[3], self.corners[0], self.corners[1], self.corners[2]

    def u_inv(self):
        self.u()
        self.u()
        self.u()

    def u2(self):
        self.u()
        self.u()

    def f(self):
        self.edges[0][0], self.edges[0][1] = self.edges[0][1], self.edges[0][0]
        self.edges[4][0], self.edges[4][1] = self.edges[4][1], self.edges[4][0]

        self.edges[0], self.edges[4], self.edges[8], self.edges[7] = \
            self.edges[4], self.edges[8], self.edges[7], self.edges[0]

        self.corners[4][0], self.corners[4][1] = self.corners[4][1], self.corners[4][0]
        self.corners[0][0], self.corners[0][2] = self.corners[0][2], self.corners[0][0]
        self.corners[7][1], self.corners[7][2] = self.corners[7][2], self.corners[7][1]
        self.corners[3][0], self.corners[3][1] = self.corners[3][1], self.corners[3][0]

        self.corners[0], self.corners[4], self.corners[7], self.corners[3] = \
            self.corners[4], self.corners[7], self.corners[3], self.corners[0]

    def f_inv(self):
        self.f()
        self.f()
        self.f()

    def f2(self):
        self.f()
        self.f()

    def l(self):
        self.edges[5][0], self.edges[5][1] = self.edges[5][1], self.edges[5][0]
        self.edges[4][0], self.edges[4][1] = self.edges[4][1], self.edges[4][0]

        self.edges[1], self.edges[5], self.edges[9], self.edges[4] = \
            self.edges[5], self.edges[9], self.edges[4], self.edges[1]

        self.corners[1][0], self.corners[1][1], self.corners[1][2] = \
            self.corners[1][2], self.corners[1][0], self.corners[1][1]

        self.corners[5][0], self.corners[5][1] = self.corners[5][1], self.corners[5][0]
        self.corners[0][1], self.corners[0][2] = self.corners[0][2], self.corners[0][1]

        self.corners[4][0], self.corners[4][1], self.corners[4][2] = \
            self.corners[4][1], self.corners[4][2], self.corners[4][0]

        self.corners[0], self.corners[1], self.corners[5], self.corners[4] = \
            self.corners[1], self.corners[5], self.corners[4], self.corners[0]

    def l_inv(self):
        self.l()
        self.l()
        self.l()

    def l2(self):
        self.l()
        self.l()

    def r(self):
        # twist edges into right orientation
        self.edges[11][0], self.edges[11][1] = self.edges[11][1], self.edges[11][0]
        self.edges[6][0], self.edges[6][1] = self.edges[6][1], self.edges[6][0]
        # shift edges into right posistion
        self.edges[6], self.edges[3], self.edges[7], self.edges[11] = \
            self.edges[3], self.edges[7], self.edges[11], self.edges[6]
        # twist corners into right orientation
        self.corners[7][1], self.corners[7][2] = self.corners[7][2], self.corners[7][1]
        self.corners[3][0], self.corners[3][1] = self.corners[3][1], self.corners[3][0]
        self.corners[6][0], self.corners[6][2] = self.corners[6][2], self.corners[6][0]
        self.corners[2][1], self.corners[2][2] = self.corners[2][2], self.corners[2][1]
        # shift corners into right position
        self.corners[6], self.corners[2], self.corners[3], self.corners[7] = \
            self.corners[2], self.corners[3], self.corners[7], self.corners[6]

    def r_inv(self):
        self.r()
        self.r()
        self.r()

    def r2(self):
        self.r()
        self.r()

    def get_copy(self):
        return copy.deepcopy(self)

    def __init__(self):
        self.edges = []
        self.init_edges()
        self.corners = []
        self.init_corners()
        self.solved_cube = self.get_copy()

    def init_edges(self):
        # UP
        self.edges.append([Color.white, Color.green])
        self.edges.append([Color.white, Color.orange])
        self.edges.append([Color.white, Color.blue])
        self.edges.append([Color.white, Color.red])
        # MIDDLE
        self.edges.append([Color.green, Color.orange])
        self.edges.append([Color.orange, Color.blue])
        self.edges.append([Color.blue, Color.red])
        self.edges.append([Color.green, Color.red])
        # DOWN
        self.edges.append([Color.green, Color.yellow])
        self.edges.append([Color.orange, Color.yellow])
        self.edges.append([Color.blue, Color.yellow])
        self.edges.append([Color.red, Color.yellow])

    def init_corners(self):
        # UP
        self.corners.append([Color.white, Color.green, Color.orange])
        self.corners.append([Color.white, Color.orange, Color.blue])
        self.corners.append([Color.white, Color.blue, Color.red])
        self.corners.append([Color.white, Color.green, Color.red])
        # DOWN
        self.corners.append([Color.green, Color.orange, Color.yellow])
        self.corners.append([Color.orange, Color.blue, Color.yellow])
        self.corners.append([Color.blue, Color.red, Color.yellow])
        self.corners.append([Color.green, Color.red, Color.yellow])
