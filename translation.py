import PyPDF2
from googletrans import Translator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def translate_text(text, dest_language="en"):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def create_pdf_with_text(text, num_pages, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    text_object = c.beginText(40, 750)
    text_object.setFont("Helvetica", 12)
    
    for line in text.split('\n'):
        text_object.textLine(line)
    
    for _ in range(num_pages):
        c.drawText(text_object)
        c.showPage()
    
    c.save()

# Path to your PDF file
pdf_path = "/home/mio/Documents/code/image_to_pdf/demofile.pdf"
output_pdf_path = "/home/mio/Documents/code/image_to_pdf/trans_demofile4.pdf"

# Extract text from PDF
extracted_text = extract_text_from_pdf(pdf_path)
print("Extracted Text:\n", extracted_text)

# Translate text to the desired language (e.g., French)
translated_text = translate_text(extracted_text, dest_language="fr")
print("Translated Text:\n", translated_text)

# Create a new PDF with the translated text
num_pages = len(PyPDF2.PdfReader(open(pdf_path, 'rb')).pages)
create_pdf_with_text(translated_text, num_pages, output_pdf_path)
print(f"Translated PDF saved as {output_pdf_path}")
