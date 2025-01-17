import sqlite3
import cred
from flask import g


class OSEDatabase:
    def __init__(self):
        self.connection = ""
        self.cursor = ""

    def __enter__(self):
        return self.connection, self.cursor

    def __exit__(self, type, value, tb):
        pass

    def initDB(self):
        self.connection = getattr(g, '_database', None)
        if self.connection is None:
            self.connection = g._database = sqlite3.connect(cred.DATABASE_LOC, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def stop(self, exception):
        self.connection = getattr(g, '_database', None)
        if self.connection is not None:
            self.connection.close()
