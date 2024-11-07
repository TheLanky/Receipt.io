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


