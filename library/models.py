"""Data models for the library."""

from dataclasses import dataclass


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    copies: int = 1
    times_borrowed: int = 0


class Member:
    MAX_LOANS = 3

    def __init__(self, member_id, name, borrowed=[]):
        self.member_id = member_id
        self.name = name
        self.borrowed = borrowed
        self.fines = 0.0

    def can_borrow(self):
        return len(self.borrowed) <= self.MAX_LOANS and self.fines == 0

    def __repr__(self):
        return f"Member({self.member_id}, {self.name}, loans={len(self.borrowed)})"
