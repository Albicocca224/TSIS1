import csv
import psycopg2
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="albicocca",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
def insert_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cursor.execute(
                "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )
    conn.commit()
def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    cursor.execute(
        "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
        (first_name, last_name, phone_number)
    )
    conn.commit()
def update_contact(contact_id, new_first_name, new_phone_number):
    cursor.execute(
        "UPDATE contacts SET first_name = %s, phone_number = %s WHERE id = %s",
        (new_first_name, new_phone_number, contact_id)
    )
    conn.commit()
def query_contacts_by_name(name):
    cursor.execute(
        "SELECT * FROM contacts WHERE first_name = %s OR last_name = %s",
        (name, name)
    )
    return cursor.fetchall()
def delete_contact_by_name(name):
    cursor.execute(
        "DELETE FROM PhoneBook WHERE first_name = %s OR last_name = %s",
        (name, name)
    )
    conn.commit()
def delete_contact_by_phone(phone):
    cursor.execute(
        "DELETE FROM PhoneBook WHERE phone_number = %s",
        (phone,)
    )
    conn.commit()