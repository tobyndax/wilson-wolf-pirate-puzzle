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

class Instruction():
  def __init__(self):
    pass

def ST(n): return f"ST{n}" # move n in start direction
def L(n): return f"L{n}" # move n in left signal direction
def R(n): return f"R{n}" # move n in right signal direction

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

STARTPOS0 = Position(2, 12)
STARTPOS1 = Position(-1, 2)
STARTPOS2 = Position(9, -1)
STARTPOS3 = Position(12, 9)



ROUNDS = [
  [ [ST2,L2,R5], [ST4,L5,L1,R5], [ST1,R1,L2, L3, L5, R2, R2], [ST3, R3, R1, L3, L3,]],
  #[ [S0,], [S1,], [S2,], [S3,]],
]

class Player():
  def __init__(self, position):
    self.position = position

class State():
  def __init__(self):
    self.players = [
      Player(STARTPOS0),
      Player(STARTPOS1),
      Player(STARTPOS2),
      Player(STARTPOS3),
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
        #player.position.move()


if __name__ == '__main__':
  main()
