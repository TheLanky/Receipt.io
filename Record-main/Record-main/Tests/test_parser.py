import unittest
from parser import parse_response
'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
'''
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

        self.assertEqual(receipt, expected_receipt, f"Expected: {expected_receipt} but got: {receipt}")
        self.assertEqual(items, expected_items, f"Expected: {expected_items} but got: {items}")

    def test_parse_response_list_of_dicts(self):
        response_text = '''
        receipt = [
            "STORE", "01/01/2021", "30.00", "0.00", "CARD"
        ]
        items = [
            {"Item name": "ITEM1", "Amount": "2.00", "Category": "Category1"},
            {"Item name": "ITEM2", "Amount": "3.00", "Category": "Category2"}
        ]
        '''
        receipt, items = parse_response(response_text)
        self.assertEqual(receipt, ["STORE", "01/01/2021", "30.00", "0.00", "CARD"])
        self.assertEqual(items, [{"Item name": "ITEM1", "Amount": "2.00", "Category": "Category1"}, {"Item name": "ITEM2", "Amount": "3.00", "Category": "Category2"}])
    def test_missing_receipt_section(self):
        response_text = """
        items = [
            ["HAND TOWEL", "2.97", "Groceries"],
            ["GATORADE", "2.00", "Groceries"]
        ]
        """
        receipt, items = parse_response(response_text)
        self.assertEqual((receipt, items), (None, None), "Expected None when 'receipt' section is missing")


    def test_incorrect_receipt_format(self):
        response_text = """
        receipt = "WALL-MART-SUPERSTORE", "10/17/2020", "27.27", "0.00", "CREDIT"  # Missing square brackets
        items = [
            ["HAND TOWEL", "2.97", "Groceries"],
            ["GATORADE", "2.00", "Groceries"]
        ]
        """
        receipt, items = parse_response(response_text)
        self.assertEqual((receipt, items), (None, None), "Expected None for incorrectly formatted receipt")
