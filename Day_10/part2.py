from pathlib import Path
from part1 import find_corrupted, opp

PUZZLE_DIR = Path(__file__).parent
lines = (PUZZLE_DIR / "input.txt").read_text().strip()

incompl = [line for line in lines.split('\n') if find_corrupted(line) == 0]


def oppo(paren):
    if paren == '<':
        return '>'
    elif paren == '(':
        return ')'
    elif paren == '[':
        return ']'
    else:
        return '}'

def find_compl(s):
    toret = {}
    table = {')': 1, ']': 2, '}': 3, '>': 4}

    for i, c in enumerate(s):
        if c in ['<', '(', '{', '[']:
            toret[i] = c
        else:
            if opp(c) == list(toret.items())[-1][1]:
                x = toret.popitem()
    
    closers = [oppo(item) for item in toret.values()][::-1]
    score = 0
    for i in closers:
        score = (score * 5) + table[i]
    return score
if __name__ == '__main__':
    score_list = [find_compl(line) for line in incompl]
    reqd_index = len(score_list)//2
    print(f'Answer to part 2 is {sorted(score_list)[reqd_index]}')