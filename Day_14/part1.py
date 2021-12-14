import pathlib
import collections

PUZZLE_DIR = pathlib.Path(__file__).parent
filename = "input.txt"

template = (PUZZLE_DIR / filename).read_text().strip().split("\n\n")[0]
pairs = (PUZZLE_DIR / filename).read_text().strip().split("\n\n")[1].split("\n")

# make the pairs into a dict
pair_dict = {}
for pair in pairs:
    # pair = pairs[0]
    pair = pair.split(" -> ")
    pair_dict[pair[0]] = pair[1]


def polymerize(string, no_of_times):
    for i in range(no_of_times):
        templ = string[0]
        for prev, curr in zip(string, string[1:]):
            for key, value in pair_dict.items():
                if key == prev + curr:
                    templ += value + curr
                    break
        string = templ
    return templ


stage1 = polymerize(template, 10)
most_common = collections.Counter(stage1).most_common()[0][1]
least_common = collections.Counter(stage1).most_common()[-1][1]
print(f"Answer to part 1 is {most_common - least_common}")
