import pytesseract
import os
from reportlab.pdfgen import canvas
import cv2 

# Define paths for the input image and output PDF
folder_name = "test_image"
image_name = "1.jpg"
current_directory = os.getcwd()
image_path = os.path.join(current_directory, folder_name, image_name)
output_pdf = "example.pdf"


# Function to extract text from image and get bounding boxes
def extract_text_from_image(image_path):
    # Extract text with bounding boxes
    pdf = pytesseract.image_to_pdf_or_hocr(image_path)
    with open('/home/mio/Documents/code/image_to_pdf/example.pdf', 'w+b') as f:
        f = open("demofile.pdf", "w+b")
        f.write(pdf)

extract_text_from_image(image_path)