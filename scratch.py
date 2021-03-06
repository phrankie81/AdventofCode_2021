example1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def part1(data):
    """Solve part 1"""
    num_of_increases = 0
    for i in range(len(data)-1):
        if data[i] - data[i+1] < 0:
            num_of_increases += 1
    return num_of_increases


def part2(data):
    """Solve part 2"""
    the_sums = []
    # the_sums = [data[i]+data[i+1]+data[i+2] for i in range(len(data)-2) if i+1 < len(data)]
    for i in range(len(data)-2):
        the_sums.append(data[i]+data[i+1]+data[i+2])
    result = part1(the_sums)
    return result

"""
Make it work, then make it beautiful, then if you really, really have to, make it fast. 
90 percent of the time, if you make it beautiful, it will already be fast. So really, 
just make it beautiful!
— Joe Armstrong

Above is me making it work. Below is me making it beautiful (maybe)
"""


part1_ans = sum([x < y for x, y in (zip(example1, example1[1:]))])
print(f"answer to part 1 is {part1_ans}")

sums = [x+y+z for x, y, z in zip(example1, example1[1:], example1[2:])]
part2_ans = sum([x < y for x, y in (zip(sums, sums[1:]))])
print(f"answer to part 1 is {part2_ans}")