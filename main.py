from player import Player
from tennis_game import TennisGame

if __name__ == "__main__":
    # Create two player objects
    player1 = Player("player1")
    player2 = Player("player2")

    # First tennis game simulation
    tennis_game1 = TennisGame(player1, player2, input_test=[
        player2, player2, player2, player2, player1, player2
    ])
    tennis_game1.start_match()

    # Second tennis game simulation
    tennis_game2 = TennisGame(player1, player2, input_test=[
        player2, player2, player1, player1, player1, player1
    ])
    tennis_game2.start_match()

    # Third tennis game simulation
    tennis_game3 = TennisGame(player1, player2, input_test=[
        player2, player2, player2, player1, player1, player1, player1, player2, player1, player1
    ])
    tennis_game3.start_match()