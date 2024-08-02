# account-management-microservice
# Requesting actions from account-management.py:
# The first line is the command; either "username" to change username, "password" to change password, or
# "delete" to delete account.
# Second line for usernmae and password commands is the new username/password
# Last line is the current user's file
# Examples:

# change username:
username
new_username
old_username.txt

# success response:
new_username.txt
# fail response:
username fail

# change password:
password
new_password
username.txt

# success response:
username.txt
# fail response:
password fail

# delete account:
delete
username.txt

# success response:
deleted
# fail response:
delete failed
