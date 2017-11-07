#!/usr/bin/python3
"""
File to practice querying mongodb using pymongo
"""
# Import
import pprint
from pymongo import MongoClient

# Make a MongoClient on default host(localhost) and port(27017)
client = MongoClient()

# Get a database
il_db = client.improv_live

# Get a collection
prompt_col = il_db.prompts

# Specify a thing to add
thing1 = {"name":"Rug", "type":"thing", "tags":["prompt", "thing"]}

# Insert thing1
#thing1_id = prompt_col.insert_one(thing1).inserted_id

# Get Single Document and print
#pprint.pprint(prompt_col.find_one())

# Get multiple Documents and print
for doc in prompt_col.find({"tags":"thing"}):
    pprint.pprint(doc)
