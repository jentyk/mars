from src.grid import Grid


def test_grid():
    grid = Grid(4, 8)
    assert str(grid) == "Grid(x=4, y=8)"
