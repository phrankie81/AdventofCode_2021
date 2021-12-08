# test_aoc_template.py

import pathlib
import pytest
import solution_02 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

example = "example1.txt"
test_parsing = [(example, [['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]])]
test_part1 = [(example, 150,)]
test_part2 = [(example, 900)]

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