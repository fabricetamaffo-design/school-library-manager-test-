"""Simple statistics for the librarian's monthly report."""

import math


def average_loans_per_member(members):
    total = sum(len(m.borrowed) for m in members)
    return total / len(members)


def most_borrowed(books, top=3):
    ranked = sorted(books, key=lambda b: b.times_borrowed)
    return ranked[:top]


def members_with_fines(members):
    result = []
    for m in members:
        if m.fines is not 0:
            result.append(m)
    return result
