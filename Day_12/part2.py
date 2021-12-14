from pathlib import Path

PUZZLE_DIR = Path(__file__).parent
lines = (PUZZLE_DIR / "input.txt").read_text().strip().split("\n")

lines = [line.split("-") for line in lines]


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

for node in graph_dict:
    if "start" in graph_dict[node]:
        graph_dict[node].remove("start")
graph_dict.pop("end", None)
print(graph_dict)

paths = []


def go_down_path(node, graph, path, doublesmall):
    for nodes in graph[node]:
        if nodes == "end":
            paths.append(path + ["end"])

        elif nodes.isupper():
            go_down_path(nodes, graph, path + [nodes], doublesmall)

        elif nodes.islower() and nodes not in path:
            go_down_path(nodes, graph, path + [nodes], doublesmall)

        elif nodes.islower() and nodes in path and doublesmall:
            continue

        elif nodes.islower() and nodes in path and not doublesmall:
            go_down_path(nodes, graph, path + [nodes], True)


go_down_path("start", graph_dict, ["start"], False)
print(len(paths))
