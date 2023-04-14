import sqlite3


connect = sqlite3.connect('bot.db')
cursor = connect.cursor()

def create():
    global cursor
    create_db = cursor.execute("""CREATE TABLE IF NOT EXISTS character(id PRIMARY KEY, name VARCHAR(100) NOT NULL, protect INT NOT NULL, attack INT NOT NULL, speed INT NOT NULL);""")
    create_db.commit()


def save_charachter(name, protect, attack, speed):
    cursor.execute("""INSERT INTO character(*) VALUES(%s, $s, %s, $s);""", (name, protect, attack, speed))
    cursor.lastrowid()
    cursor.commit()

def get_charachter(id):
    charachter = cursor.execute("""SELECT * FROM character;""").fetchall()
    return '/n'.join(f'id: {id}\n'
                     f'name {name}'
                     f'attack {attack}'
                     for id, name, attack in charachter)
