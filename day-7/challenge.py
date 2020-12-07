import re
import networkx as nx


with open("input/day-7.txt", "r") as fp:
    data = fp.readlines()


G = nx.DiGraph()


for line in data:
    m = re.match(r"(.*) bags contain (.*)$", line)
    if m:
        color = m.group(1)
        remain = m.group(2)
        for child in re.findall(r"([\d]+) (.*?) bag", remain):
            G.add_edge(color, child[1], count=int(child[0]))


def countBagsIn(root):
    totalBags = 0
    for k, val in G[root].items():
        totalBags += val['count'] * countBagsIn(k) + val['count']
    return totalBags


print('Answer one is ' + str(len(nx.ancestors(G, "shiny gold"))))
print('Answer two is ' + str(countBagsIn('shiny gold')))