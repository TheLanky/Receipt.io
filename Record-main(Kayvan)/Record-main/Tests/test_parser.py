

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
'''
import unittest
import uuid
from parser import parse_response

class TestParseResponse(unittest.TestCase):

    def test_parse_response_list_of_lists(self):
        response_text = """
        receipt = [
            "WALL-MART-SUPERSTORE",
            "10/17/2020",
            "16:12",
            "27.27",
            "0.00",
            "CREDIT"
        ]
        items = [
            ["HAND TOWEL", "2.97", "Groceries"],
            ["GATORADE", "2.00", "Groceries"],
            ["T-SHIRT", "16.88", "Clothing and Accessories"],
            ["PUSH PINS", "1.24", "Home and Furniture"]
        ]
        """
        expected_receipt = [
            str(uuid.UUID("ac018601-48e1-4f67-90c6-3c1bec084f0a")),  # Example UUID, use dynamic one if needed
            "WALL-MART-SUPERSTORE",
            "10/17/2020",
            "16:12",
            "27.27",
            "0.00",
            "CREDIT"
        ]
        expected_items = [
            {"Item name": "HAND TOWEL", "Amount": "2.97", "Category": "Groceries"},
            {"Item name": "GATORADE", "Amount": "2.00", "Category": "Groceries"},
            {"Item name": "T-SHIRT", "Amount": "16.88", "Category": "Clothing and Accessories"},
            {"Item name": "PUSH PINS", "Amount": "1.24", "Category": "Home and Furniture"}
        ]

        receipt, items = parse_response(response_text)

        # Check if the first element is a UUID instance
        receipt_uuid = uuid.UUID(receipt[0])  # If your function generates UUIDs dynamically, update this accordingly
        self.assertIsInstance(receipt_uuid, uuid.UUID, "First element of receipt should be a UUID")

        self.assertEqual(receipt[1:], expected_receipt[1:], f"Expected: {expected_receipt} but got: {receipt}")
        self.assertEqual(items, expected_items, f"Expected: {expected_items} but got: {items}")


    def test_parse_response_list_of_dicts(self):
        response_text = """
        receipt = [
            "WALL-MART-SUPERSTORE",
            "10/17/2020",
            "16:12",
            "27.27",
            "0.00",
            "CREDIT"
        ]
        items = [
            {"Item name": "HAND TOWEL", "Amount": "2.97", "Category": "Groceries"},
            {"Item name": "GATORADE", "Amount": "2.00", "Category": "Groceries"},
            {"Item name": "T-SHIRT", "Amount": "16.88", "Category": "Clothing and Accessories"},
            {"Item name": "PUSH PINS", "Amount": "1.24", "Category": "Home and Furniture"}
        ]
        """
        expected_receipt = [
            str(uuid.UUID("4ec7bafc-aa0a-4a41-bf32-f79e7fafb85b")),  # Example UUID, use dynamic one if needed
            "WALL-MART-SUPERSTORE",
            "10/17/2020",
            "16:12",
            "27.27",
            "0.00",
            "CREDIT"
        ]
        expected_items = [
            {"Item name": "HAND TOWEL", "Amount": "2.97", "Category": "Groceries"},
            {"Item name": "GATORADE", "Amount": "2.00", "Category": "Groceries"},
            {"Item name": "T-SHIRT", "Amount": "16.88", "Category": "Clothing and Accessories"},
            {"Item name": "PUSH PINS", "Amount": "1.24", "Category": "Home and Furniture"}
        ]

        receipt, items = parse_response(response_text)

        # Check if the first element is a UUID instance
        receipt_uuid = uuid.UUID(receipt[0])  # If your function generates UUIDs dynamically, update this accordingly
        self.assertIsInstance(receipt_uuid, uuid.UUID, "First element of receipt should be a UUID")

        self.assertEqual(receipt[1:], expected_receipt[1:], f"Expected: {expected_receipt} but got: {receipt}")
        self.assertEqual(items, expected_items, f"Expected: {expected_items} but got: {items}")
    def test_parse_response_malformed_receipt(self):
        response_text = """
        receipt = [
            "WALL-MART-SUPERSTORE",
            "10/17/2020",
            "INVALID DATA"
        ]
        items = [
            {"Item name": "ITEM1", "Amount": "2.00", "Category": "Category1"}
        ]
        """
        expected_receipt = [
            str(uuid.UUID("9a1fc82b-6b6c-4f09-9b7a-e9cf2457d3d2")),  # Example UUID, use dynamic one if needed
            "WALL-MART-SUPERSTORE",
            "10/17/2020",
            "INVALID DATA"
        ]
        expected_items = [
            {"Item name": "ITEM1", "Amount": "2.00", "Category": "Category1"}
        ]

        receipt, items = parse_response(response_text)

        # Check if the first element is a UUID instance
        receipt_uuid = uuid.UUID(receipt[0])  # If your function generates UUIDs dynamically, update this accordingly
        self.assertIsInstance(receipt_uuid, uuid.UUID, "First element of receipt should be a UUID")

        self.assertEqual(receipt[1:], expected_receipt[1:], f"Expected: {expected_receipt} but got: {receipt}")
        self.assertEqual(items, expected_items, f"Expected: {expected_items} but got: {items}")