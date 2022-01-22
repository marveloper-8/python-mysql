import mysql.connector

a = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='mydatabase'
)

b = a.cursor()

c = 'SELECT * FROM customers ORDER BY name DESC'

b.execute(c)

d = b.fetchall()

for e in d:
    print(e)

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

# mydb.commit()
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