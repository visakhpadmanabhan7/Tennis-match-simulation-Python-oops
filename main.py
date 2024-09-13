from flask import Flask, jsonify
from player import Player
from tennis_game import TennisGame

app = Flask(__name__)

# Create two player objects globally so we can reuse them for all matches
player1 = Player("player1")
player2 = Player("player2")

# Function to simulate a tennis game match
def simulate_match(input_test):
    tennis_game = TennisGame(player1, player2, input_test=input_test)
    result = tennis_game.start_match()
    return result

# Route for Match 1
@app.route("/match1", methods=["GET"])
def match1():
    input_test = [player2, player2, player2, player2, player1, player2]
    result = simulate_match(input_test)
    return jsonify({"match": "Match 1", "result": result})

# Route for Match 2
@app.route("/match2", methods=["GET"])
def match2():
    input_test = [player2, player2, player1, player1, player1, player1]
    result = simulate_match(input_test)
    return jsonify({"match": "Match 2", "result": result})

# Route for Match 3
@app.route("/match3", methods=["GET"])
def match3():
    input_test = [player2, player2, player2, player1, player1, player1, player1, player2, player1, player1]
    result = simulate_match(input_test)
    return jsonify({"match": "Match 3", "result": result})

if __name__ == "__main__":
    app.run(debug=True)
