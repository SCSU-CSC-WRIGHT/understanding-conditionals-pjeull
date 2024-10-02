password = input("Please create a password: ")
password_check = input("Guess the password! ")

if password_check == password:
    print("Access granted.")
else:
    print("Access denied.")