import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"]

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def categorize_receipt(receipt_text):
    prompt = f"""extract the following information: Vendor, ReceiptDate, Total Amount Given, Change, payment method if available from the following receipt then output it as a list in python named receipt and make output another python list in python for receipt items named items with columns Item name, Amount, Category which category can be one of these options: "Groceries", "Dining", "Utilities", "Transportation", "Healthcare", "Personal Care", "Clothing and Accessories", "Entertainment", "Home and Furniture", "Education", "Travel", "Gifts and Donations", "Business Expenses", "Insurance", "Taxes", "Investments", "Miscellaneous" {receipt_text}
    """
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    return response.text
