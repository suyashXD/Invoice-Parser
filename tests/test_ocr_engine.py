import os
import sys
import unittest
from PIL import Image

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Now, you should be able to import the OCR module
from app.OCR.ocr_engine import perform_ocr

class TestOCREngine(unittest.TestCase):
    def test_perform_ocr(self):
        # Load a sample image with known text content
        image_path = os.path.join(project_root, "data", "sample_invoices", "invoice.jpg")
        image = Image.open(image_path)

        # Perform OCR on the sample image
        extracted_text = perform_ocr(image)

        # Define the expected text content of the image
        expected_text = "Sample text from the image"

        # Compare the extracted text with the expected text
        self.assertEqual(extracted_text, expected_text)

if __name__ == '__main__':
    unittest.main()
