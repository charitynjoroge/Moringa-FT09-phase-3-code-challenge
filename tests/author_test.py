import unittest
from models.author import Author

class TestAuthor(unittest.TestCase):
    def setUp(self):
        self.author = Author("Test Author")

    def test_create_authors_table(self):
        self.author.create_authors_table()
        self.author.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='authors'")
        self.assertTrue(self.author.cursor.fetchone())

    def test_insert_author(self):
        self.author.insert_author("New Author")
        self.author.cursor.execute("SELECT * FROM authors WHERE name = ?", ("New Author",))
        self.assertTrue(self.author.cursor.fetchone())

    def test_id_property(self):
        self.author.insert_author("New Author")
        self.author.cursor.execute("SELECT id FROM authors WHERE name = ?", ("New Author",))
        self.assertEqual(self.author.id, self.author.cursor.fetchone()[0])

    def test_name_property(self):
        self.assertEqual(self.author.name, "Test Author")
        with self.assertRaises(AttributeError):
            self.author.name = "New Name"

    def test_articles(self):
        # create some sample data
        self.author.insert_author("Test Author")
        self.author.cursor.execute("INSERT INTO articles (title, author_id) VALUES (?, ?)", ("Test Article", self.author.id))
        self.author.conn.commit()
        self.assertEqual(self.author.articles(), ["Test Article"])

    def test_magazines(self):
        # create some sample data
        self.author.insert_author("Test Author")
        self.author.cursor.execute("INSERT INTO magazines (name) VALUES (?)", ("Test Magazine",))
        magazine_id = self.author.cursor.lastrowid
        self.author.cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Test Article", self.author.id, magazine_id))
        self.author.conn.commit()
        self.assertEqual(self.author.magazines(), ["Test Magazine"])

if __name__ == '__main__':
    unittest.main()