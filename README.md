# Secure User Login & Registration System (Python)

A beginner-friendly, console-based authentication system built in Python. This project demonstrates core information security principles, specifically **cryptographic hashing** and secure credential handling, using only standard Python libraries.

## 🚀 Features

- **User Registration:** Allows new users to sign up with a unique username and password.
- **Cryptographic Hashing:** Uses Python's built-in `hashlib` (SHA-256) to convert plain-text passwords into irreversible hashes before storing them. Plain-text passwords are never stored.
- **Login Verification:** Authenticates users by hashing their login attempt and comparing it against the stored hash.
- **Input Validation:** Prevents blank inputs and duplicate usernames.

---

## 🛠️ Core Concepts Covered

- **Dictionaries:** Using Python dictionaries (`dict`) as an in-memory database that maps usernames to password hashes.
- **Functions:** Modular code structure separating registration, login, and hashing logic.
- **Cryptographic Hashing (SHA-256):** Understanding why modern applications never store passwords in plain text.
- **Control Flow:** Using `while` loops and conditional statements (`if/else`) to build an interactive menu.

---

## 💻 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed. You can check your version by running:

```bash
python --version
```

### Running the Program

1. Clone this repository or download the `auth_system.py` file.
2. Open your terminal or command prompt in the project directory.
3. Run the script:

```bash
python auth_system.py
```

---

## 🕹️ Usage Example

When you run the script, you will see an interactive console menu:

```text
=== Secure Auth System ===
1. Register
2. Login
3. Exit
Choose an option (1-3): 1

--- REGISTER NEW USER ---
Enter a new username: alice
Enter a password: MySecurePassword123
[+] Success! User 'alice' has been registered.
```

---

## 🔒 Security Note

This project uses SHA-256 for educational purposes to demonstrate basic hashing. In production systems, passwords should be hashed with slow, salted algorithms designed for password storage (such as **Argon2**, **bcrypt**, or **PBKDF2**) to defend against brute-force and rainbow table attacks.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
