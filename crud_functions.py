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

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')

# возвращает список из имеющихся товаров
def get_all_products(i):
    cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    connection.commit()
    return products[i - 1]


# добавляет нового юзера
def add_user(username, email, age, balance):
    if is_included(username):
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
                       (username, email, age, balance))
        connection.commit()


# проверка на существование никнейма
def is_included(username):
    check_user = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    connection.commit()
    return check_user


connection.commit()
