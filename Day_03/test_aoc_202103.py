# test_aoc_template.py

import pathlib
import pytest
import aoc_202103 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

example = "example.txt"
test_parsing = [
    (
        example,
        [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ],
    )
]
test_part1 = [(example, 198,)]
test_part2 = [(example, 230)]


@pytest.mark.parametrize("input_str,expected", test_parsing)
def test_parse_example1(input_str, expected):
    """Test that input is parsed properly"""
    assert aoc.parse(input_str) == expected


@pytest.mark.parametrize("input_str,expected", test_part1)
def test_part1_example1(input_str, expected: int):
    """Test part 1 on example input"""
    assert aoc.part1(input_str) == expected


# @pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input_str,expected", test_part2)
def test_part2_example2(input_str, expected):
    """Test part 2 on example input"""
    assert aoc.part2(input_str) == expected
