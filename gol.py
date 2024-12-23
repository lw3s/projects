class GameOfLife(list[list[int]]):
    def __init__(self, *args):
        super().__init__(*args)
        self._HEIGHT = len(self)
        self._WIDTH = len(self[0, ...])
        for i in self:
            if len(i) != self.w():
                raise TypeError("all rows must be of equal length")
    
    def h(self):
        return self._HEIGHT
    
    def w(self):
        return self._WIDTH

    def __getitem__(self, coord: tuple[int | type(Ellipsis), int | type(Ellipsis)]) -> int | list[int]:
        row, col = coord

        if row == ... and col == ...:
            raise IndexError("both arguments cannot be ellipses")

        if col == ...:
            if 0 <= row < self.h():
                return super().__getitem__(row)
            return []
        if row == ...:
            if 0 <= col < self.w():
                return [super().__getitem__(i)[col] for i in range(self.h())]
            return []
    
        if 0 <= row < self.h() and 0 <= col < self.w():
            return super().__getitem__(row)[col]
    
    def __repr__(self):
        return "\n".join(map(str, self))


# mini tests

import sys

from icecream import ic

def main(args: list[str]) -> None:
    gol = GameOfLife([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ic(gol.h())
    ic(gol.w())
    ic(gol[1, ...])
    ic(gol[..., 1])
    ic(gol[1, 1])
    ic(gol)


if __name__ == "__main__":
    if ret := main(sys.argv[1:]) is not None: print(ret)
