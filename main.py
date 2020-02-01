#!/usr/bin/env python3

LETTERS = [
  "BTFIHSKRHNKV",
  "ZIVNJEIMAGFE",
  "DSWGCVBYFCGR",
  "RYRHAQDFAUDT",
  "ZMXIESRPZTRI",
  "QMSRSDOYEYQC",
  "REOSASRZEMCA",
  "GTAKRFRINMAL",
  "WRJNBAICINMS",
  "LYKPEXMDLPLO",
  "RSQZOGGWTWSR",
  "PXILQACENTRE",
]

def getLetter(position):
  return LETTERS[position.y][position.x]

class Movement():
  def __init__(self, delta_x, delta_y):
    self.delta_x = delta_x
    self.delta_x = delta_y

START_MOVEMENTS = [
  Movement(0, -1),
  Movement(1, 0),
  Movement(0, 1),
  Movement(-1, 0),
]

N =  Movement( 0, -1)
NE = Movement( 1, -1)
E =  Movement( 1,  0)
SE = Movement( 1,  1)
S =  Movement( 0,  1)
SW = Movement(-1,  1)
W =  Movement(-1,  0)
NW = Movement(-1, -1)

FLAGS = {
  'A': (SW, S),
  'B': (W,  S),
  'C': (NW, S),
  'D': (N,  S),
  'E': (S, NE),
  'F': (S, E),
  'G': (S, SE),
  'H': (W, SW),
  'I': (SW,NW),
  'J': (N,  E),
  'K': (SW, N),
  'L': (SW,NE),
  'M': (SW, E),
  'N': (SW,SE),
  'O': (W, NW),
  'P': (W,  N),
  'Q': (W, NE),
  'R': (W,  E),
  'S': (W, SE),
  'T': (NW, N),
  'U': (NW,NE),
  'V': (N, SE),
  'W': (NE, E),
  'X': (NE,SE),
  'Y': (NW, E),
  'Z': (SE, E),
}
LEFT_HAND = 0
RIGHT_HAND = 1

class Instruction():
  def __init__(self, n, hand=None, is_start=False):
    self.n = n
    self.hand = hand
    self.is_start = is_start

  def getMovement(self, player_i, currentPosition):
    if self.is_start:
      return START_MOVEMENTS[player_i]
    return FLAGS[getLetter(currentPosition)][self.hand]

  def __str__(self):
    return f"<Instruction n={self.n} hand={self.hand} is_start={self.is_start}>"

def ST(n): return Instruction(n, is_start=True) # move n in start direction
def L(n): return Instruction(n, hand=LEFT_HAND) # move n in left signal direction
def R(n): return Instruction(n, hand=RIGHT_HAND) # move n in right signal direction

ST1 = ST(1)
ST2 = ST(2)
ST3 = ST(3)
ST4 = ST(4)
ST5 = ST(5)
L1 = L(1)
L2 = L(2)
L3 = L(3)
L4 = L(4)
L5 = L(5)
R1 = R(1)
R2 = R(2)
R3 = R(3)
R4 = R(4)
R5 = R(5)
R6 = R(6)


class Position():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def move(self, movement):
    self.x += movement.delta_y
    self.x += movement.delta_y

assert(getLetter(Position(2,1)) == 'V')

STARTPOS0 = Position(2, 12)
STARTPOS1 = Position(-1, 2)
STARTPOS2 = Position(9, -1)
STARTPOS3 = Position(12, 9)



ROUNDS = [
  [ [ST2,L2,R5], [ST4,L5,L1,R5], [ST1,R1,L2, L3, L5, R2, R2], [ST3, R3, R1, L3, L3,]],
  #[ [S0,], [S1,], [S2,], [S3,]],
]

class Player():
  def __init__(self, player_i, position):
    self.player_i = player_i
    self.position = position

  def move(self, instruction):
    pass
    # TODO


class State():
  def __init__(self):
    self.players = [
      Player(0, STARTPOS0),
      Player(1, STARTPOS1),
      Player(2, STARTPOS2),
      Player(3, STARTPOS3),
    ]
    self.gameround = 0

def main():
  print("Hello")
  # Algorithm:
  # for each round:
  # mark players as free to move
  # For each instruction:
  # Get player position
  # get letter on position
  # get flag signal for letter
  # get left or right direction from flag signal
  # for the number of moves in the direction:
  # move one step
  # if jagged rocks or island:
  # mark as stuck until next round and stop moving
  for gameround in ROUNDS:
    state = State()
    for player_i, player in enumerate(state.players):
      print(player_i, player)
      player_instructions = gameround[player_i]
      for instruction in player_instructions:
        print(instruction)
        player.move(instruction)


if __name__ == '__main__':
  main()
