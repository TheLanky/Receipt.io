from ocr_service import extract_text
from categorization_service import categorize_receipt
from parser import parse_response
from Receipt_App_CRUD import create_receipt, create_item, read_receipts, read_items, close_connection
import uuid
# Step 1: Extract text from an image file
#image_path = r'D:/Users/k1nik/Downloads/standard-grocery-receipt-template.png'
image_path =r'D:\Users\k1nik\Downloads\Tesco.png'
receipt_text = extract_text(image_path)

# Step 2: Categorize the extracted receipt text
response_text = categorize_receipt(receipt_text)

# Step 3: Parse the categorized response into structured data
receipt, items = parse_response(response_text)

# Output the parsed data
print("Parsed Receipt:", receipt)
print("Parsed Items:", items)
if receipt:
    receipt_id = receipt[0]  # The first element is the UUID
    vendor = receipt[1] if len(receipt) > 1 else None
    receipt_date = receipt[2] if len(receipt) > 2 else None
    total_amount_given = receipt[3] if len(receipt) > 3 else None
    change = receipt[4] if len(receipt) > 4 else None
    payment_method = receipt[5] if len(receipt) > 5 else None
    amount = receipt[6] if len(receipt) > 6 else None
    category = receipt[7] if len(receipt) > 7 else None

    # Step 5: Call the CRUD function to insert the receipt data into the database
    create_receipt(receipt_id, vendor, receipt_date, total_amount_given, change, payment_method, amount, category)
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
print("All Receipts:")
for receipt in read_receipts():
    print(receipt)

    # Read and print all items for this receipt
    print("Items for this receipt:")
    for item in read_items(receipt[0]):
        print(item)

# Close the connection when done
close_connection()