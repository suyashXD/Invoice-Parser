import cv2
import os
import pytesseract
from PIL import Image
import numpy as np
import logging

# OCR/ocr_engine.py
try:
    import pytesseract
except ImportError:
    raise ImportError("pytesseract is not installed. You can install it using 'pip install pytesseract'.")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("ocr_engine.log"),
    ]
)

class ImageProcessingError(Exception):
    def __init__(self, message):
        super().__init__(f"Error during image preprocessing: {message}")

class OCRProcessingError(Exception):
    def __init__(self, message):
        super().__init__(f"Error during OCR: {message}")

def preprocess_image(image, resize_width=1200, resize_height=900, denoising_strength=10, threshold_type=cv2.THRESH_BINARY | cv2.THRESH_OTSU):
    try:
        # (Existing preprocessing code remains the same)
        image_rgb = image.convert("RGB")

        # Convert the image to a NumPy array
        image_np = np.array(image_rgb)

        # Resize the image
        resized_image = cv2.resize(image_np, (resize_width, resize_height))

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # Apply denoising
        denoised_image = cv2.fastNlMeansDenoising(gray_image, None, denoising_strength, 5, 21)

        # Apply adaptive thresholding
        _, binary_image = cv2.threshold(denoised_image, 0, 255, threshold_type)

        return binary_image
    except Exception as e:
        # Log the error along with the stack trace
        logging.exception(f"Error during image preprocessing: {e}")
        raise ImageProcessingError(str(e))

def perform_ocr(image, language='eng', ocr_config='--psm 6'):
    try:
        # Preprocess the image
        preprocessed_image = preprocess_image(image)

        if preprocessed_image is not None:
            # Perform OCR using pytesseract on the preprocessed image with specific language and configuration
            extracted_text = pytesseract.image_to_string(preprocessed_image, lang=language, config=ocr_config)

            # Log successful OCR processing
            logging.info("OCR processing successful.")

            return extracted_text.strip()
        else:
            logging.error("Image preprocessing failed.")
            return None
    except Exception as e:
        # Log the error along with the stack trace
        logging.exception(f"Error during OCR: {e}")
        raise OCRProcessingError(str(e))
