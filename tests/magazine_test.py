import unittest
from models.magazine import Magazine
from models.__init__ import CONN,CURSOR
from models.author import Author

class TestMagazine(unittest.TestCase):
    def setUp(self):
        self.magazine = Magazine(CURSOR, CONN)

    def test_create_magazines_table(self):
        self.magazine.create_magazines_table()
        self.magazine.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='magazines'")
        self.assertTrue(self.magazine.cursor.fetchone())

    def test_id_property(self):
        with self.assertRaises(TypeError):
            self.magazine.id = "not an integer"
        self.magazine.id = 1
        self.assertEqual(self.magazine.id, 1)

    def test_name_property(self):
        with self.assertRaises(TypeError):
            self.magazine.name = 123
        with self.assertRaises(ValueError):
            self.magazine.name = "a"
        self.magazine.name = "Test Magazine"
        self.assertEqual(self.magazine.name, "Test Magazine")

    def test_category_property(self):
        with self.assertRaises(TypeError):
            self.magazine.category = 123
        with self.assertRaises(ValueError):
            self.magazine.category = ""
        self.magazine.category = "Test Category"
        self.assertEqual(self.magazine.category, "Test Category")

    def test_articles(self):
        # create some sample data
        self.magazine.name = "Test Magazine"
        self.magazine.category = "Test Category"
        self.magazine.cursor.execute("INSERT INTO articles (title, magazine_id) VALUES ('Article 1', ?)", (self.magazine.id,))
        self.magazine.cursor.execute("INSERT INTO articles (title, magazine_id) VALUES ('Article 2', ?)", (self.magazine.id,))
        self.magazine.conn.commit()
        self.assertEqual(self.magazine.articles(), ["Article 1", "Article 2"])

    def test_contributors(self):
        # create some sample data
        self.magazine.name = "Test Magazine"
        self.magazine.category = "Test Category"
        author = Author(CURSOR, CONN, name="Test Author")
        self.magazine.cursor.execute("INSERT INTO articles (title, magazine_id, author_id) VALUES ('Article 1', ?, ?)", (self.magazine.id, author.id))
        self.magazine.cursor.execute("INSERT INTO articles (title, magazine_id, author_id) VALUES ('Article 2', ?, ?)", (self.magazine.id, author.id))
        self.magazine.conn.commit()
        self.assertEqual(self.magazine.contributors(), ["Test Author"])

    def test_article_titles(self):
        # create some sample data
        self.magazine.name = "Test Magazine"
        self.magazine.category = "Test Category"
        self.magazine.cursor.execute("INSERT INTO articles (title, magazine_id) VALUES ('Article 1', ?)", (self.magazine.id,))
        self.magazine.cursor.execute("INSERT INTO articles (title, magazine_id) VALUES ('Article 2', ?)", (self.magazine.id,))
        self.magazine.conn.commit()
        self.assertEqual(self.magazine.article_titles(), ["Article 1", "Article 2"])

    def test_contributing_authors(self):
        # create some sample data
        self.magazine.name = "Test Magazine"
        self.magazine.category = "Test Category"
        author = Author(CURSOR, CONN, name="Test Author")
        self.magazine.cursor.execute("INSERT INTO articles (title, magazine_id, author_id) VALUES ('Article 1', ?, ?)", (self.magazine.id, author.id))
        self.magazine.cursor.execute("INSERT INTO articles (title, magazine_id, author_id) VALUES ('Article 2', ?, ?)", (self.magazine.id, author.id))
        self.magazine.cursor.execute("INSERT INTO articles (title, magazine_id, author_id) VALUES ('Article 3', ?, ?)", (self.magazine.id, author.id))
        self.magazine.conn.commit()
        self.assertEqual(len(self.magazine.contributing_authors()), 1)

if __name__ == '__main__':
    unittest.main()