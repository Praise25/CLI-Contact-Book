from required import Contact, remove_from_database, show_database, add_to_database, find_in_database, update_database, display_record
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--insert", help="Insert a record into the contact book", action="store_true")
parser.add_argument("-l", "--list", help="List all the records in the database", action="store_true")
parser.add_argument("-r", "--remove", help="Remove a record from the contact book", action="store_true")
parser.add_argument("-u", "--update", help="Update a specific field in a record", action="store_true")
parser.add_argument("-f", "--find", help="Find and retrieve the record of a specified contact", action="store_true")
args = parser.parse_args()


if args.insert:
    lastname = input("Lastname: ")
    firstname = input("Firstname: ")
    email = input("Email: ")
    phone_no = input("Phone Number: ")
    contact = Contact(lastname, firstname, phone_no, email)
    add_to_database(contact)
elif args.remove:
    query = input("Enter the phone number of the contact to be deleted: ")
    remove_from_database(query)
elif args.list:
    show_database()
elif args.find:
    key = input("Enter detail to search with: ")
    query = input("Enter field to search for: ")
    record = find_in_database(key, query)
    display_record(record)
elif args.update:
    contact_phone_no = input("Enter the phone number of the contact to be updated: ")
    key = input("Enter column to be updated: ")
    new_detail = input(f"Enter the new detail: ")
    update_database(key, contact_phone_no, new_detail)