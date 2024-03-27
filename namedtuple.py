from collections import namedtuple

books = list()
Book = namedtuple('Book', ['title', 'author', 'year', 'pages', 'language'], defaults=[None, None, None, None, None])

def test_book():
    book = input("""
    1. kitob qoshish
    2. hamma kitoblar
    3. Eng katta kitob
    0. chiqish
            >>>""")

    if book == '1':
        return qoshish()

    elif book == '2':
        return hammasi()

    elif book == '3':
        return year()

    elif book == '0':
        while book == 0:
            break

    else:
        print("Error")
        return test_book()

def qoshish():
    title = input("title: ")
    author = input("author: ")
    year = input("year: ")
    pages = input("pages: ")
    language = input("language: ")

    add_book = Book(title, author, year, pages, language)
    books.append(add_book)
    return test_book()

def hammasi():
    for i in books:
        print(f"""
        Title: {i.title}
        Author: {i.author}
        Year: {i.year}
        Pages: {i.pages}
        Language: {i.language}""")
    return test_book()


def year():
    min_year_book = books[0]
    for book in books:
        if int(book[2]) < int(min_year_book[2]):
            min_year_book = book
    print(f"{min_year_book.year}")
    return test_book()


if __name__ == "__main__":
    test_book()