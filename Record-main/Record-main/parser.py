'''
def parse_response(response_text):
    print(response_text)
    receipt_start = response_text.find("receipt = [")
    receipt_end = response_text.find("]", receipt_start) + 1
    receipt_text = response_text[receipt_start:receipt_end]

    items_start = response_text.find("items = [")
    items_end = response_text.find("]", items_start) + 1
    items_text = response_text[items_start:items_end]

    # Use a dictionary to store variables created by exec
    local_vars = {}
    exec(receipt_text, {}, local_vars)
    exec(items_text, {}, local_vars)

    # Retrieve receipt and items from local_vars
    receipt = local_vars.get('receipt')
    items = local_vars.get('items')

    return receipt, items
'''
'''
def parse_response(response_text):
    print(response_text)

    # Extract 'receipt' list
    receipt_start = response_text.find("receipt = [")
    if receipt_start == -1:
        print("Error: 'receipt' list not found in response.")
        return None, None

    # Extract just the 'receipt' list part
    receipt_end = response_text.find("]", receipt_start) + 1
    receipt_text = response_text[receipt_start:receipt_end].strip()

    # Extract 'items' list
    items_start = response_text.find("items = [")
    if items_start == -1:
        print("Error: 'items' list not found in response.")
        return None, None

    # Extract just the 'items' list part
    items_end = response_text.find("]", items_start) + 1
    items_text = response_text[items_start:items_end].strip()

    # Use a dictionary to store variables created by exec
    local_vars = {}
    try:
        exec(receipt_text, {}, local_vars)
        exec(items_text, {}, local_vars)
    except SyntaxError as e:
        print("Syntax Error in executing extracted text:", e)
        return None, None

    # Retrieve receipt and items from local_vars
    receipt = local_vars.get('receipt')
    items = local_vars.get('items')

    # Standardize 'items' structure
    if isinstance(items, list) and items and isinstance(items[0], list):
        # Convert list of lists to list of dictionaries
        items = [{"Item name": item[0], "Amount": item[1], "Category": item[2] if len(item) > 2 else "Uncategorized"} for item in items]
    elif isinstance(items, list) and items and isinstance(items[0], dict):
        # Already in the desired format, so no conversion needed
        print("Items are already in dictionary format.")
    else:
        print("Error: 'items' format is unsupported or empty.")
        return receipt, None

    return receipt, items

'''
import re
import ast

def parse_response(response_text):

    # Clean up text by removing comments (anything following '#')
    clean_text = re.sub(r'#.*', '', response_text)

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

    # Ensure that the text now only contains the list content
    print("Receipt Text:\n", receipt_text)
    print("Items Text:\n", items_text)

    # Parse the receipt and items safely
    try:
        receipt = ast.literal_eval(receipt_text)
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
