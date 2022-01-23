import mysql.connector

a = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='mydatabase'
)

b = a.cursor()
c = 'SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    INNER JOIN products on users.fav = products.id'

b.execute(c)
d = b.fetchall()
for e in d:
    print(e)

# b.execute('DROP TABLE products')
# c = 'INSERT INTO products (id, name) VALUES (%s, %s)'
# print(b.rowcount, "record(s) inserted")
# d = [
#     (154, 'Chocolate Heaven'),
#     (155, 'Tasty Lemons') ,
#     (156, 'Vanilla Dreams')
# ]
# b.executemany(c, d)
# a.commit()
# print(b.rowcount, "record(s) inserted.")
# b.execute('ALTER TABLE products AUTO_INCREMENT=154')
# b.execute('CREATE TABLE products (id int(255), name VARCHAR(255))')
# b.execute('DROP TABLE users')
# c = 'DELETE FROM users WHERE id >= 6'
# d = (6)
# b.execute(c)
# a.commit()
# print(b.rowcount, "record(s) deleted")
# c = 'INSERT INTO users (name, fav) VALUES (%s, %s)'
# d = [
#     ('John',  154),
#     ('Peter',  154),
#     ('Amy',  155),
#     ('Hannah', 0),
#     ('Michael', 0)
# ]
# b.executemany(c, d)
# a.commit()
# print(b.rowcount, "record(s) inserted.")
# b.execute('ALTER TABLE users ADD fav int(255)')
# b.execute('ALTER TABLE users DROP COLUMN address')
# b.execute('ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
# b.execute('CREATE TABLE users (name VARCHAR(255), fav VARCHAR(255))')

# b.execute('SELECT * FROM customers LIMIT 5 OFFSET 2')
# c = b.fetchall()

# for d in c:
#     print(d)

# b.execute('SELECT * FROM customers LIMIT 5')
# c = b.fetchall()

# for d in c:
#     print(d)

# c = 'UPDATE customers SET address=%s WHERE address=%s'
# d = ('Valley 345', 'Canyon 123')
# b.execute(c, d)
# a.commit()
# print(b.rowcount, "record(s) affected")

# b = a.cursor()

# c = 'UPDATE customers SET address="Canyon 123" WHERE address="Valley 345"'
# b.execute(c)
# a.commit()
# print(b.rowcount, "record(s) affected")

# mycursor = a.cursor()
# c = 'DROP TABLE IF EXISTS customers'

# b.execute(c)

# b = a.cursor()

# c = 'DROP TABLE customers'
# b.execute(c)

# b = a.cursor()

# c = 'DELETE FROM customers WHERE address = %s'
# d = ('Yellow Garden 2',)

# b.execute(c, d)
# a.commit()
# print(b.rowcount, 'record(s) deleted')

# b = a.cursor()

# c = 'DELETE FROM customers WHERE address = "Mountain 21"'

# b.execute(c)
# a.commit()

# print(b.rowcount, "record(s) deleted")

# b = a.cursor()

# c = 'SELECT * FROM customers ORDER BY name DESC'

# b.execute(c)

# d = b.fetchall()

# for e in d:
#     print(e)

# b = a.cursor()

# c = 'SELECT * FROM customers WHERE address=%s'
# d = ('Yellow Garden 2', )

# b.execute(c, d)
# e = b.fetchall()
# for f in e:
#     print(f)

# c = 'SELECT * FROM customers WHERE address LIKE "%way%"'
# b.execute(c)
# d = b.fetchall()
# for e in d:
#     print(e)

# c = 'SELECT * FROM customers WHERE address="Park Lane 38"'
# b.execute(c)
# d = b.fetchall()
# for e in d:
#     print(e)

# b.execute('SELECT * FROM customers')
# c = b.fetchone()
# print(c)

# b.execute('SELECT name, address FROM customers')
# c = b.fetchall()
# for d in c:
#     print(d)

# b.execute('SELECT * FROM customers')
# c = b.fetchall()

# for d in c:
#     print(d)

# sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
# val = ('Michelle', 'Blue Village')
# mycursor.execute(sql, val)

# mydb.commit()
# print('1 record inserted, ID:', mycursor.lastrowid)

# sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)

# a.commit()
# print(mycursor.rowcount, "record inserted.")

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)