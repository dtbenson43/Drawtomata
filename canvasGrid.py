import math
from automataUtilities import roundDown, roundUp, distance

class CanvasGrid:
    def __init__(self, width=0, height=0, nodeSize=10):
        self.width = width
        self.height = height
        self.nodeSize = nodeSize
        self.widthNodes = int(width / nodeSize)
        self.heightNodes = int(width / nodeSize)
        self.numNodes = self.widthNodes * self.heightNodes
        self.fill = len(str(self.width if self.width > self.height else self.height))
        self.nodes = {}
        self.buildGrid()

    def buildGrid(self):
        for i in range(self.widthNodes):
            i = i*10
            for j in range(self.heightNodes):
                j = j*10
                self.nodes[str(j).zfill(self.fill)+str(i).zfill(self.fill)] = (j, i, j+self.nodeSize-1, i+self.nodeSize-1, True)

    def getNode(self, x, y):
      x = int(roundDown(x, self.nodeSize))
      y = int(roundDown(y, self.nodeSize))
      key = str(x).zfill(self.fill)+str(y).zfill(self.fill)
      return self.nodes[key] if key in self.nodes else False

    def getNodeAbove(self, x, y):
      x = roundDown(x, self.nodeSize)
      y = roundDown(y - self.nodeSize, self.nodeSize)
      return self.getNode(x, y)

    def getNodeBelow(self, x, y):
      x = roundDown(x, self.nodeSize)
      y = roundDown(y + self.nodeSize, self.nodeSize)
      return self.getNode(x, y)

    def getNodeLeft(self, x, y):
      x = roundDown(x - self.nodeSize, self.nodeSize)
      y = roundDown(y, self.nodeSize)
      return self.getNode(x, y)

    def getNodeRight(self, x, y):
      x = roundDown(x + self.nodeSize, self.nodeSize)
      y = roundDown(y, self.nodeSize)
      return self.getNode(x, y)

    def isNodeFree(self, x, y):
      node = self.getNode(x, y)
      return node[4] if node != False else False

    def isNodeAboveFree(self, x, y):
      node = self.getNodeAbove(x, y)
      return node[4] if node != False else False

    def isNodeBelowFree(self, x, y):
      node = self.getNodeBelow(x, y)
      return node[4] if node != False else False

    def isNodeLeftFree(self, x, y):
      node = self.getNodeLeft(x, y)
      return node[4] if node != False else False

    def isNodeRightFree(self, x, y):
      node = self.getNodeRight(x, y)
      return node[4] if node != False else False

    def isBoxFree(self, x, y, size):
      size = roundUp(size, self.nodeSize)
      numNodes = int(size / self.nodeSize)
      for i in range(numNodes):
        for j in range(numNodes):
          node = self.getNode(x + (i*self.nodeSize), y + (j*self.nodeSize))
          if node == False or node[4] == False:
            return False
      return True

    def setNode(self, newNode):
      key = str(newNode[0]).zfill(self.fill)+str(newNode[1]).zfill(self.fill)
      if self.getNode(newNode[0], newNode[1]) != False:
        self.nodes[key] = newNode

    def occupyNode(self, x, y):
      node = self.getNode(x, y)
      if node != False:
        newNode = (node[0], node[1], node[2], node[3], False)
        self.setNode(newNode)

    def freeNode(self, x, y):
      node = self.getNode(x, y)
      if node != False:
        newNode = (node[0], node[1], node[2], node[3], True)
        self.setNode(newNode)

    def occupyBox(self, x, y, size):
      size = roundUp(size, self.nodeSize)
      numNodes = int(size / self.nodeSize)
      for i in range(numNodes):
        for j in range(numNodes):
          self.occupyNode(x + (i*self.nodeSize), y + (j*self.nodeSize))

    def nextClosestFreeNode(self, x, y, center=False):
      node = self.getNode(0, 0)
      nodeDistance = 999999999
      for key in self.nodes:
        if self.nodes[key][4] == False:
          continue
        x2 = self.nodes[key][0] + (self.nodeSize/2) if center == True else self.nodes[key][0]
        y2 = self.nodes[key][1] + (self.nodeSize/2) if center == True else self.nodes[key][1]
        dist = distance((x, y), (x2, y2))
        if dist < nodeDistance:
          nodeDistance = dist
          node = self.nodes[key]
      return node


    