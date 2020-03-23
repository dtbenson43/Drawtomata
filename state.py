class State:
  def __init__(self, num, transitions=None, canvas=None, diameter=40, acceptPad=4):
    self.id = num 
    self.transitions = transitions if transitions != None else []
    self.acceptState = False
    self.x = 0
    self.y = 0
    self.diameter = diameter
    self.center = (int(self.x + (self.diameter / 2)), int(self.y + (self.diameter / 2)))
    self.acceptPad = acceptPad
    self.canvas = canvas

  def addTransition(self, transition):
    self.transitions.append(transition)

  def transition(self, symbol):
    for transition in self.transitions:
      if transition.testSymbol(symbol):
        return transition.getNextState()

  def setAccecptState(self, acceptState):
    self.acceptState = acceptState

  def setDiameter(self, diameter):
    self.diameter = diameter

  def getDiameter(self):
    return self.diameter

  def setCanvas(self, canvas):
    self.canvas = canvas

  def setLocation(self, x, y):
    self.x = x
    self.y = y
    self.center = (self.x + (self.diameter / 2), self.y + (self.diameter / 2))

  def getCenter(self):
    return self.center

  def drawCircle(self):
    self.canvas.create_oval(
      self.x, 
      self.y, 
      self.x + self.diameter, 
      self.y + self.diameter,
      tags=("state_"+str(self.id),"state_circle"),
      fill="white"
    )

  def drawAcceptCircle(self):
    self.canvas.create_oval(
      self.x + self.acceptPad, 
      self.y + self.acceptPad, 
      self.x + self.diameter - self.acceptPad, 
      self.y + self.diameter - self.acceptPad,
      tags=("state_"+str(self.id),"state_accept_circle")
    )

  def drawLabel(self):
    self.canvas.create_text(
      self.x + (self.diameter / 2), 
      self.y + (self.diameter / 2), 
      text=str(self.id),
      tags=("state_"+str(self.id),"state_label")
    )
    
  def draw(self):
    self.drawCircle()
    self.drawLabel()
    if self.acceptState:
      self.drawAcceptCircle()
