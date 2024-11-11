from package.booklover import BookLover

# Create a BookLover object
my_book_lover = BookLover("Shelly", "shelly@blah.com", "fiction")

# Add a book
my_book_lover.add_book("The Great Gatsby", 5)

# Print the number of books read
print("Number of books read:", my_book_lover.num_books_read())