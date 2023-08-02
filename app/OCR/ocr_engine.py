import cv2
import os
import pytesseract
from PIL import Image
import numpy as np

# OCR/ocr_engine.py
try:
    import pytesseract
except ImportError:
    raise ImportError("pytesseract is not installed. You can install it using 'pip install pytesseract'.")

def preprocess_image(image):
    """
    Perform preprocessing on the given image.

    Args:
        image (PIL.Image.Image): The input image (PIL/Pillow Image object).

    Returns:
        np.array: The preprocessed image as a NumPy array.
    """
    try:
        # Convert the image to RGB format (3-channel)
        image_rgb = image.convert("RGB")

        # Convert the image to a NumPy array
        image_np = np.array(image_rgb)

        # Resize the image (optional)
        resized_image = cv2.resize(image_np, (1200, 900))

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # Apply denoising
        denoised_image = cv2.fastNlMeansDenoising(gray_image, None, 10, 5, 21)

        # Apply adaptive thresholding
        _, binary_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        return binary_image
    except Exception as e:
        print(f"Error during image preprocessing: {e}")
        return None

def perform_ocr(image):
    """
    Perform Optical Character Recognition (OCR) on the given image to extract text.

    Args:
        image (PIL.Image.Image): The input image (PIL/Pillow Image object).

    Returns:
        str: The extracted text from the image.
    """
    try:
        # Preprocess the image
        preprocessed_image = preprocess_image(image)

        if preprocessed_image is not None:
            # Perform OCR using pytesseract on the preprocessed image with specific language and configuration
            extracted_text = pytesseract.image_to_string(preprocessed_image, lang='eng', config='--psm 6')

            return extracted_text.strip()
        else:
            print("Image preprocessing failed.")
            return None
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None
