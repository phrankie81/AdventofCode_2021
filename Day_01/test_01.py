# test_aoc_template.py

from pathlib import Path
import pytest
import solution_01 as aoc

PUZZLE_DIR = Path(__file__).parent


@pytest.mark.parametrize(
    "input_list,expected",
    [
        (
            [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],
            7,
        )
    ],
)
def test_part1(input_list: list, expected: int) -> None:
    assert aoc.part1(input_list) == expected


@pytest.mark.parametrize(
    "input_list,expected",
    [
        (
            [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],
            5,
        )
    ],
)
def test_part2(input_list: list, expected: int) -> None:
    assert aoc.part2(input_list) == expected
