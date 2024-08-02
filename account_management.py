#communication file examples:
#changing username:
	#"cooluser1.txt"

	#"username"
	#"cooluser2"
	#"cooluser1.txt”
#success response:
	#"cooluser2.txt"
#fail response:
	#"username fail"

#changing password:
	#"cooluser1.txt"

	#"password"
	#"new_password7"
	#"cooluser1.txt"
#success response:
	#"cooluser1.txt"
#fail response:
	#"password fail"

#deleting:
	#"cooluser1.txt"

	#"delete"
	#"cooluser1.txt"
#Success response:
	#"deleted"
#fail response:
	#"delete fail"

import time
import os

USER_FILE = 'user.txt'
COMM_FILE = "accountm.txt"
RECORDS_DIR = "records/"

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

def change_username(new_username, current_username):
	print("Changing username...")
	user_data = load_user_data()

	if user_data:
		# Rename user's record file
		old_file = os.path.join(RECORDS_DIR, f'{current_username}.txt')
		new_file = os.path.join(RECORDS_DIR, f'{new_username}.txt')
		if os.path.exists(old_file):
			os.rename(old_file, new_file)
		# Update username in user data
		user_data['username'] = new_username
		save_user_data(user_data['username'], user_data['password'])
		f = open(COMM_FILE, "w")
		f.write(f"{new_username}.txt")
		f.close
		print("Username changed successfully.")
	else:
		f = open(COMM_FILE,"w")
		f.write("username fail")
		f.close()
		print("No user found")
   
        
def change_password(new_password, username):
	print("\nChanging password...")
	user_data = load_user_data()

	if user_data:
		user_data['password'] = new_password
		save_user_data(user_data['username'], user_data['password'])
		f = open(COMM_FILE, "w")
		f.write(f"{username}.txt")
		f.close
		print("Password changed successfully.")		
	else:
		f = open(COMM_FILE, "w")
		f.write("password fail")
		f.close
		print("No user found")
 
        
def delete_account(username):
	if os.path.exists(USER_FILE):
		os.remove(USER_FILE)
		user_file = os.path.join(RECORDS_DIR, f'{username}.txt')
		if os.path.exists(user_file):
			os.remove(user_file)
		f = open(COMM_FILE, "w")
		f.write(f"deleted")
		f.close
		print("Account and all associated records deleted successfully.")
	else:
		f = open(COMM_FILE, "w")
		f.write(f"delete fail")
		f.close
		print("No user found.")

#main loop
while True:
	c = open(COMM_FILE, 'r')
	message = c.readlines()
	if len(message) == 3:
		curr_username = message[2].split(".")
		curr_username = curr_username[0]
		if message[0] == "username\n":
			new = message[1].split("\n")
			new = "".join(new) 
			change_username(new, curr_username)
		elif message[0] == "password\n":
			new = message[1].split("\n")
			new = "".join(new) 
			change_password(new, curr_username)
		else:
			print("Communciation error; command not found for " + COMM_FILE)
			print(message[0])
	elif len(message) == 2:
		if message[0] == "delete\n":
			curr_username = message[1].split(".")
			curr_username = curr_username[0]
			delete_account(curr_username)
		else:
			print("Communciation error; command not found for " + COMM_FILE)
			print(message[0])
	c.close()
	time.sleep(2)
		
		
