class Transition:
  def __init__(self, num, transitions=None, canvas=None):
    self.id = num 
    self.transitions = transitions if transitions != None else {}
    self.acceptState = False

  def addTransition(self, symbol, nextState):
    self.transitions[symbol] = nextState

  def transition(self, symbol):
    if (symbol in self.transitions):
      return self.transitions[symbol]

  def setAccecptState(self, acceptState):
    self.acceptState = acceptState