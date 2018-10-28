graph = {'a': {'b': 10, 'c': 3},
        'b': {'c': 1, 'd': 2},
        'c': {'b': 4, 'd': 8, 'e': 2},
        'd': {'e': 7},
        'e': {'d': 9}
        }

graph = {'1': {'2': 375, '3': 75},
        '2': {'1': 375, '4': 75},
        '3': {'1': 75, '5': 150},
        '4': {'2': 75, '6': 150},
        '5': {'3': 150, '7': 149},
        '6': {'4': 150, '8': 149},
        '7': {'5': 150, '9': 135},
        '8': {'6': 150, '10': 135}
        '9': {'7': 135},
        '10': {'8': 135}
        }



def djikstra(graph, start, goal):
    shortest_distance = {}
    predecessors = {}
    unseen_nodes = graph

    infinity = 9999999
    path = []

    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessors[child_node] = min_node
        unseen_nodes.pop(min_node)

    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessors[current_node]
        except KeyError:
            print('Path not reachable')
            break

    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance: ', shortest_distance[goal])
        print('Shortest path is: ' + str(path))


djikstra(graph, 'a', 'd')