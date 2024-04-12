from src.robot import Robot


def test_robot():
    robot = Robot(2, 3, "N")
    assert str(robot) == "(2, 3, N)"
