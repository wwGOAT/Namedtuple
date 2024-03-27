import psycopg2 as eldor

database = eldor.connect(
    database="homework_6",
    host="localhost",
    user="postgres",
    password="eldor12"
)
cursor = database.cursor()
qwerty = " SELECT * FROM author WHERE author_id IN (SELECT author_id FROM authorbook WHERE book_id IN(SELECT book_id FROM book WHERE title = 'Python'));"
cursor.execute(qwerty)
for i in cursor.fetchall():
    print(i)