import sqlite3

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')


def get_all_products(i):
    cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    connection.commit()
    return products[i - 1]


connection.commit()
connection.close()