import sqlite3


class Contact:
    def __init__(self, lastname, firstname, phone_no, email):
        self.lastname = lastname
        self.firstname = firstname
        self.phone_no = phone_no
        self.email = email
    
    def get_lastname(self):
        return self.lastname
    
    def get_firstname(self):
        return self.firstname

    def get_phone_no(self):
        return self.phone_no
    
    def get_email(self):
        return self.email


def add_to_database(contact):
    lastname = contact.get_lastname()
    firstname = contact.get_firstname()
    email = contact.get_email()
    phone_no = contact.get_phone_no()
    conn = sqlite3.connect("contacts.db")
    conn.execute("CREATE TABLE IF NOT EXISTS contacts (contact_id INTEGER PRIMARY KEY, lastname TEXT, firstname TEXT, email TEXT, phone_number TEXT)")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (lastname, firstname, email, phone_number) VALUES(?, ?, ?, ?)", (lastname, firstname, email, phone_no))
    conn.commit()
    cursor.close()
    conn.close()
    print("Record inserted successfully")

def remove_from_database(query):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    record = list(cursor.execute("SELECT * FROM contacts"))
    if is_present(query, record):
        cursor.execute("DELETE FROM contacts WHERE phone_number=?", (query,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Record deleted successfully")
    else:
        print("Record not found")

def show_database():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    display_record(cursor)

def find_in_database(search_key, query):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM contacts WHERE {} LIKE '{}'".format(search_key, query))
        records = list(cursor)
        if records:
            display_record(records)
        else:
            print(f"The record with {search_key} as {query} does not exist")
    except sqlite3.OperationalError:
        print(f"The search key {search_key} does not exist")
        print("Please use one of the following")
        print("- lastname\n- firstname\n- email\n- phone_number")
    cursor.close()
    conn.close()

def update_record(column, old_value, new_value):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE contacts SET {0}='{1}' WHERE {0} LIKE '{2}'".format(column, new_value, old_value))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Successfully updated column {column} from {old_value} to {new_value}")
    except sqlite3.OperationalError:
        print(f"The column {column} does not exist in the database")
    
def is_present(element, set):
    present = False
    for subset in set:
        if element in subset:
            present = True
            break
    return present

def display_record(record):
    for _, lastname, firstname, email, phone_number in record:
            print(f"Lastname: {lastname}")
            print(f"Firstname: {firstname}")
            print(f"Email: {email}")
            print(f"Phone Number: {phone_number}")
            print("===========================================")