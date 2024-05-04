import psycopg2
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="albicocca",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
def insert_from_console():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    cursor.execute(
        "INSERT INTO proc (name, phone_number) VALUES (%s, %s, %s)",
        (name, phone_number)
    )
    conn.commit()
def insert_or_update_user(conn, name, phone):
    cursor = conn.cursor()
    cursor.callproc("insert_or_update_user", (name, phone))
    conn.commit()
    cursor.close()

def insert_many_users(conn, users):
    cursor = conn.cursor()
    incorrect_data = []
    for user in users:
        name, phone = user
        cursor.callproc('insert_user', (name, phone))
    conn.commit()
    cursor.close()
    return incorrect_data

def delete_data(conn, username=None, phone=None):
    cursor = conn.cursor()
    if username:
        cursor.callproc("delete_user_by_name", (username,))
    elif phone:
        cursor.callproc("delete_user_by_phone", (phone,))
    conn.commit()
    cursor.close()
insert_many_users(conn, [('Alice', '9876543210'), ('Bob', '521512521')])
conn.close()
