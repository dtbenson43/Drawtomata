from automataUtilities import angleClockwise, distance, pointPos, angleBase
import tkinter as tk

class Transition:
  def __init__(self, originState=None, destinationState=None, symbols=None, canvas=None):
    self.state = originState
    self.nextState = destinationState
    self.symbols = symbols
    self.canvas = canvas

  def setCanvas(self, canvas):
    self.canvas = canvas

  def getOriginState(self):
    return self.state

  def getNextState(self):
    return self.nextState

  def getSymbols(self):
    return self.symbols

  def testSymbol(self, symbol):
    return True if symbol in self.symbols else False

  def angleToDirection(self, angle):
    left = (135, 225)
    up = (225, 315)
    right = (315, 45)
    down = (45, 135)
    direction = "right"
    if angle >= left[0] and angle <= left[1]:
      direction = "left"
    elif angle >= up[0] and angle <= up[1]:
      direction = "up"
    elif angle >= right[0] or angle <= right[1]:
      direction = "right"
    elif angle >= down[0] and angle <= down[1]:
      direction = "down"
    return direction

  def draw(self, startState, endState):
    lineBuffer = 5
    distanceBuffer = 40
    nodeSize = self.canvas.grid.nodeSize

    nextNodeDict = {
      "left": self.canvas.grid.getNodeLeft,
      "up": self.canvas.grid.getNodeAbove,
      "right": self.canvas.grid.getNodeRight,
      "down": self.canvas.grid.getNodeBelow
    }

    startLoc = startState.getCenter()
    endLoc = endState.getCenter()
    diameter = startState.getDiameter()

    if startLoc[0] == endLoc[0] and startLoc[0] == endLoc[0]:
      first = (startLoc[0]+(diameter / 2), startLoc[1]+(diameter / 2))
      second = (first[0] + diameter, first[1] + diameter)
      self.canvas.create_line(first, second)
      return

    angle = angleClockwise(startLoc, endLoc)
    direction = self.angleToDirection(angle)

    startNode = nextNodeDict[direction](startLoc[0]+5, startLoc[1]+5)
    startNode = self.canvas.grid.nextClosestFreeNode(startNode[0], startNode[1], True)
    node = startNode
    prevNode = startNode
    points = [startLoc, (node[0] + (nodeSize / 2), node[1] + (nodeSize / 2))]
    self.canvas.grid.occupyNode(node[0], node[1])

    count = 1
    while distance((node[0], node[1]), endLoc) > distanceBuffer:
      count += 1
      angle = angleClockwise((node[0], node[1]), endLoc)
      direction = self.angleToDirection(angle)
      tempNode = nextNodeDict[direction](node[0], node[1])

      if tempNode == False or tempNode[4] == False:
        node = self.canvas.grid.nextClosestFreeNode(node[0], node[1], True)
      else:
        node = tempNode

      points.append((node[0] + (nodeSize / 1.2), node[1] + (nodeSize / 1.2)))
      self.canvas.grid.occupyNode(node[0], node[1])

    endAngle = angleClockwise(points[len(points)-1], endLoc)
    print(endAngle)
    endPoint = pointPos(endLoc[0], endLoc[1], diameter / 2, endAngle+180)
    points.append(endPoint)
    labelidx = 3 if len(points) >= 4 else 1
    labelPoint = points[labelidx]
    self.canvas.create_text(labelPoint[0]+4, labelPoint[1]+7, text=(", ".join(self.symbols)))
    self.canvas.create_line(points, smooth=False, arrow=tk.LAST)

