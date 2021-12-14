import re
from pathlib import Path
import pprint
from typing import final

PUZZLE_DIR = Path(__file__).parent
lines = (PUZZLE_DIR / "input.txt").read_text().strip().split('\n')

lines = [line.split('-') for line in lines]

graph_dict = {}
for line in lines:
	if line[0] in graph_dict:
		graph_dict[line[0]] += [line[1]]
	else:
		graph_dict[line[0]] = [line[1]]
	if line[1] in graph_dict:
		graph_dict[line[1]] += [line[0]]
	else:
		graph_dict[line[1]] = [line[0]]

paths = []
def go_down_path(node, graph, path):
	for nodes in graph[node]:
		if nodes == "end":
			paths.append(path + ["end"])
		elif nodes.isupper() or (nodes.islower() and nodes not in path):
			go_down_path(nodes, graph, path + [nodes])


go_down_path("start", graph_dict, ["start"])
print(len(paths))