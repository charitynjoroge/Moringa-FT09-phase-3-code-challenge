import unittest
from models.article import Article
from models.author import Author
from models.magazine import Magazine
from database.connection import get_db_connection

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.article = Article(1, "Test Article", "This is a test article", 1, 1)

    def test_init(self):
        self.assertEqual(self.article.id, 1)
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.content, "This is a test article")
        self.assertEqual(self.article.author_id, 1)
        self.assertEqual(self.article.magazine_id, 1)

    def test_title_property(self):
        with self.assertRaises(ValueError):
            self.article.title = 123
        with self.assertRaises(ValueError):
            self.article.title = "a" * 51
        self.article.title = "New Title"
        self.assertEqual(self.article.title, "New Title")

    def test_get_author(self):
        # create some sample data
        author = Author(1, "Test Author")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (id, name) VALUES (?, ?)", (author.id, author.name))
        cursor.execute("INSERT INTO articles (id, title, content, author_id, magazine_id) VALUES (?, ?, ?, ?, ?)", (self.article.id, self.article.title, self.article.content, self.article.author_id, self.article.magazine_id))
        conn.commit()
        self.assertEqual(self.article.get_author().name, "Test Author")

    def test_get_magazine(self):
        # create some sample data
        magazine = Magazine(1, "Test Magazine", "Test Category")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)", (magazine.id, magazine.name, magazine.category))
        cursor.execute("INSERT INTO articles (id, title, content, author_id, magazine_id) VALUES (?, ?, ?, ?, ?)", (self.article.id, self.article.title, self.article.content, self.article.author_id, self.article.magazine_id))
        conn.commit()
        self.assertEqual(self.article.get_magazine().name, "Test Magazine")

if __name__ == '__main__':
    unittest.main()