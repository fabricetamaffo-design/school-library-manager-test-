# School Library Manager

A small Python application for a school library: it tracks books, members and loans,
computes late-return fines and produces simple monthly statistics.

## Structure

```
main.py              command-line demo
library/
  models.py          Book and Member classes
  loans.py           borrowing and returning books, fines
  stats.py           statistics for the monthly report
  storage.py         save / load the catalogue as JSON
```

## Run

```bash
python main.py
```

Requires Python 3.10+. No external dependencies.
