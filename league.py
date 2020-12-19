import random
import string
import sqlite3
from sqlite3 import Error

class User:
    _name = ""

    def __init__(self, name):
        self.name = name

    def name(self):
        return self._name



class Team:
    sport = ""
    _score = 0
    team = [] # team list of players (containing string names only)
    identifier = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))

    def __init__(self, score, sport, next=None):
        self._score = score
        self.sport = sport
        if next != None:
            self.next = next

    def score(self):
        return self._score


class League:
    length = 0
    teams = []

    def __init__(self, len):
        self.length = len

    def add_team(self, t: Team):
        if len(self.teams) == 0:
            self.teams.append(t)
        else:
            i = len(self.teams))
            while t.score() < self.teams[i]:
                i += 1
            self.teams.insert(i, t)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, task):

    sql = ''' INSERT INTO tasks(League,Sport,Teams,identifier,scores)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def main():
    """ TEMPORARY TEST """
    l = League(8) # Test
    database = r"C:/sqlite/db/pythonsqlite.db" # temporary path for now
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('Soccer League');
        project_id = create_project(conn, project)



if __name__ == "__main__":
    main()
