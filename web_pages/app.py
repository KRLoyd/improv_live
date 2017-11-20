#!/usr/bin/python3
"""
Script to start a Flask web application and route for the following requests

- GET: /, /index, /game, /wheel, /wheelGame, /wheelPrompt
"""

# Imports
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo

# Create instance of Flask
app = Flask(__name__)
# Set strict_slashes for all routes
app.url_map.strict_slashes = False
# Congfigure Mongodb variables for app
app.config['MONGO_DBNAME'] = 'improv_live'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/improv_live'

# Create instance of PyMongo
mongo = PyMongo(app)

# Get collections
with app.app_context():
    col_prompt = mongo.db.prompts
    col_game = mongo.db.games

# Set up CORS
cors = CORS(app, resources={r"/*": {"origins":"*"}})


@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    """
    Method to render the index page
    """
    return render_template("index.html")

@app.route('/game', methods=['GET'])
def game(game_list=None):
    """
    Method to route game GET HTTP requests
    """
    return render_template("game.html")

@app.route('/gameList', methods=['POST'])
def game_list():
    """
    Method to route gameList POST HTTP requests
    """
    request_json = request.get_json()
    players = []
    for item in request_json.get('players'):
        players.append(item)
    items = []
    for player in players:
        items.extend(list(col_game.find({"num_player":player})))
    all_games = {}
    i = 0
    for game in items:
        game_dict = {}
        game_dict['name'] = game['name']
        game_dict['description'] = game['description']

        separator = ''
        playerStr = ''
        for player_count in game['num_player']:
            playerStr += separator
            playerStr += str(player_count)
            separator = ", "
        game_dict['num_player'] = playerStr

        if game_dict not in all_games.values():
            all_games[i] = game_dict
        i += 1
    return jsonify(all_games)


@app.route('/wheel', methods=['GET'])
def wheel():
    """
    Method to route wheel GET HTTP requests
    """

    return render_template("wheel.html")

@app.route('/wheelGame', methods=['POST'])
def wheel_game():
    """
    Method to route wheelGame POST HTTP requests
    """
    request_json = request.get_json()
    prompt = request_json['num_player'][0]
    wheel_dict = {}
    items = list(col_game.find({"num_player":prompt}))
    i = 0
    for item in items:
        wheel_dict[i] = item['name']
        i += 1
    return jsonify(wheel_dict)


@app.route('/wheelPrompt', methods=['POST'])
def wheel_prompt():
    """
    Method to route wheelPrompt POST HTTP requests
    """
    request_json = request.get_json()
    prompt = request_json['prompt'][0]
    prompt_dict = {'Things':'thing', 'Locations':'location', 'Occupations':'occupation', 'Relationships':'relationship'}
    wheel_dict = {}
    items = list(col_prompt.find({"tags":prompt_dict.get(prompt)}))
    i = 0
    for item in items:
        wheel_dict[i] = item['name']
        i += 1
    return jsonify(wheel_dict)



if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
