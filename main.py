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
  print(position)
  return LETTERS[position.y][position.x]

LAND_MAP = [
  ".......x....",
  "...x........",
  "............",
  ".........x..",
  ".##.........",
  ".##.........",
  ".##....##...",
  ".......##...",
  ".......##.x.",
  "x...........",
  ".....x......",
  "............",
]

def isLand(position):
  return LAND_MAP[position.y][position.x] != '.'

import collections
Movement = collections.namedtuple('Movement', 'delta_x delta_y')

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
ST6 = ST(6)
ST7 = ST(7)
ST8 = ST(8)
ST9 = ST(9)
L1 = L(1)
L2 = L(2)
L3 = L(3)
L4 = L(4)
L5 = L(5)
L9 = L(9)
R1 = R(1)
R2 = R(2)
R3 = R(3)
R4 = R(4)
R5 = R(5)
R6 = R(6)
R7 = R(7)


class Position():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def move(self, movement):
    self.x += movement.delta_x
    self.y += movement.delta_y

  def __str__(self):
    return f"<Position x={self.x} y={self.y}>"

assert(getLetter(Position(2,1)) == 'V')
assert(not isLand(Position(2,1)))
assert(isLand(Position(3,1)))
assert(Instruction(1,LEFT_HAND).getMovement(1, Position(1,2)) == Movement(-1,0))


STARTPOS0 = Position(2, 12)
STARTPOS1 = Position(-1, 2)
STARTPOS2 = Position(9, -1)
STARTPOS3 = Position(12, 9)


ROUNDS = [
  #1
  [ [ST2,L2,R5], [ST4,L5,L1,R5], [ST1,R1,L2, L3, L5, R2, R2], [ST3, R3, R1, L3, L3,]],
  #2
  [ [ST5,L2], [ST6,L2,L5,R5,R1,], [ST4,], [ST9,R4,L1,]],
  #3
  [ [ST2,R1,R2,L2,R3,R2,R1], [ST6,R1,R3,R1], [ST1,L1,R5], [ST1,R1,]],
  #4
  [ [ST2,R3,R2], [ST9,L4,], [ST2,R2,R2,L3,L3], [ST5,L1]],
  #5
  [ [ST4,R3,R1,R2,R1,R2], [ST5,R5,R3,], [ST1,L1,R5,], [ST3,R3,L1,]],
  #6
  [ [ST2,R1,R4,L1], [ST1,R3,R1,], [ST1,L3,L1,L2,L1,], [ST8,L2,R1,]],
  #7
  [ [ST2,R3,R2], [ST1,R6,R7], [ST1,L1,R5], [ST2,R1,L1]],
  #8
  [ [ST2,R1,R3,R3,R3,R3,L1], [ST1,R6,R7], [ST1,L3,R4,R1], [ST3,R5,L1,R3]],
  #9
  [ [ST4,R5], [ST6,R1,R4,R1], [ST1,L4,R2], [ST3,R3,L1]],
  #10
  [ [ST2,R3,R2], [ST3,L1], [ST1,L1,R5], [ST6,L1]],
  #11
  [ [ST2,R3,L2,L2], [ST2,R1,R3,R1,L3,R4], [ST1,L1,R3,R3,L1,L2,L1], [ST3,L3,L1]],
  #12
  [ [ST2,R3,R2], [ST2,R1,R5,L1,L2,R2], [ST4], [ST3,R3,L1]],
  #13
  [ [ST4,R5], [ST5,R2,R3,R4,L3,L3], [ST1,L1,R5], [ST8,R2,R1]],
  #14
  [ [ST2,R5,R1,L1], [ST7,R5,R1], [ST1,L9], [ST5,L1]],
  #15
  [ [ST5,L1,L1,L1,R1], [ST1,R3,R1], [ST1,L5,L2], [ST6,R5,R1]],
  #16
  [ [ST6], [ST5,L1], [ST1,R2,L4,L2,L5,R5,R1], [ST8,L1,R3,R1]],
  #17
  [ [ST2,R1,R3,R4,R1,L1,L1], [ST7,R5,R1], [ST1,L1,R5], [ST3,R3,L1]],
  #18
  [ [ST2,R3,R2], [ST2,R1,R4,L1,L2,L1], [ST1,R1,L2,L3,L3,L3], [ST3,R3,L1]],
  #
]

class Player():
  def __init__(self, player_i, position):
    self.player_i = player_i
    self.position = position

  def move(self, movement):
    print(f"Move player {self}: {movement}")
    self.position.move(movement)
    print(f"            {self}: {movement}")

  def isStuck(self):
    return isLand(self.position)

  def __str__(self):
    return f"<Player {self.player_i} position={self.position}>"

class State():
  def __init__(self):
    self.players = [
      Player(0, STARTPOS0),
      Player(1, STARTPOS1),
      Player(2, STARTPOS2),
      Player(3, STARTPOS3),
    ]
    self.gameround = 0

  def __str__(self):
    gamemap = [['.' for c in range(12)] for r in range(12)]
    for player_i, player in enumerate(self.players):
      gamemap[player.position.y][player.position.x] = str(player_i)
    s = ""
    for row in gamemap:
      for cell in row:
        s += cell
      s += "\n"
    return s

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
        movement = instruction.getMovement(player_i, player.position)
        for _ in range(instruction.n):
          player.move(movement)
          if player.isStuck():
            break
        if player.isStuck():
          break
    print(state)


if __name__ == '__main__':
  main()
