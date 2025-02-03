import pytesseract

# Set Tesseract Path (Modify this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Check Tesseract Version
try:
    print("Tesseract Version:", pytesseract.get_tesseract_version())
except Exception as e:
    print("Error:", e)