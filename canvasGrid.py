from automataUtilities import roundDown

class CanvasGrid:
    def __init__(self, width=0, height=0, nodeSize=10):
        self.width = width
        self.height = height
        self.nodeSize = nodeSize
        self.widthNodes = int(width / nodeSize)
        self.heightNodes = int(width / nodeSize)
        self.numNodes = self.widthNodes * self.heightNodes
        self.nodes = {}
        self.buildGrid()

    def buildGrid(self):
        n = self.width if self.width > self.height else self.height
        n = len(str(n))
        print(n)
        for i in range(self.widthNodes):
            i = i*10
            for j in range(self.heightNodes):
                j = j*10
                self.nodes[str(j).zfill(n)+str(i).zfill(n)] = (j, i, j+9, i+9, False)
        print(self.nodes)