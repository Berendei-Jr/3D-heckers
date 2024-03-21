from typing import Final
import numpy as np

Dimensity: Final = 4

class PlayCube:
    class Coordinate:
        def __init__(self, x: int, y: int, z: int) -> None:
            self.x = x
            self.y = y
            self.z = z

    def __init__(self, dim: int) -> None:
        self.dim = dim
        self._cube = np.zeros((dim, dim, dim))
        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    if (i + j + k) % 2 == 1:
                        self._cube[i, j, k] = 1
                        if k == 0:
                            self._cube[i, j, k] = 2
                        if k == dim - 1:
                            self._cube[i, j, k] = 3

    def print(self):
        for i in range(self.dim):
            print('\t', end="")
            print(*[a for a in range(self.dim)], sep='\t')
            for j in range(self.dim):
                print(int(j), end="\t")
                for k in range(self.dim):
                    if self._cube[i, j, k] == 0:
                        print("", end = "\t")
                    if self._cube[i, j, k] == 1:
                        print("■", end = "\t")
                    if self._cube[i, j, k] == 2:
                        print("O", end = "\t")
                    if self._cube[i, j, k] == 3:
                        print("X", end = "\t")
                print()
            print()
        print()
    def move(self, start: Coordinate, end: Coordinate, is_king = False) -> None:
        if self._cube[start.x, start.y, start.z] < 2 or self._cube[end.x, end.y, end.z] != 1:
            return

        coordinates_diff = [abs(end.x - start.x), abs(end.y - start.y), abs(end.z - start.z)]

        if coordinates_diff[0] > 1 or coordinates_diff[1] > 1 or coordinates_diff[2] > 1:
            return

        if sum(coordinates_diff) != 2:
            return

        self._cube[end.x, end.y, end.z] = self._cube[start.x, start.y, start.z]
        self._cube[start.x, start.y, start.z] = 1

    def eat(self, start: Coordinate, end: Coordinate, is_king = False) -> None:
        if self._cube[start.x, start.y, start.z] == 0 or self._cube[end.x, end.y, end.z] != 1:
            return

        #if not (abs(end.x - start.x) == 2 and abs(end.y - start.y) == 2 and abs(end.z - start.z) == 2 and not is_king):
        #    return

        enemy_coordinate = self.Coordinate((start.x + end.x) // 2, (start.y + end.y) // 2, (start.z + end.z) // 2)
        if not(self._cube[enemy_coordinate.x, enemy_coordinate.y, enemy_coordinate.z] == 2 or self._cube[enemy_coordinate.x, enemy_coordinate.y, enemy_coordinate.z] == 3):
            return

        self._cube[enemy_coordinate.x, enemy_coordinate.y, enemy_coordinate.z] = 1
        self._cube[end.x, end.y, end.z] = self._cube[start.x, start.y, start.z]
        self._cube[start.x, start.y, start.z] = 1



field = PlayCube(Dimensity)
sides = ["Правый игрок", "Левый игрок"]
cur_side = 0
while(True):
    print(sides[cur_side])
    field.print()
    x1, y1, z1, x2, y2, z2 = map(int, input().split())

    field.move(field.Coordinate(x1, y1, z1), field.Coordinate(x2, y2, z2))
    field.eat(field.Coordinate(x1, y1, z1), field.Coordinate(x2, y2, z2))

    cur_side = (cur_side + 1) % 2
