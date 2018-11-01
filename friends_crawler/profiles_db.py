import sqlite3

class ProfilesDb:
    def __init__(self):
        self.sqlite = sqlite3.connect('profiles.db')

    def write(self, Person):
        pass
