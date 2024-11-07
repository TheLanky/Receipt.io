from ocr_service import extract_text
from categorization_service import categorize_receipt
from parser import parse_response

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
