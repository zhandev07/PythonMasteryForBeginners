import os
import json
import base64

# Function to load passwords from a file
def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            return json.load(file)
    return {}

# Function to save passwords to a file
def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

# Function to encode the password (simple base64 encoding)
def encode_password(password):
    password_bytes = password.encode('utf-8')
    base64_bytes = base64.b64encode(password_bytes)
    return base64_bytes.decode('utf-8')

# Function to decode the password
def decode_password(encoded_password):
    base64_bytes = encoded_password.encode('utf-8')
    password_bytes = base64.b64decode(base64_bytes)
    return password_bytes.decode('utf-8')

# Function to add a new password
def add_password(passwords):
    service = input("Enter the service name (e.g., Gmail, Facebook): ").strip()
    username = input(f"Enter the username for {service}: ").strip()
    password = input(f"Enter the password for {service}: ").strip()
    encoded_password = encode_password(password)

    passwords[service] = {"username": username, "password": encoded_password}
    save_passwords(passwords)
    print(f"Password for {service} added successfully.")

# Function to retrieve a password
def retrieve_password(passwords):
    service = input("Enter the service name to retrieve the password for: ").strip()
    if service in passwords:
        username = passwords[service]["username"]
        password = decode_password(passwords[service]["password"])
        print(f"Service: {service}")
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print(f"No password found for {service}.")

# Function to delete a password
def delete_password(passwords):
    service = input("Enter the service name to delete the password for: ").strip()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f"Password for {service} deleted successfully.")
    else:
        print(f"No password found for {service}.")

# Main menu function
def main_menu():
    passwords = load_passwords()
    
    while True:
        print("\nPassword Manager Menu:")
        print("1. Add a Password")
        print("2. Retrieve a Password")
        print("3. Delete a Password")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_password(passwords)
        elif choice == "2":
            retrieve_password(passwords)
        elif choice == "3":
            delete_password(passwords)
        elif choice == "4":
            print("Exiting the password manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
