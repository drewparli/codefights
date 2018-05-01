"""
Quick note:
Even though this is a shortest solutions challenge, I would also appreciate seeing some fast algorithms here!

As an evil mastermind and a casual Plague Inc player, your goal is to destroy all form of life on Earth. There are many ways to do this, but currently the "cheapest" method is to release a contagious virus to the population.

The downside? Nobody is giving you money for this (Why would they lend you money for destroying the world?) and making the virus is expensive, each day of the outbreak adds up the cost. Not only that, the virus isn't effective, and can only spread to an infected person's family and friends every day.

Thankfully, you have been given a matrix of relationships, where people[i] represents the relationship between person[i][0] and everyone in the list (ex: [0,1,3,4] for person[0] means 0 is friends with 1,3, and 4) (NOTE: Friendship is both ways, no need to think about pretending to be their friend). Now all you have to do is to find who you should infect first to infect everyone!

You must return the number of he person that will take the least amount of days to infect the world. If there are ties, return the smaller value.

Note: If not everyone can be infected (ex: Someone with no friends or family :c ), return -1
"""
class Node(object):

    def __init__(self, uid, relations):
        self.uid = uid
        self.cost = 0
        self.relations = set()
        if relations:
            self.addRelations(relations)
        else:
            raise RuntimeError("unreachable")
        self.reachable = set()

    def __str__(self):
        return "NODE(uid={}, relations={})".format(self.uid, self.relations)

    def addRelations(self, relations):
        for r in relations:
            self.relations.add(r)

class Graph(object):

    def __init__(self, people):
        self.size = len(people)
        self.nodes = dict()
        self.addNodes(people)

    def __str__(self):
        nodes = list(self.nodes.values())
        return "GRAPH(\n  size={},\n  nodes=[\n    {}]\n)".format(self.size, "\n    ".join(map(str, nodes)))

    def addNodes(self, people):
        for (i, relations) in enumerate(people):
            n = Node(i, relations)
            self.nodes[i] = n

    def findCosts(self):
        for n in self.nodes.values():
            n.cost = self.search(n)

    def search(self, node):
        #TODO this function is not done yet...
        for i in node.relations:
            self.nodes[i].relations


def test5():
    people = [[0,1,2],
              [1,0,2],
              [2,1,0],
              [3,5,4],
              [4,3,5],
              [5,4,3]]
    try:
        g = Graph(people)
        print(str(g))
    except RuntimeError as msg:
        print(msg)



if __name__ == '__main__':
    test5()