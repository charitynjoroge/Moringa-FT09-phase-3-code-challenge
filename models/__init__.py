class Magazine:
    def __init__(self, cursor, id, name, category):
        self.cursor = cursor
        self._id = id
        self._name = name
        self._category = category

class Author:
    def __init__(self, cursor, name):
        self.cursor = cursor
        self._name = name

class Article:
    def __init__(self, cursor, id, title, content, author_id, magazine_id):
        self.cursor = cursor
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id



#I was unable to keep track of my magazine.db so i created a magazines.db 
#my magazines.db stores the magazines and the authors 
#I was unable to display the articles in the article table