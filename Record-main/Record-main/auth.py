#can be used for sign up and sign in
#make sure the database is set right
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
