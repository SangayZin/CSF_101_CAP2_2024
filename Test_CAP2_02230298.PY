import unittest
from CSF_101_CAP2_02230298 import Library, User, Admin

class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        # Set up the library, admin, and user before each test.
        self.library = Library()
        self.user = User("TestUser")
        self.admin = Admin("Admin")

    # Test case 1: Valid book borrowing
    def test_valid_book_borrowing(self):
        """Test if a user can successfully borrow a book."""
        result = self.library.borrow_book("Book A", self.user.name)  # Call the borrow method
        print("test_valid_book_borrowing - Expected: 'Book 'Book A' borrowed by TestUser.', Got:", result)
        self.assertEqual(result, "Book 'Book A' borrowed by TestUser.")  # Check the return message
        self.assertFalse(self.library.books[0].is_available)  # Ensure book A is now borrowed

    # Test case 2: Invalid book borrowing (already borrowed)
    def test_invalid_book_borrowing(self):
        # Test trying to borrow a book that is already borrowed.
        self.library.borrow_book("Book A", self.user.name)
        result = self.library.borrow_book("Book A", self.user.name)  # Borrowing again
        print("test_invalid_book_borrowing - Expected: 'Book \'Book A\' is not available or already borrowed.', Got:", result)
        self.assertEqual(result, "Book 'Book A' is not available or already borrowed.")

     # Test case 3: Valid book returning
    def test_valid_book_returning(self):
        # Test if a user can return a borrowed book and check availability.
        self.library.borrow_book("Book A", self.user.name)
        result = self.library.return_book("Book A", self.user.name)
        print("test_valid_book_returning - Expected: 'Book \'Book A\' returned by TestUser.', Got:", result)
        self.assertEqual(result, "Book 'Book A' returned by TestUser.")
        self.assertTrue(self.library.books[0].is_available)  # Book A should be available again

    # Test case 4: Invalid book returning (not borrowed)
    def test_invalid_book_returning(self):
        # Test returning a book that hasn't been borrowed.
        result = self.library.return_book("Book A", self.user.name)  # Return without borrowing
        print("test_invalid_book_returning - Expected: 'Book \'Book A\' is not borrowed by TestUser.', Got:", result)
        self.assertEqual(result, "Book 'Book A' is not borrowed by TestUser.")

    # Test case 5: Admin adding books
    def test_admin_adding_books(self):
        # Test if the admin can add books and check if they appear in the library.
        result = self.admin.add_book(self.library, "Book D", "Author D")
        print("test_admin_adding_books - Expected: 'Book \'Book D\' by Author D added to the library.', Got:", result)
        self.assertIn("Book D", [book.title for book in self.library.books])  # Book D should be added

    # Test case 6: Boundary case - borrowing all books
    def test_borrowing_all_books(self):
        # Test if all books can be borrowed.
        self.library.borrow_book("Book A", self.user.name)
        self.library.borrow_book("Book B", self.user.name)
        self.library.borrow_book("Book C", self.user.name)
        self.assertFalse(self.library.books[0].is_available)  # Book A should be unavailable
        self.assertFalse(self.library.books[1].is_available)  # Book B should be unavailable
        self.assertFalse(self.library.books[2].is_available)  # Book C should be unavailable

    # Test case 7: Check available books after borrowing
    def test_check_available_books_after_borrowing(self):
        # Ensure that availability updates correctly after borrowing.
        self.library.borrow_book("Book A", self.user.name)
        available_books = [book.title for book in self.library.books if book.is_available]
        self.assertNotIn("Book A", available_books)  # Book A should not be in available books

    # Test case 8: Check available books after returning
    def test_check_available_books_after_returning(self):
        # Ensure that availability updates correctly after returning.
        self.library.borrow_book("Book A", self.user.name)
        self.library.return_book("Book A", self.user.name)
        available_books = [book.title for book in self.library.books if book.is_available]
        self.assertIn("Book A", available_books)  # Book A should be in available books again


if __name__ == '__main__':
    unittest.main()
