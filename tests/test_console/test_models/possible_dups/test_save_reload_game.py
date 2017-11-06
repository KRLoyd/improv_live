#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.game import Game

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_game = Game()
my_game.name = "Betty"
my_game.number_players = 2
my_game.description = "The best game!"
my_game.save()
print(my_game)
