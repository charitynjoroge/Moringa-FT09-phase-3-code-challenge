import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine


class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        cursor = None
        magazine = Magazine(cursor, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Technology")

if __name__ == "__main__":
    unittest.main()
