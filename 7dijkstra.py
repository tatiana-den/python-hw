class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.previousVertex = None
        self.minDistance = float('inf')
        self.edges = []

    def __lt__(self, other):
        if self.minDistance < other.minDistance:
            return True
        else:
            return False

    def __le__(self, other):
        if self.minDistance <= other.minDistance:
            return True
        else:
            return False


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.vertexes = None
        self.edgesToVertexes = None

    def computePath(self, sourceId):
        self.resetDijkstra()
        self.vertexes[sourceId].minDistance = 0
        heap = []
        myset = set()
        self.vertexes[sourceId].minDistance = 0
        heapPush(heap, self.vertexes[sourceId])
        while heap:
            elem = heapPop(heap)
            myset.add(elem)
            for edge in elem.edges:
                if self.vertexes[edge.target].minDistance > elem.minDistance + edge.weight:
                    self.vertexes[edge.target].minDistance = elem.minDistance + edge.weight
                    self.vertexes[edge.target].previousVertex = elem
                    if self.vertexes[edge.target] in heap:
                        seaveUp(heap, self.vertexes[edge.target])
                if self.vertexes[edge.target] not in myset and self.vertexes[edge.target] not in heap:
                    heapPush(heap, self.vertexes[edge.target])

    def getShortestPathTo(self, targetId):
        current = self.vertexes[targetId]
        if current is None:
            return []
        if self.vertexes[targetId].previousVertex is not None:
            return self.getShortestPathTo(self.vertexes[targetId].previousVertex.id) + [self.vertexes[targetId]]
        else:
            return [self.vertexes[targetId]]

    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = vertexes
        self.edgesToVertexes = edgesToVertexes
        for i in self.vertexes:
            i.previousVertex = None
            i.minDistance = float('inf')
            i.edges = []
        for i in edgesToVertexes:
            self.vertexes[i.source].edges.append(i)

    def resetDijkstra(self):
        for i in self.vertexes:
            i.minDistance = float('inf')
            i.previousVertex = None

    def getVertexes(self):
        return self.vertexes


def heapPop(heap):
    if len(heap) == 1:
        return heap.pop()
    val = heap[0]
    heap[0] = heap.pop()
    i = 0
    while 2 * i + 2 < len(heap) and heap[i] > min(heap[2 * i + 1], heap[2 * i + 2]):
        if heap[2 * i + 1] < heap[2 * i + 2]:
            heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
            i = 2 * i + 1
        else:
            heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]
            i = 2 * i + 2
    if 2 * i + 1 == len(heap) - 1 and heap[i] > heap[2 * i + 1]:
        heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
    return val


def seaveUp(heap, elem):
    index = heap.index(elem)
    parent = (index - 1) // 2
    while heap[index] <= heap[parent] and index != 0:
        if heap[index] <= heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
        parent = (index - 1) // 2


def heapPush(heap, elem):
    heap.append(elem)
    seaveUp(heap, elem)
