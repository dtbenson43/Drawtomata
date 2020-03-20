from state import State

class Automata:
  def __init__(self, dataString=None, canvas=None):
    self.numStates = 0
    self.alphabet = []
    self.transitions = []
    self.transitionDict = {}
    self.startState = 0
    self.acceptStates = []
    self.states = []
    self.canvas = canvas
    
    if (dataString != None):
      self.parseDataString(dataString)

  def createState(self, num):
    return State(num, canvas=self.canvas)
  
  def parseDataString(self, dataString):
    tokens = dataString.split(";")
    self.numStates = int(tokens[0])
    self.alphabet = tokens[1].split(",")
    for i in range(len(self.alphabet)):
      self.alphabet[i] = self.alphabet[i].strip()

    self.transitions = tokens[2].split(",")
    self.startState = int(tokens[3])
    self.acceptStates = tokens[4].split(",")
    for i in range(len(self.acceptStates)):
      self.acceptStates[i] = int(self.acceptStates[i])

    for i in range(self.numStates):
      state = self.createState(i)
      if (state.id in self.acceptStates):
        state.setAccecptState(True)
      self.states.append(state)
    
    for i in range(len(self.transitions)):
      transition = self.transitions[i].replace("(", "").replace(")", "").split(":")
      self.transitions[i] = transition

      if transition[0] not in self.transitionDict:
        self.transitionDict[transition[0]] = {}

      if transition[1] not in self.transitionDict[transition[0]]:
        self.transitionDict[transition[0]][transition[1]] = []

      self.transitionDict[transition[0]][transition[1]].append(transition[2])

      state = self.states[int(transition[0])]
      state.addTransition(transition[2], int(transition[1]))



  def transition(self, currentState, symbol):
    if (currentState < self.numStates):
      self.states[currentState].transition(symbol)


  def print(self):
    strToPrint = "Number of states: {}\nAlphabet: {}\nTransitions: {}\nStart State: {}\nAccept States: {}"
    print(strToPrint.format(self.numStates, self.alphabet, self.transitionDict, self.startState, self.acceptStates))
    print("States:")

    for state in self.states:
      print("State: {}\tTran: {}\t Acpt: {}".format(state.id, state.transitions, state.acceptState))