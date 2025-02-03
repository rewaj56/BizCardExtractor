import pytesseract
import cv2
import os

# Set Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_image(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not load image. Check the file path.")
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def preprocess_image(img):
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    thresholded = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]

    return thresholded

def extract_text_from_image(img):
    text = pytesseract.image_to_string(img)
    return text

def display_image(img):
    resized_img = cv2.resize(img, (800, 650))
    cv2.imshow("Business Card", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace with your image path
    image_path = os.path.join("images", "tmc.jpeg")
    img = read_image(image_path)
    
    if img is not None:
        preprocessed_img = preprocess_image(img)
        display_image(preprocessed_img)
        
        custom_config = r'--oem 3 --psm 6'
        extracted_text = pytesseract.image_to_string(preprocessed_img, config=custom_config)

        print("\nExtracted Text:\n", extracted_text)