"""Command-line demo of the School Library Manager."""

from datetime import date, timedelta

from library import Book, Member, borrow_book, return_book, average_loans_per_member, most_borrowed
from library.storage import save_books, load_books


def main():
    books = load_books("books.json") or [
        Book("978-0132350884", "Clean Code", "Robert C. Martin", copies=2),
        Book("978-0201633610", "Design Patterns", "Gamma et al.", copies=1),
        Book("978-1491946008", "Fluent Python", "Luciano Ramalho", copies=1),
    ]
    alice = Member(1, "Alice")
    bob = Member(2, "Bob")
    report_title = "Monthly report"

    due = borrow_book(alice, books[0])
    print(f"Alice must return '{books[0].title}' by {due}")
    borrow_book(bob, books[1])
    print("Bob's loans:", bob.borrowed)

    fine = return_book(alice, books[0], today=date.today() + timedelta(days=20))
    print(f"Alice paid a fine of {fine:.2f}")

    print("Average loans per member:", average_loans_per_member([alice, bob]))
    print("Most borrowed:", [b.title for b in most_borrowed(books)])
    save_books(books, "books.json")


if __name__ == "__main__":
    main()
