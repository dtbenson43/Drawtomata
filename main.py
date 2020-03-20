from tkinter import Tk, Frame, BOTH
from automataCanvas import AutomataCanvas
from automata import Automata

FILEPATH = "automataData" ## automata data file
WIDTH = 506               ## window width
HEIGHT = 506              ## window height
FRAME_WIDTH = 500
FRAME_HEIGHT = 500
PAD = 3

def main():
  
  # get data from file
  with open(FILEPATH) as f:
    data = f.readline()

  # pass data Automata
  aut = Automata(data)
  aut.print()

  # set up Tk root and frame
  root = Tk()
  root.geometry(str(WIDTH)+"x"+str(HEIGHT)+"+10+10")
  frame = Frame(width=FRAME_WIDTH, height=FRAME_HEIGHT, padx=PAD, pady=PAD)
  frame.pack(fill=BOTH, expand=1)
  
  # create automata canvas with Automata and Frame
  AutomataCanvas(frame=frame, automata=aut, width=FRAME_WIDTH, height=FRAME_HEIGHT)

  # start Tk
  root.mainloop()


if __name__ == '__main__':
  main()