from tkinter import Canvas, BOTH
from automata import Automata
from canvasGrid import CanvasGrid

class AutomataCanvas(Canvas):
  def __init__(self, frame=None, data=None, automata=None, width=0, height=0):
    if frame == None:
      raise ValueError('ERROR: no frame')

    super().__init__(
      frame,
      width=width,
      height=height,
      borderwidth=0,
      highlightthickness=0
    )
    self.pack(fill=BOTH, expand=1)

    self.width = width
    self.height = height
    self.automata = automata if automata != None else Automata(data)
    self.grid = CanvasGrid(width=width, height=height)
    # self.drawGrid()s
    self.drawCircle()

  def drawAutomata(self):
    state = self.automata.states[self.automata.startState]
    self.drawState(state, [])
  
  def drawGrid(self):
    for x in range(int(51)):
      self.create_line(x*10, 0, x*10, 500)
    for y in range(int(51)):
      self.create_line(0, y*10, 500, y*10)

  def drawState(self, state, drawn):
    if state.id not in drawn:
      drawn.append(state.id)
      # print(drawn)
      for symbol in state.transitions:
        nextStateId = state.transitions[symbol]
        nextState = self.automata.states[nextStateId]
        self.drawState(nextState, drawn)


  def drawCircle(self):
    self.test = self.create_oval(0, 0, 39, 39, outline="#000", width=1, tags=("one", "two"))  
    self.create_line(40, 20, 70, 20)
    # print([method_name for method_name in dir(self.test)
    #               if callable(getattr(self.test, method_name))]);
    # print(self.canvas.gettags(self.test))

  def drawData(self, data):
    for x in range(data.numCircles):
        self.drawCircle()
    self.canvas.create_line(data.points[0][0],
                            data.points[0][1],
                            data.points[1][0],
                            data.points[1][1])
    self.canvas.pack(fill=BOTH, expand=1)       