import graph

def default_heuristic(n):
    """
    Default heuristic for A*. Do not change, rename or remove!
    """
    return 0


def bfs(start, goal):
    """
    Breadth-First search algorithm. The function is passed a start graph.Node object and a goal predicate.
    
    The start node can produce neighbors as needed, see graph.py for details.
    
    The goal is represented as a function, that is passed a node, and returns True if that node is a goal node, otherwise False. 
    
    The function should return a 4-tuple (path,distance,visited,expanded):
        - path is a sequence of graph.Edge objects that have to be traversed to reach a goal state from the start
        - distance is the sum of costs of all edges in the path 
        - visited is the total number of nodes that were added to the frontier during the execution of the algorithm 
        - expanded is the total number of nodes that were expanded, i.e. removed from the frontier to add their neighbors
    """

    # Set of arrays needed for the implementations
    nodeList = []
    expanded = []
    visited = []

    # Using a dictionary to store nodes and its value
    nodeDict = {}

    # Start the list with the start node
    nodeList.append(start)
    visited.append(start)

    # Set an empty array for the path
    path = []
    # Set the distance to 0
    distance = 0

    # Run until it reaches the destination
    while (len(nodeList) > 0):
        # pop the next node in the list and make it current
        currentNode = nodeList.pop(0)
        # Take current node and add to expanded
        expanded.append(currentNode)
        # Get all the neighbors of the current node
        neighbors = currentNode.get_neighbors()
        # Run through all the neighbors
        for neighbor in neighbors:
            # Checks if the next neighbor node is visited
            if neighbor.target not in visited:
                # Put neighbor node in visited
                visited.append(neighbor.target)
                # Set the current node with its value to a variable
                nodeEntry = [currentNode, neighbor.cost]
                # Add the next current node to the dictionary
                nodeDict[neighbor.target.get_id()] = nodeEntry
                # Check if the neighbor node is our goal
                if goal(neighbor.target):
                    # add the goal to the path
                    path.insert(0, neighbor.target)
                    n = neighbor.target
                    # Run until the goal is our current node
                    while n != start:
                        currentEntry = nodeDict[n.get_id()]
                        path.insert(0, currentEntry[0])
                        distance = distance + currentEntry[1]
                        n = currentEntry[0]
                    nodeList = []
                    break
                else:
                    nodeList.append(neighbor.target)

    return path, distance, len(visited), len(expanded)


def dfs(start, goal):
    """
    Depth-First search algorithm. The function is passed a start graph.Node object, a heuristic function, and a goal predicate.
    
    The start node can produce neighbors as needed, see graph.py for details.
    
    The goal is represented as a function, that is passed a node, and returns True if that node is a goal node, otherwise False. 
    
    The function should return a 4-tuple (path,distance,visited,expanded):
        - path is a sequence of graph.Edge objects that have to be traversed to reach a goal state from the start
        - distance is the sum of costs of all edges in the path 
        - visited is the total number of nodes that were added to the frontier during the execution of the algorithm 
        - expanded is the total number of nodes that were expanded, i.e. removed from the frontier to add their neighbors
    """
    nodeList = []
    expanded = []
    visited = []

    nodeDict = {}

    nodeList.append(start)
    visited.append(start)

    path = []
    distance = 0

    while len(nodeList) > 0:
        currentNode = nodeList.pop(0)
        expanded.append(currentNode)
        neighbors = currentNode.get_neighbors()
        for neighbor in neighbors:
            if neighbor.target not in visited:
                visited.append(neighbor.target)
                nodeEntry = [currentNode, neighbor.cost]
                nodeDict[neighbor.target.get_id()] = nodeEntry
                if goal(neighbor.target):
                    path.insert(0, neighbor.target)
                    n = neighbor.target
                    while n != start:
                        currentEntry = nodeDict[n.get_id()]
                        path.insert(0, currentEntry[0])
                        distance = distance + currentEntry[1]
                        n = currentEntry[0]
                    nodeList = []
                    break
                else:
                    nodeList.insert(0, neighbor.target)
                    if len(nodeList) > 10000:
                        print("Max stack size exceeded")
                        nodeList = []
                        break

    return path, distance, len(visited), len(expanded)


def greedy(start, heuristic, goal):
    """
    Greedy search algorithm. The function is passed a start graph.Node object, a heuristic function, and a goal predicate.

    The start node can produce neighbors as needed, see graph.py for details.

    The heuristic is a function that takes a node as a parameter and returns an estimate for how far that node is from the goal.

    The goal is also represented as a function, that is passed a node, and returns True if that node is a goal node, otherwise False.

    The function should return a 4-tuple (path,distance,visited,expanded):
        - path is a sequence of graph.Edge objects that have to be traversed to reach a goal state from the start
        - distance is the sum of costs of all edges in the path
        - visited is the total number of nodes that were added to the frontier during the execution of the algorithm
        - expanded is the total number of nodes that were expanded, i.e. removed from the frontier to add their neighbors
    """

    # Set of arrays needed for the implementations
    nodeList = []
    expanded = []
    visited = []

    # Using a dictionary to store nodes and its value
    nodeDict = {}

    # Start the list with the start node and heuristic
    nodeList.append((start, heuristic(start)))
    visited.append(start)

    # Set an empty array for the path
    path = []
    # Set the distance to 0
    distance = 0

    # Run until it reaches the destination
    while len(nodeList) > 0:
        # pop the next node in the list and make it current
        currentNode = nodeList.pop(0)
        # Take current node and add to expanded
        expanded.append(currentNode)
        # Get all the neighbors of the current node
        neighbors = currentNode[0].get_neighbors()
        # Run through all the neighbors
        for neighbor in neighbors:
            # Checks if the next neighbor node is visited
            if neighbor.target not in visited:
                # Put neighbor node in visited
                visited.append(neighbor.target)
                # (modified) Set the current node with its value to a variable
                nodeEntry = [currentNode[0], neighbor.cost]
                # Add the next current node to the dictionary
                nodeDict[neighbor.target.get_id()] = nodeEntry
                # Check if the neighbor node is our goal

                if goal(neighbor.target):
                    # add the goal to the path
                    path.insert(0, neighbor.target)
                    n = neighbor.target
                    # Run until the goal is our current node
                    while n != start:
                        currentEntry = nodeDict[n.get_id()]
                        path.insert(0, currentEntry[0])
                        distance = distance + currentEntry[1]
                        n = currentEntry[0]
                        nodeList = []
                    break
                else:
                    # (modified)
                    nodeList.append((neighbor.target, heuristic(neighbor.target)))
                    if (len(nodeList) > 1000):
                        nodeList = []
                        break

        # (new) Sort list by the value of heuristics in ascending order.
        nodeList.sort(key=lambda a: a[1])


    return path, distance, len(visited), len(expanded)


def astar(start, heuristic, goal):
    """
    A* search algorithm. The function is passed a start graph.Node object, a heuristic function, and a goal predicate.

    The start node can produce neighbors as needed, see graph.py for details.

    The heuristic is a function that takes a node as a parameter and returns an estimate for how far that node is from the goal.

    The goal is also represented as a function, that is passed a node, and returns True if that node is a goal node, otherwise False.

    The function should return a 4-tuple (path,distance,visited,expanded):
        - path is a sequence of graph.Edge objects that have to be traversed to reach a goal state from the start
        - distance is the sum of costs of all edges in the path
        - visited is the total number of nodes that were added to the frontier during the execution of the algorithm
        - expanded is the total number of nodes that were expanded, i.e. removed from the frontier to add their neighbors
    """
    # Set of arrays needed for the implementations
    nodeList = []
    expanded = []
    visited = []

    # Using a dictionary to store nodes and its value
    nodeDict = {}

    # Start the list with the start node and heuristic
    nodeList.append((start, heuristic(start)))
    visited.append(start)

    # Set an empty array for the path
    path = []
    # Set the distance to 0
    distance = 0

    # (new) Sort list by the value of heuristics in ascending order.
    nodeList.sort(key=lambda a: a[1])

    # Run until it reaches the destination
    while len(nodeList) > 0:
        # pop the next node in the list and make it current
        currentNode = nodeList.pop(0)
        # Take current node and add to expanded
        expanded.append(currentNode)
        # Get all the neighbors of the current node
        neighbors = currentNode[0].get_neighbors()
        # Run through all the neighbors
        for neighbor in neighbors:
            # Checks if the next neighbor node is visited
            if neighbor.target not in visited:
                # Put neighbor node in visited
                visited.append(neighbor.target)
                # (modified) Set the current node with its value to a variable
                nodeEntry = [currentNode[0], neighbor.cost]
                # Add the next current node to the dictionary
                nodeDict[neighbor.target.get_id()] = nodeEntry
                # Check if the neighbor node is our goal

                if goal(neighbor.target):
                    # add the goal to the path
                    path.insert(0, neighbor.target)
                    n = neighbor.target
                    # Run until the goal is our current node
                    while n != start:
                        currentEntry = nodeDict[n.get_id()]
                        path.insert(0, currentEntry[0])
                        distance = distance + currentEntry[1]
                        n = currentEntry[0]
                        nodeList = []
                    break
                else:
                    # (modified)
                    nodeList.append((neighbor.target, heuristic(neighbor.target)))
                    if (len(nodeList) > 1000):
                        nodeList = []
                        break

    return path, distance, len(visited), len(expanded)


def run_all(name, start, heuristic, goal):
    print("running test", name)
    print("Breadth-First Search")
    result = bfs(start, goal)
    print_path(result)

    print("\nDepth-First Search")
    result = dfs(start, goal)
    print_path(result)

    print("\nGreedy Search (default heuristic)")
    result = greedy(start, default_heuristic, goal)
    print_path(result)

    print("\nGreedy Search")
    result = greedy(start, heuristic, goal)
    print_path(result)

    print("\nA* Search (default heuristic)")
    result = astar(start, default_heuristic, goal)
    print_path(result)

    print("\nA* Search")
    result = astar(start, heuristic, goal)
    print_path(result)

    print("\n\n")


def print_path(result):
    (path, cost, visited_cnt, expanded_cnt) = result
    print("visited nodes:", visited_cnt, "expanded nodes:", expanded_cnt)
    if path:
        print("Path found with cost", cost)
        for n in path:
            print(n.name)
    else:
        print("No path found")
    print("\n")


def main():
    """
    You are free (and encouraged) to change this function to add more test cases.
    
    You are provided with three test cases:
        - pathfinding in Austria, using the map shown in class. This is a relatively small graph, but it comes with an admissible heuristic. Below astar is called using that heuristic, 
          as well as with the default heuristic (which always returns 0). If you implement A* correctly, you should see a small difference in the number of visited/expanded nodes between the two heuristics.
        - pathfinding on an infinite graph, where each node corresponds to a natural number, which is connected to its predecessor, successor and twice its value, as well as half its value, if the number is even.
          e.g. 16 is connected to 15, 17, 32, and 8. The problem given is to find a path from 1 to 2050, for example by doubling the number until 2048 is reached and then adding 1 twice. There is also a heuristic 
          provided for this problem, but it is not admissible (think about why), but it should result in a path being found almost instantaneously. On the other hand, if the default heuristic is used, the search process 
          will take a noticeable amount (a couple of seconds).
        - pathfinding on the same infinite graph, but with infinitely many goal nodes. Each node corresponding to a number greater 1000 that is congruent to 63 mod 123 is a valid goal node. As before, a non-admissible
          heuristic is provided, which greatly accelerates the search process. 
    """
    target = "Bregenz"

    def atheuristic(n):
        return graph.AustriaHeuristic[target][n.get_id()]

    def atgoal(n):
        return n.get_id() == target

    run_all("Austria", graph.Austria["Eisenstadt"], atheuristic, atgoal)

    target = 2050

    def infheuristic(n):
        return abs(n.get_id() - target)

    def infgoal(n):
        return n.get_id() == target

    run_all("Infinite Graph (simple)", graph.InfNode(1), infheuristic, infgoal)

    def multiheuristic(n):
        return abs(n.get_id() % 123 - 63)

    def multigoal(n):
        return n.get_id() > 1000 and n.get_id() % 123 == 63

    run_all("Infinite Graph (multi)", graph.InfNode(1), multiheuristic, multigoal)


if __name__ == "__main__":
    main()
