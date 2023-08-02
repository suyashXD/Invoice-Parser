import os
import sys
import unittest

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Now, you should be able to import the invoice_parser module
from app.InvoiceParser.invoice_parser import parse_invoice

class TestInvoiceParser(unittest.TestCase):
    def test_parse_invoice(self):
        # Test case 1: Test with a valid image file
        image_path = os.path.join(project_root, "data", "sample_invoices", "invoice.jpg")
        invoice_info = parse_invoice(image_path)

        # Ensure that invoice_info is not None, indicating successful parsing
        self.assertIsNotNone(invoice_info)

        # Test case 2: Test with an invalid image file (non-existent file)
        invalid_image_path = "invalid_image.jpg"
        invoice_info = parse_invoice(invalid_image_path)

        # Ensure that invoice_info is None, indicating failed parsing
        self.assertIsNone(invoice_info)

        # Test case 3: Test with an image containing known entities
        # Create a sample image with known entities and save it
        # Then pass the image path to the parse_invoice function and check for correct extraction

        # ...

        # Add more test cases to thoroughly test the invoice_parser functionality

if __name__ == '__main__':
    unittest.main()
