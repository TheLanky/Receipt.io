"""
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('receipts.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS receipts (
                id INTEGER PRIMARY KEY,
                vendor TEXT,
                receipt_date TEXT,
                total_amount_given REAL,
                change REAL,
                payment_method TEXT,
                amount REAL,
                category TEXT
            )''')

# Function to create a new receipt
def create_receipt(vendor, receipt_date, total_amount_given, change, payment_method, amount, category):
    c.execute('''INSERT INTO receipts (vendor, receipt_date, total_amount_given, change, payment_method, amount, category)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''', (vendor, receipt_date, total_amount_given, change, payment_method, amount, category))
    conn.commit()

# Function to read all receipts
def read_receipts():
    c.execute('SELECT * FROM receipts')
    return c.fetchall()

# Function to update a receipt
def update_receipt(receipt_id, vendor, receipt_date, total_amount_given, change, payment_method, amount, category):
    c.execute('''UPDATE receipts
                 SET vendor = ?, receipt_date = ?, total_amount_given = ?, change = ?, payment_method = ?, amount = ?, category = ?
                 WHERE id = ?''', (vendor, receipt_date, total_amount_given, change, payment_method, amount, category, receipt_id))
    conn.commit()

# Function to delete a receipt
def delete_receipt(receipt_id):
    c.execute('DELETE FROM receipts WHERE id = ?', (receipt_id,))
    conn.commit()

# Example usage
create_receipt('Supermarket', '2024-11-07', 100.0, 10.0, 'Cash', 90.0, 'Groceries')
create_receipt('Restaurant', '2024-11-06', 50.0, 0.0, 'Credit Card', 50.0, 'Dining')

print("All Receipts:")
for receipt in read_receipts():
    print(receipt)

update_receipt(1, 'Supermarket', '2024-11-07', 100.0, 10.0, 'Cash', 90.0, 'Groceries')
delete_receipt(2)

print("Receipts after update and delete:")
for receipt in read_receipts():
    print(receipt)

# Close the connection
conn.close()
"""
"""
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('receipts.db')
c = conn.cursor()

# Create tables for receipts and items
c.execute('''CREATE TABLE IF NOT EXISTS receipts (
                id TEXT PRIMARY KEY,
                vendor TEXT,
                receipt_date TEXT,
                total_amount_given REAL,
                change REAL,
                payment_method TEXT,
                amount REAL,
                category TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receipt_id TEXT,
                item_name TEXT,
                amount REAL,
                category TEXT,
                FOREIGN KEY (receipt_id) REFERENCES receipts(id)
            )''')

# Function to create a new receipt
def create_receipt(receipt_id, vendor, receipt_date, total_amount_given, change, payment_method, amount, category):
    c.execute('''INSERT INTO receipts (id, vendor, receipt_date, total_amount_given, change, payment_method, amount, category)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (receipt_id, vendor, receipt_date, total_amount_given, change, payment_method, amount, category))
    conn.commit()

# Function to create a new item
def create_item(receipt_id, item_name, amount, category):
    c.execute('''INSERT INTO items (receipt_id, item_name, amount, category)
                 VALUES (?, ?, ?, ?)''', (receipt_id, item_name, amount, category))
    conn.commit()

# Function to read all receipts
def read_receipts():
    c.execute('SELECT * FROM receipts')
    return c.fetchall()

# Function to read items for a given receipt
def read_items(receipt_id):
    c.execute('SELECT * FROM items WHERE receipt_id = ?', (receipt_id,))
    return c.fetchall()

# Function to update a receipt
def update_receipt(receipt_id, vendor, receipt_date, total_amount_given, change, payment_method, amount, category):
    c.execute('''UPDATE receipts
                 SET vendor = ?, receipt_date = ?, total_amount_given = ?, change = ?, payment_method = ?, amount = ?, category = ?
                 WHERE id = ?''', (vendor, receipt_date, total_amount_given, change, payment_method, amount, category, receipt_id))
    conn.commit()

# Function to delete a receipt and its associated items
def delete_receipt(receipt_id):
    # First, delete items associated with the receipt
    c.execute('DELETE FROM items WHERE receipt_id = ?', (receipt_id,))
    # Then, delete the receipt itself
    c.execute('DELETE FROM receipts WHERE id = ?', (receipt_id,))
    conn.commit()

# Close the connection
def close_connection():
    conn.close()

"""
import sqlite3
'''
# Connect to SQLite database
conn = sqlite3.connect('receipts.db')
c = conn.cursor()'''
conn = sqlite3.connect('receipts.db', check_same_thread=False)
c = conn.cursor()

# Create tables for receipts and items, with user_id linking receipts to users
c.execute('''CREATE TABLE IF NOT EXISTS receipts (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                vendor TEXT,
                receipt_date TEXT,
                total REAL,  -- Total value of the receipt (e.g., before payment)
                total_amount_given REAL,  -- Amount paid by the user
                change REAL,
                payment_method TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receipt_id TEXT,
                item_name TEXT,
                amount REAL,
                category TEXT,
                FOREIGN KEY (receipt_id) REFERENCES receipts(id)
            )''')
conn.commit()

# Function to create a new receipt for a specific user
def create_receipt(user_id, receipt_id, vendor, receipt_date, total, total_amount_given, change, payment_method):
    c.execute('''INSERT INTO receipts (id, user_id, vendor, receipt_date, total, total_amount_given, change, payment_method)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
              (receipt_id, user_id, vendor, receipt_date, total, total_amount_given, change, payment_method))
    conn.commit()

# Function to create a new item associated with a receipt
def create_item(receipt_id, item_name, amount, category):
    c.execute('''INSERT INTO items (receipt_id, item_name, amount, category)
                 VALUES (?, ?, ?, ?)''', (receipt_id, item_name, amount, category))
    conn.commit()

# Function to read all receipts for a specific user
def read_receipts(user_id):
    c.execute('SELECT * FROM receipts WHERE user_id = ?', (user_id,))
    rows = c.fetchall()

    # Return a list of dictionaries for easier JSON serialization
    receipts = []
    for row in rows:
        receipts.append({
            "id": row[0],
            "user_id": row[1],
            "vendor": row[2],
            "receipt_date": row[3],
            "total": row[4],
            "total_amount_given": row[5],
            "change": row[6],
            "payment_method": row[7]
        })
    return receipts

# Function to read items for a given receipt
def read_items(receipt_id):
    c.execute('SELECT * FROM items WHERE receipt_id = ?', (receipt_id,))
    rows = c.fetchall()

    # Return a list of dictionaries for easier JSON serialization
    items = []
    for row in rows:
        items.append({
            "id": row[0],
            "receipt_id": row[1],
            "item_name": row[2],
            "amount": row[3],
            "category": row[4]
        })
    return items
# Function to update a receipt
def update_receipt(receipt_id, vendor, receipt_date, total_amount_given, change, payment_method):
    c.execute('''UPDATE receipts
                 SET vendor = ?, receipt_date = ?, total_amount_given = ?, change = ?, payment_method = ?
                 WHERE id = ?''', (vendor, receipt_date, total_amount_given, change, payment_method, receipt_id))
    conn.commit()


# Function to delete a receipt and its associated items
def delete_receipt(receipt_id):
    # First, delete items associated with the receipt
    c.execute('DELETE FROM items WHERE receipt_id = ?', (receipt_id,))
    # Then, delete the receipt itself
    c.execute('DELETE FROM receipts WHERE id = ?', (receipt_id,))
    conn.commit()

# Function to close the connection
def close_connection():
    conn.close()

# Example usage
if __name__ == "__main__":
    # Assuming a signed-in user with user_id
    user_id = 1  # Replace with actual user_id after sign-in

    # Create a new receipt for this user
    create_receipt(user_id, 'receipt123', 'Supermarket', '2024-11-07', 100.0, 10.0, 'Cash', 90.0, 'Groceries')

    # Add items to this receipt
    create_item('receipt123', 'Apples', 3.0, 'Fruit')
    create_item('receipt123', 'Milk', 2.0, 'Dairy')

    # Read receipts for this user
    receipts = read_receipts(user_id)
    print(receipts)

    # Read items for a specific receipt
    items = read_items('receipt123')
    print(items)

    # Close the connection
    close_connection()


