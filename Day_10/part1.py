from pathlib import Path

PUZZLE_DIR = Path(__file__).parent
lines = (PUZZLE_DIR / "input.txt").read_text().strip()


def opp(paren):
    if paren == '>':
        return '<'
    elif paren == ')':
        return '('
    elif paren == ']':
        return '['
    else:
        return '{'


def find_corrupted(s):
    toret = {}
    table = {')': 3, ']': 57, '}': 1197, '>': 25137}

    for i, c in enumerate(s):
        if c in ['<', '(', '{', '[']:
            toret[i] = c
        else:
            if opp(c) == list(toret.items())[-1][1]:
                x = toret.popitem()
            else:
                if table[c] is None:
                    return 0
                else:
                    return table[c]
    return 0

if __name__ == '__main__':
    points = []
    for line in lines.split('\n'):
        points.append(find_corrupted(line))
    print(sum(points))