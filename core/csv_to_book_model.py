from .models import Book
import csv


with open('sample_books.csv') as f:
    reader = csv.reader(f)
    next(reader, None)  # Skip the first row
    for row in reader:
        _, created = Book.objects.get_or_create(
            title=row[0],
            author=row[1],
            url=row[2],
            description=row[3]
        )
