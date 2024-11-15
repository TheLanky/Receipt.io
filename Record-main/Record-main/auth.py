#can be used for sign up and sign in
#make sure the database is set right
'''
import bcrypt
from database import get_connection
import sqlite3

def sign_up(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("Sign-up successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please try another.")
    finally:
        conn.close()

def sign_in(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        user_id, stored_password = result
        if bcrypt.checkpw(password.encode(), stored_password):
            print("Sign-in successful! User ID:", user_id)
            return user_id
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

'''
import sqlite3
import hashlib

# Connect to SQLite database
'''conn = sqlite3.connect('receipts.db')
c = conn.cursor()'''
conn = sqlite3.connect('receipts.db', check_same_thread=False)
c = conn.cursor()

# Create a users table
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                phone TEXT NOT NULL
            )''')
conn.commit()

# Helper function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Sign-up function
def sign_up(email, password, phone):
    hashed_password = hash_password(password)

    try:
        # Insert the new user
        c.execute('INSERT INTO users (email, password, phone) VALUES (?, ?, ?)',
                  (email, hashed_password, phone))
        conn.commit()
        print(f"User {email} registered successfully!")
        return True
    except sqlite3.IntegrityError:
        print("User with this email already exists.")
        return False

# Sign-in function
def sign_in(email, password):
    hashed_password = hash_password(password)

    # Verify the user's credentials
    c.execute('SELECT id FROM users WHERE email = ? AND password = ?', (email, hashed_password))
    user = c.fetchone()

    if user:
        print(f"User {email} signed in successfully!")
        return user[0]  # Return user ID for linking receipts
    else:
        print("Invalid email or password.")
        return None

# Function to close the connection
def close_connection():
    conn.close()

# Example usage
if __name__ == "__main__":
    # Sign up a new user
    sign_up('user@example.com', 'securepassword123', '555-1234')

    # Sign in with existing user credentials
    user_id = sign_in('user@example.com', 'securepassword123')

    # Close the connection
    close_connection()
