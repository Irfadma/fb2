# A simple login system in Python

# Dictionary to store usernames and passwords (for demonstration purposes)
user_credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists and if the password matches
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

# Main function
def main():
    print("Welcome to the Login Page")
    login()

if __name__ == "__main__":
    main()

