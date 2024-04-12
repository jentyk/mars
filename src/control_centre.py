from dataclasses import dataclass, field

from src.grid import Grid
from src.robot import Robot


@dataclass
class ControlCentre:
    """A class representing a control centre."""

    grid: Grid
    robots: list[Robot] = field(default_factory=list)

    def add_robot(self, robot: Robot) -> None:
        self.robots.append(robot)

    def move_robot(self, index: int, movements: str) -> None:
        robot = self.robots[index]
        if robot.status == "LOST":
            return

        for movement in movements:
            if movement == "F":
                original_x = robot.x
                original_y = robot.y

                robot.move(movement)

                if (
                    robot.x < 0
                    or robot.x > self.grid.x
                    or robot.y < 0
                    or robot.y > self.grid.y
                ):
                    robot.status = "LOST"
                    robot.set_position(original_x, original_y)
                    break

            elif movement == "L":
                robot.turn_left()
            elif movement == "R":
                robot.turn_right()

    def __str__(self):
        return "\n".join([str(r) for r in self.robots])
