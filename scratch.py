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
    

print(part1(example1))
print(part2(example1))