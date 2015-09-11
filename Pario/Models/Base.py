#   Base.py
#   Description:    ...

from Pario import app
from pymongo import MongoClient
import json


class Base():

    def __init__(self):
        client = MongoClient(
            app.config['DATABASE_HOST'],
            app.config['DATABASE_PORT']
            )
        self.db = client[app.config['DATABASE_NAME']]

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.db = None
            return False
        self.db.disconnect()
        self.db = None
        return True
