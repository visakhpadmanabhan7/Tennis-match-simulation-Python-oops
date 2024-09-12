from player import Player
from tennis_game import TennisGame

player1=Player("player1")
player2=Player("player2")
#
# tennis_game1=TennisGame(player1,player2,input_test=[player2,player2,player2,player2,player1,player2])
# tennis_game1.start_match()
#
# tennis_game1=TennisGame(player1,player2,input_test=[player2,player2,player1,player1,player1,player1])
# tennis_game1.start_match()
#
tennis_game1=TennisGame(player1,player2,input_test=[player2,player2,player2,player1,player1,player1,player1,player2,player1,player1])
tennis_game1.start_match()
# #
# tennis_game1=TennisGame(player1,player2,input_test=[player2,player2,player2,player1,player1,player1,player2,player2])
# tennis_game1.start_match()