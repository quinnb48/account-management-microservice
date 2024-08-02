from datetime import datetime
import time
import os

# File paths
USER_FILE = 'user.txt'
RECORDS_DIR = 'records/'
ACC_COM_FILE = 'accountm.txt'


# Utility function to load user data
def load_user_data():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            data = f.read().strip()
            if data:
                username, password = data.split(',')
                return {'username': username, 'password': password}
    return {}


# Utility function to save user data
def save_user_data(username, password):
    with open(USER_FILE, 'w') as f:
        f.write(f'{username},{password}')


# Utility function to load records for the current user
def load_records(username):
    user_file = os.path.join(RECORDS_DIR, f'{username}.txt')
    records = []
    if os.path.exists(user_file):
        with open(user_file, 'r') as f:
            for line in f:
                record_id, title, body, creation_date = line.strip().split(',')
                records.append({'id': int(record_id), 'title': title, 'body': body, 'creation_date': creation_date})
    return records


# Utility function to save records for the current user
def save_records(username, records):
    user_file = os.path.join(RECORDS_DIR, f'{username}.txt')
    os.makedirs(RECORDS_DIR, exist_ok=True)
    with open(user_file, 'w') as f:
        for record in records:
            f.write(f"{record['id']},{record['title']},{record['body']},{record['creation_date']}\n")


def main_menu(username):
    while True:
        print("\nMain Menu")
        print("Please enter your desired option number, or enter 'back' or hit 'Enter' to go back to the login page.")
        print("1. Account management")
        print("2. Access Records")
        choice = input("Your choice: ").strip()

        if choice == '1':
            account_management(username)
        elif choice == '2':
            records_management(username)
        elif choice == '' or choice.lower() == 'back':
            login()
        else:
            print("Invalid choice. Please try again.")


def account_management(username):
    while True:
        print("\nAccount Management Page")
        print("Please feel free to change any information related to your account here.")
        print(
            "Please enter 'back' or hit 'Enter' to go back to the previous page. Otherwise, enter the option number "
            "below:")
        print("1. Change username")
        print("2. Change password")
        print("3. Delete account")
        print(
            "WARNING: deleting your account not only deletes your account information, but also all records "
            "associated with your account. This action is immediate and non-reversible, please take caution before "
            "proceeding.")
        choice = input("Your choice: ").strip()

        if choice == '' or choice.lower() == 'back':
            main_menu(username)

        if choice == '1':
            change_username(username)
        elif choice == '2':
            change_password(username)
        elif choice == '3':
            delete_account(username)
        else:
            print("Invalid choice. Please try again.")


def change_username(current_username):
    print("\nChange Username")
    new_username = input("Please enter your new username, or enter 'back' or hit 'Enter' to go back to the previous "
                         "page: ").strip()
    user_data = load_user_data()

    if new_username == '' or new_username.lower() == 'back':
        account_management(current_username)

    if user_data:
        c = open(ACC_COM_FILE, 'w')
        c.write(f"username\n{new_username}\n{current_username}.txt")
        c.close()
        while True:
        	time.sleep(2)
        	c = open(ACC_COM_FILE, 'r')
        	message = c.readlines()
        	if len(message) == 1:
        		if message[0] == "username fail":
        			print("No user found. Please create an account first.")
        		else:
        			print("Username changed successfully")
        		c.close()
        		break
        	c.close()
    else:
        print("No user found. Please create an account first.")


def change_password(username):
    print("\nChange Password")
    password = input("Please enter your new password, or enter 'back' or hit 'Enter' to go back to the previous "
                     "page: ").strip()
    user_data = load_user_data()

    if password == '' or password.lower() == 'back':
        account_management(username)

    if user_data:
        c = open(ACC_COM_FILE, 'w')
        c.write(f"password\n{password}\n{username}.txt")
        c.close()
        while True:
        	time.sleep(2)
        	c = open(ACC_COM_FILE, 'r')
        	message = c.readlines()
        	if len(message) == 1:
        		if message[0] == "password fail":
        			print("No user found. Please create an account first.")
        		else:
        			print("Password changed successfully")
        		c.close()
        		break
        	c.close()
    else:
        print("No user found. Please create an account first.")


def delete_account(username):
    delete = input("Please enter 'confirm' to delete your account, or enter 'back' or hit 'Enter' to go back to the "
                   "previous page: ").strip()
    if delete == 'confirm':
        c = open(ACC_COM_FILE, 'w')
        c.write(f"delete\n{username}.txt")
        c.close()
        while True:
        	time.sleep(2)
        	c = open(ACC_COM_FILE, 'r')
        	message = c.readlines()
        	if len(message) == 1:
        		if message[0] == "delete fail":
        			print("No user found. Please create an account first.")
        		else:
        			print("Account and all associated records deleted successfully.")
        		c.close()
        		login()
        		break
        	c.close()
    elif delete == '' or delete.lower() == 'back':
        account_management(username)


def records_management(username):
    while True:
        print("\nRecord Management Screen")
        print("Please enter your desired option number, or enter 'back' or hit 'Enter' to return to the previous page.")
        print("1. Create a new record")
        print("2. Update a record by id")
        print("3. Read a record by id")
        print("4. Look up a record by id")
        print("5. Delete a record by id")
        print("6. List all records")
        choice = input("Your choice: ").strip()

        if choice == '' or choice.lower() == 'back':
            main_menu(username)

        if choice == '1':
            create_record(username)
        elif choice == '2':
            update_record(username)
        elif choice == '3':
            read_record(username)
        elif choice == '4':
            find_record(username)
        elif choice == '5':
            delete_record(username)
        elif choice == '6':
            list_records(username)
        else:
            print("Invalid choice. Please try again.")


def create_record(username):
    print("\nCreate a new record")
    print('You can create a new record here. A record allows you to create an entry in our system, including a title '
          'and a body. Feel free to record whatever you want here.')
    print("Please enter below the title of your new record. Enter 'back' to return to the previous page, "
          "or enter 'cancel' to start again.")
    title = input().strip()
    if title == '':
        create_record(username)
    elif title.lower() == 'back':
        records_management(username)
    elif title.lower() == 'cancel':
        create_record(username)

    print("Please enter below the body of your new record. Enter 'back' to return to the previous page, "
          "or enter 'cancel' to start again.")
    body = input().strip()
    if body == '':
        create_record(username)
    elif title.lower() == 'back':
        records_management(username)
    elif body.lower() == 'cancel':
        create_record(username)

    records = load_records(username)
    record_id = len(records) + 1
    creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"\nThis is your new record:\nTITLE: {title}\nBODY: {body}\nID: {record_id}")
    print("Please hit Enter to confirm, or enter 'cancel' to start again and 'back' to return to the previous page.")
    entry = input()
    if entry == '':
        record = {'id': record_id, 'title': title, 'body': body, 'creation_date': creation_date}
        records.append(record)
        save_records(username, records)
    elif entry.lower() == 'cancel':
        create_record(username)
    elif entry.lower() == 'back':
        records_management(username)


def update_record(username, record_id=None):
    print("\nUpdate a record")
    print(
        'To update a record, you need to separately enter the new title and body content, but the old title and '
        'content will be lost after the update.')
    if not record_id:
        print("Please enter the id number of the record you wish to update. Alternatively, enter 'back' or hit "
              "'Enter' to return to the previous screen.")
        record_id = input().strip()

    if record_id == '' or record_id.lower() == 'back':
        records_management(username)

    records = load_records(username)
    record = next((rec for rec in records if rec['id'] == int(record_id)), None)

    if record:
        print(f"Below is the current title of your record: {record['title']}, hit Enter to confirm or enter a new one:")
        title = input().strip()
        print(f"Below is the current body of your record: {record['body']}, hit Enter to confirm or enter a new one:")
        body = input().strip()

        record['title'] = title if title else record['title']
        record['body'] = body if body else record['body']

        print(f"\nThis is your updated record:\nTITLE: {record['title']}\nBODY: {record['body']}")
        print('')
        print("Please hit Enter to confirm, or enter 'cancel' to try again. Please be aware that the modification "
              "will be immediate and final, and there is no way for you to revert the changes made.")
        response = input()

        if response == '':
            save_records(username, records)
        elif response.lower() == 'cancel':
            update_record(username, record_id)

    else:
        print("The record you are looking for does not exist, please try again.")


def read_record(username, record_id=None):
    print("\nRead a record")

    if not record_id:
        record_id = input("Please enter the id number of the record you wish to read: ").strip()

    records = load_records(username)
    record = next((rec for rec in records if rec['id'] == int(record_id)), None)

    if record:
        print(f"\nThis is the record you wished to read:\nTITLE: {record['title']}\nBODY: {record['body']}")
        print("Please enter 'back' or hit 'Enter' to go back to the previous screen, or enter the option number below:")
        print("1. Update this record")
        print("2. Delete this record")
        print("Alternatively, enter 'info' to see more details about this entry")

        choice = input("Your choice: ").strip()
        if choice == '' or choice.lower() == 'back':
            records_management(username)

        if choice == '1':
            update_record(username, record_id)
        elif choice == '2':
            delete_record(username, record_id)
        elif choice == 'info':
            info(record)
            return
        else:
            print("Invalid choice. Please try again.")
    else:
        print("The record you are looking for does not exist, please try again.")


def info(record):
    print(f"\nRecord Information:\nTITLE: {record['title']}\nBODY: {record['body']}")
    print(f"CREATION DATE: {record['creation_date']}")
    record_size = len(record['title']) + len(record['body'])
    print(f"SIZE: {record_size} bytes")
    input("Press Enter to go back...")


def find_record(username):
    print("\nLook up a record")
    record_id = input("Please enter the id number of the record you wish to find, or enter 'back' or hit 'ESC' to go "
                      "back to the previous screen").strip()
    if record_id == '' or record_id.lower() == 'back':
        records_management(username)

    records = load_records(username)
    record = next((rec for rec in records if rec['id'] == int(record_id)), None)

    if record:
        read_record(username, record_id)
    else:
        print("The record you are looking for does not exist, please try again.")


def delete_record(username, record_id=None):
    print("\nDelete a record")
    if not record_id:
        record_id = input("Please enter the id number of the record you wish to delete: ").strip()

    records = load_records(username)
    record = next((rec for rec in records if rec['id'] == int(record_id)), None)

    if record:
        print(f"\nThis is the record you wish to delete:\nTITLE: {record['title']}\nBODY: {record['body']}")
        print("Please enter 'confirm' to confirm, or enter 'back' or hit 'Enter' to go back to the previous page.")
        confirmation = input("Your choice: ").strip()
        if confirmation == '' or confirmation.lower() == 'back':
            records_management(username)
        elif confirmation.lower() == 'confirm':
            records.remove(record)
            save_records(username, records)

            print("Record deleted successfully.")
    else:
        print("The record you are looking for does not exist, please try again.")


def list_records(username):
    print("\nList all records")
    records = load_records(username)
    if records:
        for record in records:
            print(f"\nID: {record['id']}\nTITLE: {record['title']}\nBODY: {record['body']}")
    else:
        print("No records found.")


def login():
    print("\nLogin Page")
    user_data = load_user_data()
    print(
        "Welcome to our command-line data management system!\nPlease start entering your username. Otherwise, "
        "enter 'new' to create a new account ")
    username = input().strip()

    if username.lower() == 'new':
        create_account()
    elif 'username' in user_data and user_data['username'] == username:
        password = input("Please enter your password: ").strip()
        if user_data['password'] == password:
            print("Login successful.")
            main_menu(username)
        else:
            print("Incorrect password. Please try again.")
            login()
    else:
        print("Username not found. Please try again.")
        login()


def create_account():
    print("\nCreate Account Page")
    user_data = load_user_data()
    username = input("Please start by entering your username, or enter 'back' or hit 'Enter' to go back to the "
                     "previous page.").strip()
    if username.lower() == 'back' or username == '':
        login()
    password = input("Please enter your password, or enter 'back' or hit 'Enter' to go back to the "
                     "previous page.").strip()
    if password.lower() == 'back' or password == '':
        login()
    confirm_password = input("Please enter your password again to confirm: ").strip()

    if password != confirm_password:
        print("Your passwords do not match. Please enter again.")
        create_account()

    if user_data:
        print("An account already exists. Please log in.")
        login()
    else:
        save_user_data(username, password)
        print("Account created successfully.")
        login()


if __name__ == "__main__":
    login()
