# import cv2
# import pytesseract
# import spacy
# import json

# # Load spaCy NER model
# nlp = spacy.load("en_core_web_sm")

# def extract_text_from_image(image_path):
#     # Load the image using OpenCV
#     image = cv2.imread(image_path)

#     # Perform OCR using Tesseract
#     extracted_text = pytesseract.image_to_string(image)

#     return extracted_text

# def extract_invoice_information(text):
#     # Process the text using spaCy NER
#     doc = nlp(text)

#     # Initialize variables to store the extracted information
#     invoice_date = None
#     seller_name = None
#     buyer_name = None
#     address = None
#     due_date = None

#     # Iterate through the entities recognized by spaCy
#     for ent in doc.ents:
#         if "date" in ent.label_.lower() and not invoice_date:
#             invoice_date = ent.text
#         elif "person" in ent.label_.lower() and not seller_name:
#             seller_name = ent.text
#         elif "person" in ent.label_.lower() and not buyer_name:
#             buyer_name = ent.text
#         elif "address" in ent.label_.lower() and not address:
#             address = ent.text
#         elif "date" in ent.label_.lower() and not due_date:
#             due_date = ent.text

#     # Create a dictionary with the extracted information
#     invoice_info = {
#         "invoice_date": invoice_date,
#         "seller_name": seller_name,
#         "buyer_name": buyer_name,
#         "address": address,
#         "due_date": due_date
#     }

#     return invoice_info

# if __name__ == "__main__":
#     # Replace 'invoice.jpg' with the path to your invoice image
#     image_path = "invoice.jpg"

#     # Step 1: Extract text from the invoice image
#     extracted_text = extract_text_from_image(image_path)

#     # Step 2: Extract invoice information using NER
#     invoice_info = extract_invoice_information(extracted_text)

#     # Step 3: Output JSON file
#     with open("invoice_info.json", "w") as json_file:
#         json.dump(invoice_info, json_file, indent=4)

#     print("Invoice information extracted and saved to 'invoice_info.json'.")

# import pytesseract
# import spacy

# Test Tesseract OCR
# try:
#     pytesseract.get_tesseract_version()
#     print("Tesseract OCR is installed and working.")
# except Exception as e:
#     print("Tesseract OCR is not installed or not working.")
#     print("Error:", e)

# # Test spaCy
# try:
#     nlp = spacy.load("en_core_web_sm")
#     print("spaCy is installed and working.")
# except Exception as e:
#     print("spaCy is not installed or not working.")
#     print("Error:", e)

# import cv2
# import pytesseract

# # Load the image using OpenCV
# image = cv2.imread("invoice.jpg")

# # Perform OCR using Tesseract
# extracted_text = pytesseract.image_to_string(image)

# # Print the extracted text
# print("Extracted Text:")
# print(extracted_text)

# import spacy

# # Load spaCy NER model
# nlp = spacy.load("en_core_web_sm")

# # Sample text for testing NER (replace this with extracted text from your invoice)
# sample_text = "This is a sample text containing invoice date, seller name, buyer name, addresses, and due date."

# # Process the text using spaCy NER
# doc = nlp(sample_text)

# # Check if entities are recognized
# if not doc.ents:
#     print("No named entities recognized in the text.")
# else:
#     # Iterate through the entities recognized by spaCy
#     for ent in doc.ents:
#         print(ent.text, ent.label_)

import cv2
import pytesseract
import spacy
import json

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

# Load the image using OpenCV
image = cv2.imread("invoice.jpg")

# Perform OCR using Tesseract
extracted_text = pytesseract.image_to_string(image)

# Process the text using spaCy NER
doc = nlp(extracted_text)

# Initialize variables to store the extracted information
invoice_date = None
seller_name = None
buyer_name = None
address = None
due_date = None

# Iterate through the entities recognized by spaCy
for ent in doc.ents:
    if "date" in ent.label_.lower() and not invoice_date:
        invoice_date = ent.text
    elif "person" in ent.label_.lower() and not seller_name:
        seller_name = ent.text
    elif "person" in ent.label_.lower() and not buyer_name:
        buyer_name = ent.text
    elif "address" in ent.label_.lower() and not address:
        address = ent.text
    elif "date" in ent.label_.lower() and not due_date:
        due_date = ent.text

# Create a dictionary with the extracted information
invoice_info = {
    "invoice_date": invoice_date,
    "seller_name": seller_name,
    "buyer_name": buyer_name,
    "address": address,
    "due_date": due_date
}

# Print the extracted information
print("Invoice Information:")
print(invoice_info)


import cv2
import pytesseract
import spacy
import re

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

# Load the image using OpenCV
image = cv2.imread("invoice.jpg")

# Preprocess the image (you can experiment with different preprocessing techniques)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Perform OCR using Tesseract
extracted_text = pytesseract.image_to_string(threshold_image)

# Text cleaning to remove unnecessary characters and noise
cleaned_text = re.sub(r'[^a-zA-Z0-9\s\.,\-\n]', '', extracted_text)

# Process the cleaned text using spaCy NER
doc = nlp(cleaned_text)

# Initialize a dictionary to store the extracted information
invoice_info = {}

# Iterate through the entities recognized by spaCy
for ent in doc.ents:
    # Convert entity label to lowercase and use it as the key
    key = ent.label_.lower()
    # Use the entity text as the value
    value = ent.text
    # Add the key-value pair to the invoice_info dictionary
    invoice_info[key] = value

# Save the extracted information as a JSON file
with open("invoice_info.json", "w") as json_file:
    json.dump(invoice_info, json_file, indent=4)

print("Invoice information extracted and saved to 'invoice_info.json'.")

