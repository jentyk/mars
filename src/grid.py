from dataclasses import dataclass, field

from src.robot import Robot


@dataclass
class Grid:
    """A grid for Mars Robots."""

    x: int = 0
    y: int = 0
