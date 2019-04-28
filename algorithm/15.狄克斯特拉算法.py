# _*_ coding: utf-8 _*_
__author__ = 'edward'
__date__ = '2019-04-22 14:15'

graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['finish'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['finish'] = 5

graph['finish'] = {}

infinity = float('inf')

# Each node has a cost. The cost is how long it takes to get to that node from the start.
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['finish'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['finish'] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # node = b

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]  # 当是a的时候，new_cost = 2 + 3 = 5
        if costs[n] > new_cost:  # costs[a] = 6  > new_cost(5)
            costs[n] = new_cost  # 把costs[a]更新为5
            parents[n] = node  # The new path goes through node B, so set B as the new parent.

    processed.append(node)
    node = find_lowest_cost_node(costs)


