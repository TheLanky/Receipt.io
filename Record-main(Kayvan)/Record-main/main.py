from ocr_service import extract_text
from categorization_service import categorize_receipt
from parser import parse_response
from Receipt_App_CRUD import create_receipt, create_item, read_receipts, read_items, close_connection
from auth import sign_in, sign_up
import uuid
import re
# Ask the user whether to sign up or sign in
choice = input("Do you want to (1) Sign In or (2) Sign Up? Enter 1 or 2: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
phone = None

if choice == '2':  # If the user chooses to sign up
    phone = input("Enter your phone number for new accounts only: ")
    if sign_up(email, password, phone):
        print(f"User {email} registered successfully!")
    else:
        print("Sign-up failed. Exiting the program.")
        exit()

# Attempt to sign in
user_id = sign_in(email, password)
if user_id:
    print(f"User {email} signed in successfully.")
else:
    print("Invalid email or password. Exiting the program.")
    exit()

# Step 1: Extract text from an image file
#image_path = r'D:/Users/k1nik/Downloads/standard-grocery-receipt-template.png'
image_path = r'D:\Users\k1nik\Downloads\Tesco.png'
receipt_text = extract_text(image_path)
print("Receipt Text:\n", receipt_text)

# Step 2: Categorize the extracted receipt text
response_text = categorize_receipt(receipt_text)
print("Items Text:\n", response_text)

# Step 3: Parse the categorized response into structured data
receipt, items = parse_response(response_text)

# Output the parsed data
print("Parsed Receipt:", receipt)
print("Parsed Items:", items)
def clean_currency(value):
    # Remove any non-numeric characters except the decimal point
    cleaned_value = re.sub(r'[^\d.]+', '', value)
    # Convert the cleaned value to a float
    return float(cleaned_value) if cleaned_value else None
# Check and insert the receipt if data is parsed successfully
if receipt:
    # Generate unique receipt ID
    receipt_id = str(uuid.uuid4())
    vendor = receipt[1] if len(receipt) > 1 else None
    receipt_date = receipt[2] if len(receipt) > 2 else None

    # Remove non-numeric characters and convert to float
    total = clean_currency(receipt[3]) if len(receipt) > 3 else None
    total_amount_given = clean_currency(receipt[4]) if len(receipt) > 4 else None
    change = clean_currency(receipt[5]) if len(receipt) > 5 else None

    payment_method = receipt[6] if len(receipt) > 6 else None

    # Insert the receipt data into the database with user_id
    create_receipt(user_id, receipt_id, vendor, receipt_date, total, total_amount_given, change, payment_method)
    print(f"Receipt with ID {receipt_id} has been added to the database.")

    # Step 6: Insert items associated with this receipt
    if items:
        for item in items:
            item_name = item.get("Item name")
            item_amount = item.get("Amount")
            item_category = item.get("Category", "Uncategorized")  # Default to "Uncategorized" if no category is present
            create_item(receipt_id, item_name, item_amount, item_category)
            print(f"Item '{item_name}' has been added to the database under receipt ID {receipt_id}.")

# Optional: You can read all receipts and items to check the data in the database
'''
print("All Receipts:")
for receipt in read_receipts(user_id):
    print(receipt)

    # Read and print all items for this receipt
    print("Items for this receipt:")
    for item in read_items(receipt[0]):
        print(item)'''

# Close the connection when done
close_connection()
