# account-management-microservice
# Requesting actions from account_management.py:
The first line is the command; either "username" to change username, "password" to change password, or
"delete" to delete account.
Second line for username and password commands is the new username/password
Last line is the current user's file
# Examples:

# change username:
username

new_username

old_username.txt

<b>success response:</b>
new_username.txt

<b>fail response:</b>
username fail

# change password:
password

new_password

username.txt

<b>success response:</b>
username.txt

<b>fail response:</b>
password fail

# delete account:
delete

username.txt

<b>success response:</b>
deleted

<b>fail response:</b>
delete failed

```mermaid
sequenceDiagram
  participant m as main.py
  participant t as accountm.txt
  participant p as account_management.py
  participant u as current_user_file.txt
  loop InstructionCheck
    p->>t: check for instruction
  end
  m ->> t: change_username()
  t ->> p: new username#59; current_user_file.txt
  alt file doesn't exist
    p -->> t: username fail
    t -->> m: username fail
  else file exists
    p ->> u: rename file to new_username.txt
    p -->> t: new_username.txt
    t -->> m: new_username.txt
  end
  
  loop InstructionCheck
    p->>t: check for instruction
  end
  m ->> t: change_password()
  t ->> p: new password#59; new_username.txt
  alt file doesn't exist
    p -->> t: password fail
    t -->> m: password fail
  else file exists
    p ->> u: edit file contents to have new password
    p -->> t: new_username.txt
    t -->> m: new_username.txt
  end
  loop InstructionCheck
    p->>t: check for instruction
  end
  m ->> t: delete_account()
  t ->> p: new_username.txt
  alt file doesn't exist
    p -->> t: delete failed
    t -->> m: delete failed
  else file exists
    destroy u
    p -x u: delete file
    p -->> t: deleted
    t -->> m: deleted
  end
  
  loop InstructionCheck
    p->>t: check for instruction
  end
```
