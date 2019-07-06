from required import Contact, remove_from_database, show_database, add_to_database, find_in_database, update_record
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--insert", help="Insert a record into the contact book", nargs=4)
parser.add_argument("-r", "--remove", help="Remove a record from the contact book")
parser.add_argument("-u", "--update", help="Update a specific field in a record", nargs=3)
parser.add_argument("-f", "--find", help="Find and retrieve the record of a specified contact", nargs=2)
parser.add_argument("-l", "--list", help="List all the records in the database")
args = parser.parse_args()

# TODO: Refactor insert to accept the inputs separately and check argparse documentation for how to run a function when an argument is used
if args.insert:
    lastname, firstname, email, phone_no = args.insert
    contact = Contact(lastname, firstname, phone_no, email)
    add_to_database(contact)
elif args.remove:
    remove_from_database(args.remove)
elif args.list:
    show_database()
elif args.find:
    key = args.find[0]
    query = args.find[1]
    find_in_database(key, query)
elif args.update:
    key = args.update[0]
    query1 = args.update[1]
    query2 = args.update[2]
    update_record(key, query1, query2)
