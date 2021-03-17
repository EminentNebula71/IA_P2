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
    return randrange(5) + state.game.min_score

class Solution3(StudentHeuristic):
  def get_name(self) -> str:
    return "Zampa Teste"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    return randrange(7) + state.game.max_score
