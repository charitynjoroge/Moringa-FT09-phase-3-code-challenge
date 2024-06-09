import sqlite3

class Author:
    def __init__(self, name):
        self.conn = sqlite3.connect('magazines.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS authors
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)''')
        self.conn.commit()
        self._id = None
        self._name = name
        self.cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        self.conn.commit()
        self._id = self.cursor.lastrowid

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):  
            raise AttributeError("Cannot change author's name after instantiation")
        setattr(self, '_name', value)
        self.cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (value, self._id))
        self.conn.commit()

    def __repr__(self):
        return f'<Author {self.name}>'
    

    def articles(self):
        self.cursor.execute('''SELECT a.title 
                              FROM authors 
                              JOIN articles a ON authors.id = a.author_id 
                              WHERE authors.id =?''', (self.id,))
        results = self.cursor.fetchall()
        return [row[0] for row in results]

    def magazines(self):
        self.cursor.execute('''SELECT m.name 
                              FROM authors 
                              JOIN articles a ON authors.id = a.author_id 
                              JOIN magazines m ON a.magazine_id = m.id 
                              WHERE authors.id =?''', (self.id,))
        results = self.cursor.fetchall()
        return [row[0] for row in results]
    
