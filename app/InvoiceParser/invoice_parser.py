import os
from PIL import Image
import numpy as np
import sys
import re

# Add the project root directory to sys.path (optional if not using as a package)


# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

# Now, you should be able to import modules from the project


from app.OCR.ocr_engine import perform_ocr
from app.NER.ner_engine import perform_ner

from app.utils.date_parser import extract_dates_from_text



# ... (Rest of the code remains the same)

def load_image(image_path):
    """
    Load an image using PIL/Pillow.

    Args:
        image_path (str): Path to the image.

    Returns:
        PIL.Image.Image: PIL/Pillow Image object.
    """
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print(f"Error while loading image: {e}")
        return None

def clean_extracted_text(text):
    """
    Clean the extracted text using regular expressions to remove noise.

    Args:
        text (str): The extracted text from OCR.

    Returns:
        str: Cleaned text.
    """
    # Remove special characters and extra whitespaces
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Remove multiple whitespaces and newlines
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    return cleaned_text.strip()

def parse_invoice(image_path):
    # Load the image using PIL/Pillow
    image_np = load_image(image_path)

    if image_np is not None:
        # Perform OCR on the invoice image to extract text
        extracted_text = perform_ocr(image_np)

        if extracted_text:
            print("Extracted Text:")
            print(extracted_text)

            # Clean the extracted text
            cleaned_text = clean_extracted_text(extracted_text)

            if cleaned_text:
                print("Cleaned Text:")
                print(cleaned_text)

                # Perform NER on the cleaned text to identify entities
                entities = perform_ner(cleaned_text)

                # Extract dates from the cleaned text
                dates = extract_dates_from_text(cleaned_text)

                # Create a dictionary to store the extracted information
                invoice_info = {
                    "text": cleaned_text,
                    "entities": entities,
                    "dates": dates
                }

                return invoice_info
            else:
                print("Error during OCR: No text extracted.")
                return None
        else:
            print("Error during OCR: No text extracted.")
            return None
    else:
        print("Invoice parsing failed. Check if the image file can be loaded.")
        return None

if __name__ == "__main__":
    # Replace 'invoice.jpg' with the path to your actual invoice image
    invoice_image_path = r"C:\Users\zucck\OneDrive\Desktop\InvoiceParserMain\data\sample_invoices\invoice.jpg"

    # Call the parse_invoice function to extract information from the invoice image
    invoice_info = parse_invoice(invoice_image_path)

    if invoice_info:
        print("Extracted Invoice Information:")
        print(invoice_info)
