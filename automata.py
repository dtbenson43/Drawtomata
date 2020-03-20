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
  
  def parseNumStates(self, tokens):
    try:
      numStates = int(tokens[0])
    except:
      raise ValueError('Number of states is not a valid integer')
    return numStates

  def parseAlphabet(self, tokens):
    try:
      alphabet = tokens[1].split(",")
    except:
      raise ValueError('Alphabet not provided')

    if len(alphabet) == 0:
      raise ValueError('Alphabet not provided')

    for i in range(len(alphabet)):
      alphabet[i] = alphabet[i].strip()
    return alphabet

  def parseTransitions(self, tokens):
    try:
      transitions = tokens[2].split(",")
    except:
      raise ValueError('Transitions not provided')
    if len(transitions) == 0:
      raise ValueError('Transitions not provided')

    for i in range(len(transitions)):
      transition = transitions[i].replace("(", "").replace(")", "").split(":")
      if len(transition) != 3:
        raise ValueError('Transition \'{}\' is malformed'.format(transitions[i]))
      transitions[i] = transition
    return transitions

  def parseStartState(self, tokens):
    try:
      startState = int(tokens[3])
    except:
      raise ValueError('Start state is not a valid integer')
    return startState

  def parseAcceptStates(self, tokens):
    try:
      acceptStates = tokens[4].split(",")
    except:
      raise ValueError('Accept states not provided')
    if len(acceptStates) == 0:
      raise ValueError('Accept states not provided')

    for i in range(len(self.acceptStates)):
      try:
        acceptStates[i] = int(acceptStates[i])
      except:
        raise ValueError('Accept state \'{}\' is not a valid integer'.format(acceptStates[i]))
    return acceptStates

  def parseDataString(self, dataString):
    tokens = dataString.split(";")
    self.numStates = self.parseNumStates(tokens)
    self.alphabet = self.parseAlphabet(tokens)
    self.transitions = self.parseTransitions(tokens)
    self.startState = self.parseStartState(tokens)
    self.acceptStates = self.parseAcceptStates(tokens)
    print(self.transitions)

    for i in range(self.numStates):
      state = self.createState(i)
      if (state.id in self.acceptStates):
        state.setAccecptState(True)
      self.states.append(state)
    
    for i in range(len(self.transitions)):

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