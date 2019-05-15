import sqlite3

def create_table():
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS User(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            phone VARCHAR(255) NOT NULL,
            additional_info TEXT);
        """)
    connection.commit()
    connection.close()

def add_user(full_name, email, age, phone, additional_info):
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO User (full_name, email, age, phone, additional_info) VALUES('{full_name}', '{email}', '{age}', '{phone}', '{additional_info}')
        """.format(full_name=full_name, email=email, age=age, phone=phone, additional_info=additional_info)
    )
    connection.commit()
    connection.close()

def list_users():
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    return users

def get_user(id):
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM User WHERE id={id}".format(id=id))
    user = cursor.fetchall()
    connection.commit()
    connection.close()
    return user[0]

def delete_user(id):
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM User WHERE id={id}".format(id=id))
    user = cursor.fetchall()
    cursor.execute("DELETE FROM User WHERE id={id}".format(id=id))
    connection.commit()
    connection.close()
    return user[0]
