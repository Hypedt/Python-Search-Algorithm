# Python-Search-Algorithm
Lab 1
Python
Search Algorithms
Report
Submission
Lab 1: Search, deadline: March 2nd, AoE

# Python
To complete this lab, you will need Python 3. The code should work with any recent version of Python 3, but if you have one that is older than 3.5 you may want to update (it should still work, but I have not tested it). I recommend a standalone installation with Python added to your system’s search path, so you can run python from your system’s command line. Once you have downloaded the framework (described below), you can run it with python pathfinding.py from your development directory. You can also set up an editor like Atom or VSCode to automatically run this file (personally, I use Notepad++ and run the code from the command line, and can only provide limited support for other environments).

If you are new to Python, check out the official tutorial, Python for Java Programmers, and/or Kate Compton’s Python cheatsheet.

# Search Algorithms
In this lab, you will implement four “different” (directed) graph search algorithms in Python:

Breadth-First Search
Depth-First Search
Greedy Search
A*
Each of these algorithms takes a graph, represented as an initial node that can produce its neighbors, and a goal predicate/function that tells you when you have reached a goal node. The last two algorithms additionally get a heuristic that tells you how close a node is estimated to be to the goal.

To get started download this zip file, which contains two python files: pathfinding.py and graph.py. Your main task is to modify pathfinding.py, but you can and should use graph.py to come up with more test cases!

The graph representation is implemented in graph.py, and does not have to be modified. If you modify graph.py, please do not change Node and Edge and their interfaces. When in doubt what you can change, ask. For this task, you only have to implement four functions: bfs(start, goal), dfs(start, goal), greedy(start, heuristic, goal) and astar(start, heuristic, goal). The result of each of the functions should be four values:

The path, represented as a sequence of Edge objects
The total length of the path as a number
The number of nodes visited, i.e. added to the frontier, during search
The number of nodes expanded, i.e. removed from the frontier, during search If no path is found, the first two values should be None, but the number of visited and expanded nodes should still be reported.
Note that all four functions have the same basic structure, and only differ in how they select which node to expand next, i.e. which data structure they use for the frontier. You could implement a base search function and pass it the appropriate data structure to get each of the four algorithms, or you can implement them individually.

As mentioned above, the graph is not represented explicitly, instead only a single Node object is passed to the algorithm, which has a method get_neighbors which returns a list of Edge objects representing outgoing edges. Each Edge object stores its target, the cost to use the edge, and its name (used for printing the path). The target is another Node object, which can then in turn be asked for its own neighbors, and so on. Note that to simplify development, nodes do not need to be cached between calls, and are instead identified by a unique id, which can be obtained from the get_id method. graph.py shows how this representation can be used to represent finite and infinite graphs.

Mandatory functions in pathfinding.py, following the API described there (and above):

bfs
dfs
greedy
astar
Do not remove or change the default_heuristic in pathfinding.py. Come up with at least one graph of your own and test the four algorithms on it. This could be a map of your home town or your favorite video game, some interesting graph of websites you frequent, or anything else you can think of. Try to define a reasonable heuristic, and see how it affects performance (you can use the run_all function for testing, which will run greedy search and A* with the default heuristic as well as with the provided heuristic).

The Austria graph follows this approximate map:



# Report
Your report should consist of three sections:

Briefly describe how you implemented the four algorithms, and any challenges you encountered. 

How do you determine loops? How do you determine that you can not find a path?

How did the four algorithms perform on the given test problems? 

Which algorithm visits/expands the least nodes, which one finds the shortest path? Any surprises? Also note any additional tests you performed on the given test graphs.

Describe the additional test graph (or graphs!) you added. For small-ish graphs (less than 20 nodes), include a graphical representation. 
For larger (or even infinite) graphs, a textual or mathematical description will suffice. What search problems did you define on this graph, and how did the algorithms perform?

# Submission
Submit the finished code (all python files you have!), and your report pdf in a single zip file on Blackboard. Do not forget to put the names and BroncoIDs of both team members in the report as well! Only one of you has to submit, but if both do, please make sure you submit the same file, or I will pick one at random.
