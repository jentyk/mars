import pytest
from src.mars_expedition import get_grid, get_robot_commands, main


def test_get_grid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5 6")
    grid = get_grid()
    assert grid.x == 5 and grid.y == 6


@pytest.mark.parametrize("input_text", ["5 a\n", "5\n", "5 4 \n", "5 5 5\n"])
def test_get_grid_invalid_input(monkeypatch, input_text):
    monkeypatch.setattr("builtins.input", lambda _: input_text)
    with pytest.raises(ValueError):
        get_grid()


def test_get_robot_commands_valid_input(monkeypatch):
    user_input = "(1, 2, N) FFLRF"
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    assert get_robot_commands() == (1, 2, "N", "FFLRF")


def test_get_robot_commands_empty_input(monkeypatch):
    user_input = ""
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    assert get_robot_commands() is None


@pytest.mark.parametrize(
    "user_input, expected",
    [
        (["4 8", "invalid", ""], "Invalid robot command 'invalid'\n"),
        (
            ["4 8", "(2, 3, N) FLLFRI", "(1, 0, S) FFRLF", ""],
            "Invalid robot command '(2, 3, N) FLLFRI'\n",
        ),
    ],
)
def test_get_robot_commands_invalid_input(mocker, capsys, user_input, expected):
    fake_stdout = iter(user_input).__next__
    mocker.patch(
        "builtins.input",
        lambda _: fake_stdout(),
    )
    main()
    captured = capsys.readouterr()
    assert expected in captured.err


@pytest.mark.parametrize(
    "user_input, expected",
    [
        (
            ["4 8", "(2, 3, E) LFRFF", "(0, 2, N) FFLFRFF", ""],
            "(4, 4, E)\n(0, 4, W) LOST\n",
        ),
        (
            ["4 8", "(2, 3, N) FLLFR", "(1, 0, S) FFRLF", ""],
            "(2, 3, W)\n(1, 0, S) LOST\n",
        ),
    ],
)
def test_mars_expedition(mocker, capsys, user_input, expected):
    fake_stdout = iter(user_input).__next__
    mocker.patch(
        "builtins.input",
        lambda _: fake_stdout(),
    )
    main()
    captured = capsys.readouterr()
    assert captured.out == expected
