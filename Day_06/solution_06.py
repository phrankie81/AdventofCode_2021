test_fish = [3,4,3,1,2]
input_fish = [1,1,1,1,3,1,4,1,4,1,1,2,5,2,5,1,1,1,4,3,1,4,1,1,1,1,1,1,1,2,1,2,4,1,1,1,1,1,1,1,3,1,1,5,1,1,2,1,5,1,1,1,1,1,1,1,1,4,3,1,1,1,2,1,1,5,2,1,1,1,1,4,5,1,1,2,4,1,1,1,5,1,1,1,1,5,1,3,1,1,4,2,1,5,1,2,1,1,1,1,1,3,3,1,5,1,1,1,1,3,1,1,1,4,1,1,1,4,1,4,3,1,1,1,4,1,2,1,1,1,2,1,1,1,1,5,1,1,3,5,1,1,5,2,1,1,1,1,1,4,4,1,1,2,1,1,1,4,1,1,1,1,5,3,1,1,1,5,1,1,1,4,1,4,1,1,1,5,1,1,3,2,2,1,1,1,4,1,3,1,1,1,2,1,3,1,1,1,1,4,1,1,1,1,2,1,4,1,1,1,1,1,4,1,1,2,4,2,1,2,3,1,3,1,1,2,1,1,1,3,1,1,3,1,1,4,1,3,1,1,2,1,1,1,4,1,1,3,1,1,5,1,1,3,1,1,1,1,5,1,1,1,1,1,2,3,4,1,1,1,1,1,2,1,1,1,1,1,1,1,3,2,2,1,3,5,1,1,4,4,1,3,4,1,2,4,1,1,3,1]

# used a naive approach to handle part 1
def spawn(a_list):
    new_list = []
    for i in a_list:
        if i == 0:
            new_list.append(6)
            new_list.append(8)
        else:
            new_list.append(i-1)
    return new_list


def solve(days, fish):
    while True:
        if days == 0:
            return fish
        days, fish = days - 1, spawn(fish)

# print(len(solve(80, input_fish)))

"""realized how naive my approach was for part 1 when I ran into memory issues.
tried to look into memoization but it appears that's not meant for this kind of problem

Got a hint on reddit to count the number of occurrences of the integers (ages) 0 - 8
"""

groups = [test_fish.count(i) for i in range(9)]

days=256 #for part 1, days=80
''' Also got a hint on reddit to apply a sliding increase to the counts. 
Essentially if there are:
2 fish with age 3 on day 1 then there will be 
2 fish with age 2 on day 2 then there will be
2 fish with age 1 on day 3 and so on
'''
for i in range(days):
    groups = groups[1:]+[groups[0]]
    groups[6]+=groups[-1]

sum_of_groups = sum(groups)
print(f"Answer to part 2 is {sum_of_groups}")