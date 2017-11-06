#!/usr/bin/python3
"""
Module for Game Class
"""

from datetime import datetime
import models
from models.base_model import BaseModel
from uuid import uuid4


class Game(BaseModel):
    """
    Game Class

    public attributes:
    name
    number_players
    description
    """

    name = ""
    number_players = 0
    description = ""

    def __init__(self, *args, **kwargs):
        """
        __init__ method for Game class
        """
        if kwargs:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
