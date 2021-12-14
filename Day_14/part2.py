from collections import Counter, defaultdict
from pathlib import Path


PUZZLE_DIR = Path(__file__).parent
filename = "input.txt"

template = (PUZZLE_DIR / filename).read_text().strip().split("\n\n")[0]
pairs = (PUZZLE_DIR / filename).read_text().strip().split("\n\n")[1].split("\n")

pair_dict = dict(line.split(" -> ") for line in pairs)
aa = [a+b for a, b in zip(template, template[1:])]
count = Counter(a+b for a, b in zip(template, template[1:]))

for _ in range(40):
    keys = defaultdict(int)
    for p, v in count.items():
        if p in pair_dict:
            i = pair_dict[p]
            keys[p[0]+i] += v
            keys[i+p[1]] += v
        else:
            keys[p] = v
    count = keys
another_dict = defaultdict(int)
for p, v in count.items():
    another_dict[p[0]] += v
    another_dict[p[1]] += v

for p, v in another_dict.items():
    if v%2 == 0:
        another_dict[p] = int(v/2)
    else:
        another_dict[p] = int((v+1)/2)

# sort the final dict based on values
another = sorted(another_dict.items(), key=lambda kv: kv[1], reverse=True)
print(f"Answer to part 1 is {another[0][1] - another[-1][1]}")
