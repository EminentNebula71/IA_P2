import time
from random import randrange
from game import (
    TwoPlayerGameState,
)
from tournament import (
    StudentHeuristic,
)
from strategy import MinimaxStrategy


class Solution1(StudentHeuristic):
  def get_name(self) -> str:
    return "Elsa Polindo"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    return randrange(10)


class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "Marcia Ana"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    return min(randrange(5) + state.game.min_score, randrange(10))

class Solution3(StudentHeuristic):
  def get_name(self) -> str:
    return "Zampa Teste"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    max = state.game.max_score
    min = state.game.min_score
    if(max + min != 0):
      return (100*((max - min)/(max - min)))
    else:
      return 0