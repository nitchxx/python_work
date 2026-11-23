
import re

book_title = input("Book title: ")
publication_year = input("Publication year: ")

try:
    if not re.fullmatch(r"[a-zA-Z\s]+", book_title):
        raise ValueError("Invalid book title. Use only alphabets and spaces.")

    if not re.fullmatch(r"(19|20)\d{2}", publication_year):
        raise ValueError("Invalid publication year. Enter a 4-digit year starting with 19 or 20.")

    print("Book details accepted successfully!")

except ValueError as e:
    print("Error:", e)

finally:
    print("Library input validation process completed.")
