import hashlib

def hash_password(password: str) -> str:
    """
    Takes a plain-text password, encodes it into bytes, 
    hashes it using SHA-256, and returns the hexadecimal string.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(users_db: dict):
    """Handles new user sign-up and stores their hashed password."""
    print("\n--- REGISTER NEW USER ---")
    username = input("Enter a new username: ").strip()
    
    if not username:
        print("[-] Error: Username cannot be blank.")
        return
        
    if username in users_db:
        print("[-] Error: Username already exists! Try a different one.")
        return

    password = input("Enter a password: ").strip()
    if not password:
        print("[-] Error: Password cannot be blank.")
        return

    # Securely hash the password (never store plain-text!)
    hashed_pw = hash_password(password)
    
    # Save the username and its hash in our dictionary database
    users_db[username] = hashed_pw
    print(f"[+] Success! User '{username}' has been registered.")

def login_user(users_db: dict):
    """Handles user login verification by checking hashes."""
    print("\n--- USER LOGIN ---")
    username = input("Enter your username: ").strip()
    
    if username not in users_db:
        print("[-] Error: Username not found. Please register first.")
        return

    password = input("Enter your password: ").strip()
    
    # Hash the password entered by the user during login
    hashed_input_pw = hash_password(password)
    
    # Compare the newly hashed input with the stored hash
    if users_db[username] == hashed_input_pw:
        print(f"[+] Access Granted! Welcome back, {username}!")
    else:
        print("[-] Access Denied: Incorrect password.")

def main():
    # In-memory "database" dictionary 
    # Structure: { "username": "sha256_hashed_password_string" }
    users_db = {}
    
    while True:
        print("\n=== Secure Auth System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            register_user(users_db)
        elif choice == '2':
            login_user(users_db)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("[-] Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()