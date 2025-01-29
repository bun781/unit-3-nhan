import sqlite3

haiku = '''Code flows like a stream
Algorithms guide its way
In silence, it solves
'''

# Create Database with table Words
database_name = "quiz039.db"

con = sqlite3.connect(database_name)
cursor = con.cursor()

query_create_table = '''
create table word(
    word TEXT,
    length INTEGER
)
'''

cursor.execute(query_create_table)
con.commit()

for word in haiku.split():
    query = f"INSERT into word(word, length) values ('{word}', '{len(word)}')"
    cursor.execute(query)
    con.commit()

# query the average of all the lengths
output = cursor.execute('''
SELECT AVG(length)
FROM word
''')
result = output.fetchall()
print(result)

# close database
con.close()
