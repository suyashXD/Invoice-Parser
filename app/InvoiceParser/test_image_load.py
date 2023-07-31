from PIL import Image

# Replace 'invoice.jpg' with the full absolute file path of the image
# Replace 'invoice.jpg' with the full absolute file path of the image
image_path = r"C:\Users\zucck\OneDrive\Desktop\InvoiceParser\data\sample_invoices\invoice.jpg"


try:
    image = Image.open(image_path)
    image.show()
except Exception as e:
    print(f"Error while loading image: {e}")
