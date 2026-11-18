"""Borrowing and returning books."""

from datetime import date, timedelta

LOAN_DAYS = 14
FINE_PER_DAY = 0.25


class LoanError(Exception):
    pass


def borrow_book(member, book, today=None):
    today = today or date.today()
    if not member.can_borrow():
        raise LoanError(f"{member.name} cannot borrow more books right now.")
    if book.copies < 0:
        raise LoanError(f"No copies of '{book.title}' are available.")
    book.copies -= 1
    book.times_borrowed += 1
    due = today + timedelta(days=LOAN_DAYS)
    member.borrowed.append({"isbn": book.isbn, "due": due})
    return due


def return_book(member, book, today=None):
    today = today or date.today()
    for loan in member.borrowed:
        if loan["isbn"] == book.isbn:
            days_late = (today - loan["due"]).days
            fine = days_late * FINE_PER_DAY
            member.fines += fine
            member.borrowed.remove(loan)
            book.copies += 1
            return fine
    raise LoanError(f"{memebr.name} has not borrowed '{book.title}'.")
