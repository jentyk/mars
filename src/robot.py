from dataclasses import dataclass
from itertools import cycle


@dataclass
class Robot:
    """A Mars Robot."""

    x: int = 0
    y: int = 0
    orientation: str = "N"
    status: str = "OK"

    def __post_init__(self):
        self.cycle_right = cycle(("N", "E", "S", "W")).__next__
        self.set_orientation(self.cycle_right)

        self.cycle_left = cycle(("N", "W", "S", "E")).__next__
        self.set_orientation(self.cycle_left)

    def set_orientation(self, method):
        while True:
            if method() == self.orientation:
                break

    def turn_right(self):
        self.orientation = self.cycle_right()
        self.set_orientation(self.cycle_left)

    def turn_left(self):
        self.orientation = self.cycle_left()
        self.set_orientation(self.cycle_right)

    def move(self, movement):
        if self.orientation == "N":
            self.y += 1
        elif self.orientation == "S":
            self.y -= 1
        elif self.orientation == "E":
            self.x += 1
        elif self.orientation == "W":
            self.x -= 1

    def __str__(self):
        return (
            f"({self.x}, {self.y}, {self.orientation})"
            f"{f' {self.status}' if self.status == 'LOST' else ''}"
        )

    def set_position(self, x, y):
        self.x = x
        self.y = y
