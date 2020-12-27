import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# creates the table
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# inserting a row
user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# inserting multiple rows
users = [
    (2, 'bob', '1234'),
    (3, 'john', 'secret')
]
cursor.executemany(insert_query, users)

# selecting rows
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()