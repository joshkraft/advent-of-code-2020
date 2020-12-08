import re
import networkx as nx


with open("input/day-7.txt", "r") as fp:
    input = fp.readlines()

graph = nx.DiGraph()

for line in input:
    match = re.match(r"(.*) bags contain (.*)$", line)
    if match:
        color = match.group(1)
        remain = match.group(2)
        for child in re.findall(r"([\d]+) (.*?) bag", remain):
            graph.add_edge(color, child[1], count=int(child[0]))

def countBagsIn(root):
    totalBags = 0
    for k, val in graph[root].items():
        totalBags += val['count'] * countBagsIn(k) + val['count']
    return totalBags


print('Answer one is ' + str(len(nx.ancestors(graph, "shiny gold"))))
print('Answer two is ' + str(countBagsIn('shiny gold')))