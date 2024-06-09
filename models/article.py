import sqlite3

class Article:
    def __init__(self,cursor, author, magazine, title, content):
        self.conn = sqlite3.connect('magazines.db')
        self.cursor = self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS articles
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL, author_id INTEGER, magazine_id INTEGER, 
                             FOREIGN KEY (author_id) REFERENCES authors (id), FOREIGN KEY (magazine_id) REFERENCES magazines (id))''')
        self.conn.commit()
        self._id = None
        self._title = None
        self._content = None
        self._author_id = None
        self._magazine_id = None
        if not hasattr(author, 'id') or not hasattr(magazine, 'id'):
            raise ValueError("Author and Magazine must be instantiated with IDs")
        self.title = title
        self.content = content
        self.author_id = author.id
        self.magazine_id = magazine.id
        self.cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?,?,?,?)", (title, content, author.id, magazine.id))
        self.conn.commit()
        self._id = self.cursor.lastrowid

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        raise AttributeError("ID cannot be changed after instantiation")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError("Content must be a string")
        self._content = value

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self):
        raise AttributeError("Author ID cannot be changed after instantiation")

    @property
    def magazine_id(self):
        return self._magazine_id

    @magazine_id.setter
    def magazine_id(self):
        raise AttributeError("Magazine ID cannot be changed after instantiation")

    def __repr__(self):
        return f'<Article {self.title}>'
    
    def get_author(self):
        self.cursor.execute('''SELECT a.name 
                              FROM articles 
                              JOIN authors a ON articles.author_id = a.id 
                              WHERE articles.id = ?''', (self.id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def get_magazine(self):
        self.cursor.execute('''SELECT m.name 
                              FROM articles 
                              JOIN magazines m ON articles.magazine_id = m.id 
                              WHERE articles.id = ?''', (self.id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None