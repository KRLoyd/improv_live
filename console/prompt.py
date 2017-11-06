#!/usr/bin/python3
"""
Module for Game Class
"""

from datetime import datetime
import models
from models.base_model import BaseModel
from uuid import uuid4


class Prompt(BaseModel):
    """
    Prompt Class

    public attributes:
    name
    p_type (1 of 4: relationship, occupation, thing, location)
    """

    name = ""
    ptype = ""

    def __init__(self, *args, **kwargs):
        """
        __init__ method for Prompt class
        """
        if kwargs:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
