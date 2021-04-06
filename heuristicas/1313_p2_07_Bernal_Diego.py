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
    return randrange(10) + state.game.min_score


# class Solution2(StudentHeuristic):
#   def get_name(self) -> str:
#     return "Marcia Ana"

#   def evaluation_function(self, state: TwoPlayerGameState) -> float:
#     cont = 0
#     while (state.parent != None):
#       cont += 1
#       state = state.parent.clone()
#     return cont/2

# class Solution3(StudentHeuristic):
#   def get_name(self) -> str:
#     return "Zampa Teste"

#   def evaluation_function(self, state: TwoPlayerGameState) -> float:
#     return max(Solution1.evaluation_function(self, state), Solution2().evaluation_function(state))