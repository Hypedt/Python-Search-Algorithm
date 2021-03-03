

class Node:
    def get_id(self):
        """
        Returns a unique identifier for the node (for example, the name, the hash value of the contents, etc.), used to compare two nodes for equality.
        """
        return ""
    def get_neighbors(self):
        """
        Returns all neighbors of a node, and how to reach them. The result is a list Edge objects, each of which contains 3 attributes: target, cost and name, 
        where target is a Node object, cost is a numeric value representing the distance between the two nodes, and name is a string representing the path taken to the neighbor.
        """
        return []
    def __eq__(self, other):
        return self.get_id() == other.get_id()
        
class Edge:
    """
    Abstraction of a graph edge. Has a target (Node that the edge leads to), a cost (numeric) and a name (string), which can be used to print the edge.
    """
    def __init__(self, target, cost, name):
        self.target = target 
        self.cost = cost
        self.name = name

class GeomNode(Node):
    """
    Representation of a finite graph in which all nodes are kept in memory at all times, and stored in the node's neighbors field.
    """
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def get_neighbors(self):
        return self.neighbors
    def get_id(self):
        return self.name
        
class InfNode(Node):
    """
    Infinite graph, in which every node represents an integer, and neighbors are generated on demand. Note that Nodes are not cached, i.e. if you
    request the neighbors of node 1, and the neighbors of node 3, both will contain the node 2, but they will be using two distinct objects. 
    """
    def __init__(self, nr):
        self.nr = nr
    def get_neighbors(self):
        result = [Edge(InfNode(self.nr-1),1,("%d - -1 - %d"%(self.nr,self.nr-1))), Edge(InfNode(self.nr+1),1,("%d - +1 - %d"%(self.nr,self.nr+1))), Edge(InfNode(self.nr*2),1,("%d - *2 - %d"%(self.nr,self.nr*2)))]
        if self.nr%2 == 0:
            result.append(Edge(InfNode(self.nr//2),1,("%d - /2 - %d"%(self.nr,self.nr//2))))
        return result
    def get_id(self):
        return self.nr


def make_geom_graph(nodes, edges):
    """
    Given a list of nodes and edges (with distances), creates a dictionary of Node objects 
    representing the graph. Note that the resulting graph is directed, but each edge will be 
    replaced with *two* directed edges (to and from).
    """
    result = {}
    for c in nodes:
        result[c] = GeomNode(c)
    for (a,b,d) in edges:
        result[a].neighbors.append(Edge(result[b], d, "%s - %s"%(a,b)))
        result[b].neighbors.append(Edge(result[a], d, "%s - %s"%(b,a)))
    return result
    
Austria = make_geom_graph(
    ["Graz", "Vienna", "Salzburg", "Innsbruck", "Munich", "Bregenz", "Linz", "Eisenstadt", "Klagenfurt", "Lienz", "Bruck"],
    [("Graz", "Bruck", 55.0),
     ("Graz", "Klagenfurt", 136.0),
     ("Graz", "Vienna", 200.0),
     ("Graz", "Eisenstadt", 173.0),
     ("Bruck", "Klagenfurt", 152.0),
     ("Bruck", "Salzburg", 215.0),
     ("Bruck", "Linz", 195.0),
     ("Bruck", "Vienna", 150.0),
     ("Vienna", "Eisenstadt", 60.0),
     ("Vienna", "Linz", 184.0),
     ("Linz", "Salzburg", 123.0),
     ("Salzburg", "Munich", 145.0),
     ("Salzburg", "Klagenfurt", 223.0),
     ("Klagenfurt", "Lienz", 145.0),
     ("Lienz", "Innsbruck", 180.0),
     ("Munich", "Innsbruck", 151.0),
     ("Munich", "Bregenz", 180.0),
     ("Innsbruck", "Bregenz", 190.0)])
     
AustriaHeuristic = { 
   "Graz":       {"Graz": 0.0,   "Vienna": 180.0, "Eisenstadt": 150.0, "Bruck": 50.0,  "Linz": 225.0, "Salzburg": 250.0, "Klagenfurt": 125.0, "Lienz": 270.0, "Innsbruck": 435.0, "Munich": 375.0, "Bregenz": 450.0},
   "Vienna":     {"Graz": 180.0, "Vienna": 0.0,   "Eisenstadt": 50.0,  "Bruck": 126.0, "Linz": 175.0, "Salzburg": 285.0, "Klagenfurt": 295.0, "Lienz": 400.0, "Innsbruck": 525.0, "Munich": 407.0, "Bregenz": 593.0},
   "Eisenstadt": {"Graz": 150.0, "Vienna": 50.0,  "Eisenstadt": 0.0,   "Bruck": 171.0, "Linz": 221.0, "Salzburg": 328.0, "Klagenfurt": 335.0, "Lienz": 437.0, "Innsbruck": 569.0, "Munich": 446.0, "Bregenz": 630.0},
   "Bruck":      {"Graz": 50.0,  "Vienna": 126.0, "Eisenstadt": 171.0, "Bruck": 0.0,   "Linz": 175.0, "Salzburg": 201.0, "Klagenfurt": 146.0, "Lienz": 287.0, "Innsbruck": 479.0, "Munich": 339.0, "Bregenz": 521.0},
   "Linz":       {"Graz": 225.0, "Vienna": 175.0, "Eisenstadt": 221.0, "Bruck": 175.0, "Linz": 0.0,   "Salzburg": 117.0, "Klagenfurt": 311.0, "Lienz": 443.0, "Innsbruck": 378.0, "Munich": 265.0, "Bregenz": 456.0},
   "Salzburg":   {"Graz": 250.0, "Vienna": 285.0, "Eisenstadt": 328.0, "Bruck": 201.0, "Linz": 117.0, "Salzburg": 0.0,   "Klagenfurt": 201.0, "Lienz": 321.0, "Innsbruck": 265.0, "Munich": 132.0, "Bregenz": 301.0},
   "Klagenfurt": {"Graz": 125.0, "Vienna": 295.0, "Eisenstadt": 335.0, "Bruck": 146.0, "Linz": 311.0, "Salzburg": 201.0, "Klagenfurt": 0.0,   "Lienz": 132.0, "Innsbruck": 301.0, "Munich": 443.0, "Bregenz": 465.0},
   "Lienz":      {"Graz": 270.0, "Vienna": 400.0, "Eisenstadt": 437.0, "Bruck": 287.0, "Linz": 443.0, "Salzburg": 321.0, "Klagenfurt": 132.0, "Lienz": 0.0,   "Innsbruck": 157.0, "Munich": 298.0, "Bregenz": 332.0},
   "Innsbruck":  {"Graz": 435.0, "Vienna": 525.0, "Eisenstadt": 569.0, "Bruck": 479.0, "Linz": 378.0, "Salzburg": 265.0, "Klagenfurt": 301.0, "Lienz": 157.0, "Innsbruck": 0.0,   "Munich": 143.0, "Bregenz": 187.0},
   "Munich":     {"Graz": 375.0, "Vienna": 407.0, "Eisenstadt": 446.0, "Bruck": 339.0, "Linz": 265.0, "Salzburg": 132.0, "Klagenfurt": 443.0, "Lienz": 298.0, "Innsbruck": 143.0, "Munich": 0.0,   "Bregenz": 165.0},
   "Bregenz":    {"Graz": 450.0, "Vienna": 593.0, "Eisenstadt": 630.0, "Bruck": 521.0, "Linz": 456.0, "Salzburg": 301.0, "Klagenfurt": 465.0, "Lienz": 332.0, "Innsbruck": 187.0, "Munich": 165.0, "Bregenz": 0.0}}

TestCase = make_geom_graph(
    ["San Diego", "Temecula", "Oceanside", "Irvine", "Santa Ana", "Los Angeles","Palm Springs", "Pomona", "Santa Monica", "Santa Barbara", "Lancaster", "Bakersfield" ],
    [("San Diego", "Temecula", 59.0),
     ("San Diego", "Oceanside", 38.0),
     ("Temecula", "Oceanside", 30.0),
     ("Temecula", "Palm Springs", 81.0),
     ("Temecula", "Pomona", 58.0),
     ("Oceanside","Irvine", 48.0),
     ("Irvine", "Santa Ana", 8.0),
     ("Santa Ana","Pomona", 26.0),
     ("Santa Ana","Los Angeles",32.0),
     ("Santa Ana","Santa Monica", 46.0),
     ("Pomona", "Palm Springs", 79.0),
     ("Pomona", "Lancaster", 94.0),
     ("Pomona", "Los Angeles", 30.0),
     ("Los Angeles", "Lancaster", 70.0),
     ("Los Angeles", "Bakersfield", 111.0),
     ("Los Angeles", "Santa Monica", 16.0),
     ("Santa Monica", "Santa Barbara", 87.0),
     ("Lancaster", "Bakersfield", 87.0)])

TestCaseHeuristic = {
    "San Diego":    {"San Diego": 0.0, "Temecula": 120.0, "Oceanside": 160.0, "Irvine": 210.0, "Santa Ana": 240.0, "Los Angeles": 270.0, "Palm Springs": 320.0, "Pomona": 370.0, "Santa Monica": 410.0, "Santa Barbara": 440.0, "Lancaster": 470.0, "Bakersfield": 550.0},
    "Temecula":     {"San Diego": 120.0, "Temecula": 0.0, "Oceanside": 110.0, "Irvine": 150.0, "Santa Ana": 180.0, "Los Angeles": 220.0, "Palm Springs": 290.0, "Pomona": 350.0, "Santa Monica": 460.0, "Santa Barbara": 520.0, "Lancaster": 550.0, "Bakersfield": 600.0},
    "Oceanside":    {"San Diego": 160.0, "Temecula": 110.0, "Oceanside": 0.0, "Irvine": 140.0, "Santa Ana": 190.0, "Los Angeles": 260.0, "Palm Springs": 300.0, "Pomona": 350.0, "Santa Monica": 400.0, "Santa Barbara": 460.0, "Lancaster": 520.0, "Bakersfield": 570.0},
    "Irvine":       {"San Diego": 210.0, "Temecula": 150.0, "Oceanside": 140.0, "Irvine": 0.0, "Santa Ana": 100.0, "Los Angeles": 150.0, "Palm Springs": 190.0, "Pomona": 220.0, "Santa Monica": 270.0, "Santa Barbara": 350.0, "Lancaster": 410.0, "Bakersfield": 460.0},
    "Santa Ana":    {"San Diego": 240.0, "Temecula": 180.0, "Oceanside": 190.0, "Irvine": 100.0, "Santa Ana": 0.0, "Los Angeles": 120.0, "Palm Springs": 170.0, "Pomona": 210.0, "Santa Monica": 250.0, "Santa Barbara": 320.0, "Lancaster": 360.0, "Bakersfield": 410.0},
    "Los Angeles":  {"San Diego": 270.0, "Temecula": 220.0, "Oceanside": 260.0, "Irvine": 150.0, "Santa Ana": 120.0, "Los Angeles": 0.0, "Palm Springs": 130.0, "Pomona": 170.0, "Santa Monica": 210.0, "Santa Barbara": 260.0, "Lancaster": 330.0, "Bakersfield": 390.0},
    "Palm Springs": {"San Diego": 320.0, "Temecula": 290.0, "Oceanside": 300.0, "Irvine": 190.0, "Santa Ana": 170.0, "Los Angeles": 130.0, "Palm Springs": 0.0, "Pomona": 110.0, "Santa Monica": 160.0, "Santa Barbara": 210.0, "Lancaster": 280.0, "Bakersfield": 350.0},
    "Pomona":       {"San Diego": 370.0, "Temecula": 350.0, "Oceanside": 350.0, "Irvine": 220.0, "Santa Ana": 210.0, "Los Angeles": 170.0, "Palm Springs": 110.0, "Pomona": 0.0, "Santa Monica": 130.0, "Santa Barbara": 170.0, "Lancaster": 240.0, "Bakersfield": 290.0},
    "Santa Monica": {"San Diego": 410.0, "Temecula": 460.0, "Oceanside": 400.0, "Irvine": 270.0, "Santa Ana": 250.0, "Los Angeles": 210.0, "Palm Springs": 160.0, "Pomona": 130.0, "Santa Monica": 0.0, "Santa Barbara": 150.0, "Lancaster": 210.0, "Bakersfield": 250.0},
    "Santa Barbara":{"San Diego": 440.0, "Temecula": 520.0, "Oceanside": 460.0, "Irvine": 350.0, "Santa Ana": 320.0, "Los Angeles": 260.0, "Palm Springs": 210.0, "Pomona": 170.0, "Santa Monica": 150.0, "Santa Barbara": 0.0, "Lancaster": 120.0, "Bakersfield": 190.0},
    "Lancaster":    {"San Diego": 470.0, "Temecula": 550.0, "Oceanside": 520.0, "Irvine": 410.0, "Santa Ana": 360.0, "Los Angeles": 330.0, "Palm Springs": 280.0, "Pomona": 240.0, "Santa Monica": 210.0, "Santa Barbara": 120.0, "Lancaster": 0.0, "Bakersfield": 130.0},
    "Bakersfield":  {"San Diego": 550.0, "Temecula": 600.0, "Oceanside": 570.0, "Irvine": 460.0, "Santa Ana": 410.0, "Los Angeles": 390.0, "Palm Springs": 350.0, "Pomona": 290.0, "Santa Monica": 250.0, "Santa Barbara": 190.0, "Lancaster": 130.0, "Bakersfield": 0.0}}
