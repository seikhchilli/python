password = input("Enter your password: ")

count = 0

for i in password:
    if i >= '0' and i <= '9':
        count += 1

if len(password) >= 8 and password.isalnum() and count >= 2:
    print("Valid password.")
else:
    print("Invalid password.")
    