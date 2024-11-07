import re
import ast
import uuid

def parse_response(response_text):
    # Clean up text by removing comments (anything following '#')
    clean_text = re.sub(r'#.*', '', response_text)

    # Check for presence of required lists in the response
    if "receipt = [" not in clean_text or "items = [" not in clean_text:
        raise ValueError("Error: 'receipt' or 'items' list not found in response.")

    # Extract 'receipt' list
    receipt_start = clean_text.find("receipt = [")
    receipt_end = clean_text.find("]", receipt_start) + 1
    receipt_text = clean_text[receipt_start:receipt_end].strip()

    # Remove the 'receipt =' part of the extracted text
    if receipt_text.startswith("receipt ="):
        receipt_text = receipt_text[len("receipt ="):].strip()

    # Extract 'items' list
    items_start = clean_text.find("items = [")
    items_end = clean_text.rfind("]") + 1  # Change to rfind to capture the last closing bracket
    items_text = clean_text[items_start:items_end].strip()

    # Remove the 'items =' part of the extracted text
    if items_text.startswith("items ="):
        items_text = items_text[len("items ="):].strip()

    # Print extracted text for debugging
    print("Receipt Text:\n", receipt_text)
    print("Items Text:\n", items_text)

    # Parse the receipt and items safely
    try:
        receipt = ast.literal_eval(receipt_text)
        # Insert a unique ID at the start of the receipt list
        receipt.insert(0, str(uuid.uuid4()))  # Add ID as a string
    except Exception as e:
        print(f"Error parsing receipt: {e}")
        return None, None

    try:
        items = ast.literal_eval(items_text)
    except Exception as e:
        print(f"Error parsing items: {e}")
        return receipt, None

    # Standardize 'items' structure
    if isinstance(items, list) and items and isinstance(items[0], list):
        # Convert list of lists to list of dictionaries
        items = [{"Item name": item[0], "Amount": item[1], "Category": item[2] if len(item) > 2 else "Uncategorized"} for item in items]
    elif isinstance(items, list) and items and isinstance(items[0], dict):
        print("Items are already in dictionary format.")
    else:
        print("Error: 'items' format is unsupported or empty.")
        return receipt, None

    return receipt, items
