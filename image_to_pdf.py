import os
import easyocr
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
# Get the current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

# Define paths for the input image and output PDF
folder_name = "test_image"
image_name = "1.jpg"
image_path = os.path.join(current_directory, folder_name, image_name)
output_pdf = "example.pdf"
image = Image.open(image_path)
# Create a PDF document and set the font
pdf_canvas = canvas.Canvas(output_pdf, pagesize=image.size)
pdf_canvas.setFont("Courier", 15)
page_width , page_height = image.size
# Function to draw text on the PDF at specified coordinates
def draw_text_on_pdf(text, bbox):
    # Adjust the y-coordinate since PDF origin (0,0) is at the bottom-left
    x = bbox[0][0]
    y = page_height - bbox[0][1] - 10
    pdf_canvas.drawString(x, y, text)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Perform OCR on the image
ocr_results = reader.readtext(image_path)

# Process the OCR results and draw text on the PDF
for (bbox, text, prob) in ocr_results:
    print(f'Text: {text}, BBox: {bbox}')
    # Draw the text using the bounding box coordinates
    draw_text_on_pdf(text, bbox)

# Save the PDF document
pdf_canvas.save()
print(f"PDF saved as {output_pdf}")
