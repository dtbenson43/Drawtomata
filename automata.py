import sys
from state import State
from transition import Transition

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

  def getTransitions(self):
    return self.transitions

  def getStates(self):
    return self.states

  def setCanvas(self, canvas):
    self.canvas = canvas

  def error(self, str):
    print(str)
    sys.exit()

  def createTransition(self, origin, destination, symbols):
    return Transition(origin, destination, symbols, self.canvas)

  def createState(self, num):
    return State(num, self.canvas)
  
  def parseNumStates(self, tokens):
    try:
      numStates = int(tokens[0])
    except:
      self.error('Number of states is not a valid integer')
    return numStates

  def parseAlphabet(self, tokens):
    try:
      alphabet = tokens[1].split(",")
    except:
      self.error('Alphabet not provided')

    if len(alphabet) == 0:
      self.error('Alphabet not provided')

    for i in range(len(alphabet)):
      alphabet[i] = alphabet[i].strip()
    return alphabet

  def parseTransitions(self, tokens):
    numStates = self.parseNumStates(tokens)
    alphabet = self.parseAlphabet(tokens)
    transitionDict = {}
    try:
      transitions = tokens[2].split(",")
    except:
      self.error('Transitions not provided')
    if len(transitions) == 0:
      self.error('Transitions not provided')

    for i in range(len(transitions)):
      transition = transitions[i].replace("(", "").replace(")", "").split(":")
      if len(transition) != 3:
        self.error('Transition \'{}\' is malformed.'.format(transitions[i]))
      try:
        transition[0] = int(transition[0])
      except:
        self.error(
          'State \'{}\' in transition \'{}\' is not a valid integer'
          .format(transition[0], transitions[i])
        )
      try:
        transition[1] = int(transition[1])
      except:
        self.error(
          'State \'{}\' in transition \'{}\' is not a valid integer'
          .format(transition[1], transitions[i])
        )

      if transition[0] >= numStates or transition[0] < 0:
        self.error(
          'State \'{}\' in transition \'{}\' does not exist. Number of states is {}.'
          .format(str(transition[0]), transitions[i], numStates)
        )

      if transition[1] >= numStates or transition[1] < 0:
        self.error(
          'State \'{}\' in transition \'{}\' does not exist. Number of states is {}.'
          .format(str(transition[1]), transitions[i], numStates)
        )
        
      transition[2] = transition[2].strip()
      if transition[2] not in alphabet:
        self.error(
          'Symbol \'{}\' in transition \'{}\' not in alphabet. Alphabet is {}.'
          .format(transition[2], transitions[i], alphabet)
        )

      if transition[0] not in transitionDict:
        transitionDict[transition[0]] = {}

      if transition[1] not in transitionDict[transition[0]]:
        transitionDict[transition[0]][transition[1]] = []

      transitionDict[transition[0]][transition[1]].append(transition[2])
    return transitionDict

  def parseStartState(self, tokens):
    try:
      startState = int(tokens[3])
    except:
      self.error('Start state is not a valid integer')
    return startState

  def parseAcceptStates(self, tokens):
    try:
      acceptStates = tokens[4].split(",")
    except:
      self.error('Accept states not provided')
    if len(acceptStates) == 0:
      self.error('Accept states not provided')

    for i in range(len(acceptStates)):
      try:
        acceptStates[i] = int(acceptStates[i])
      except:
        self.error('Accept state \'{}\' is not a valid integer'.format(acceptStates[i]))
    return acceptStates

  def buildAutomata(self):
    for i in range(self.numStates):
      state = self.createState(i)
      if (state.id in self.acceptStates):
        state.setAccecptState(True)
      self.states.append(state)

    for origin in self.transitionDict:
      for destination in self.transitionDict[origin]:
        symbols = self.transitionDict[origin][destination]
        transition = self.createTransition(origin, destination, symbols)
        self.states[origin].addTransition(transition)
        self.transitions.append(transition)

  def parseDataString(self, dataString):
    tokens = dataString.split(";")
    self.numStates = self.parseNumStates(tokens)
    self.alphabet = self.parseAlphabet(tokens)
    self.transitionDict = self.parseTransitions(tokens)
    self.startState = self.parseStartState(tokens)
    self.acceptStates = self.parseAcceptStates(tokens)
    self.buildAutomata()

  def transition(self, currentState, symbol):
    if (currentState < self.numStates):
      self.states[currentState].transition(symbol)


  def print(self):
    strToPrint = "Number of states: {}\nAlphabet: {}\nTransitions: {}\nStart State: {}\nAccept States: {}"
    print(strToPrint.format(self.numStates, self.alphabet, self.transitionDict, self.startState, self.acceptStates))
    print("States:")

    for state in self.states:
      print("State: {}\tTran: {}\t Acpt: {}".format(state.id, state.transition, state.acceptState))