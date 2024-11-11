import unittest
from package_folder.package.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def setUp(self):
        # Initialize with required arguments: name, email, fav_genre
        self.bl = BookLover("Jordan", "jordan@example.com", "scifi")

    def test_add_new_book_successfully(self):
        self.bl.add_book("Dune", 5)
        self.assertIn("Dune", self.bl.book_list['book_name'].values,
                      "New book should appear in the collection.")

    def test_prevent_duplicate_books(self):
        self.bl.add_book("Neuromancer", 4)
        result = self.bl.add_book("Neuromancer", 5)
        self.assertEqual(result, "Book already exists.",
                         "Duplicate entries should not be allowed.")

    def test_check_book_exists_true(self):
        self.bl.add_book("Snow Crash", 3)
        self.assertTrue(self.bl.has_read("Snow Crash"),
                        "has_read should return True if book exists.")

    def test_check_book_exists_false(self):
        self.assertFalse(self.bl.has_read("Hyperion"),
                         "has_read should return False if book doesn’t exist.")

    def test_count_books_read(self):
        self.bl.add_book("The Left Hand of Darkness", 5)
        self.bl.add_book("Foundation", 4)
        self.assertEqual(self.bl.num_books_read(), 2,
                         "num_books_read should return the count of unique books added.")

    def test_favorite_books_only_high_ratings(self):
        self.bl.add_book("Do Androids Dream of Electric Sheep?", 2)
        self.bl.add_book("The Expanse", 4)
        self.bl.add_book("Ender’s Game", 5)
        fav_books = self.bl.fav_books()
        self.assertEqual(len(fav_books), 2,
                         "Only books with ratings above 3 should be favorites.")
        self.assertIn("The Expanse", fav_books['book_name'].values)
        self.assertIn("Ender’s Game", fav_books['book_name'].values)


if __name__ == '__main__':
    unittest.main()
