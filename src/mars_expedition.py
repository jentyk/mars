import re
import sys
from typing import Optional, Tuple

from src.control_centre import ControlCentre
from src.grid import Grid
from src.robot import Robot

GRID_SIZE_RE = re.compile(r"^\d+ \d+$")
ROBOT_COMMAND_RE = re.compile(
    r"^\((?P<x>\d), (?P<y>\d), (?P<orientation>[NESW])\) (?P<movements>[LRF]+)$"
)


def main() -> None:
    while True:
        try:
            grid = get_grid()
            break
        except ValueError as e:
            print(e, file=sys.stderr)

    control_centre = ControlCentre(grid)

    while True:
        try:
            commands = get_robot_commands()
            if commands is None:
                break
            x, y, orientation, movements = commands
            robot = Robot(x, y, orientation)
            control_centre.add_robot(robot)
            control_centre.move_robot(-1, movements)
        except ValueError as e:
            print(e, file=sys.stderr)
    print(control_centre)


def get_robot_commands() -> Optional[Tuple[int, int, str, str]]:
    command = input("")
    if command == "":
        return None
    match = ROBOT_COMMAND_RE.match(command)
    if not match:
        raise ValueError(
            f"\nInvalid robot command '{command}'\n"
            f"Please provide a command in a form\n\n"
            f"(x, y, o) mmm...\n\n"
            f"where:\n\n"
            "x - initial position on x axis\n"
            "y - initial position on y axis\n"
            "o - initial orientation (N, E, S, W)\n"
            "m - specifies simple move in a sequence of movements "
            "(F - forward one space, L - rotate left by 90 degrees,"
            " R - rotate right by 90 degrees.\n\n"
        )
    return (
        int(match.group("x")),
        int(match.group("y")),
        match.group("orientation"),
        match.group("movements"),
    )


def get_grid() -> Grid:
    command = input("")
    if not GRID_SIZE_RE.match(command):
        raise ValueError(
            "Invalid grid size. Please provide a grid size in the format 'X Y'."
        )
    width, height = command.split(" ")
    return Grid(int(width), int(height))


if __name__ == "__main__":
    main()
