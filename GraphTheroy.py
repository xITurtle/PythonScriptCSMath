class DirectedWeightedGraph:

    # TODO Add Weights
    def __init__(self, nodesParam, connectionsParam):
        self.connections = [()]
        self.nodes = []
        for i in nodesParam:
            self.nodes.append(i)
        for i in connectionsParam:
            self.connections.append(i)

    def is_connected(nodeStart, nodeEnd):
        pass

    def find_connection(nodeStart, nodeEnd):
        pass

    def find_lightest_way(nodeStart, nodeEnd):
        pass
