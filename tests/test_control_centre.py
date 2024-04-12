from src.control_centre import ControlCentre
from src.grid import Grid
from src.robot import Robot


def test_control_centre_with_robots():
    control_centre = ControlCentre(Grid(4, 8))
    r1 = Robot(2, 3, "N")
    control_centre.add_robot(r1)
    r2 = Robot(1, 0, "S")
    control_centre.add_robot(r2)
    assert (
        str(control_centre)
        == """(2, 3, N)
(1, 0, S)"""
    )


def test_move():
    control_centre = ControlCentre(Grid(4, 8))
    r1 = Robot(2, 3, "N")
    control_centre.add_robot(r1)
    r2 = Robot(1, 0, "S")
    control_centre.add_robot(r2)
    control_centre.move_robot(0, "FLLFR")
    control_centre.move_robot(1, "FFRLF")
    assert (
        str(control_centre)
        == """(2, 3, W)
(1, 0, S) LOST"""
    )
