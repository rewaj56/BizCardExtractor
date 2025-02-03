import cv2
import easyocr
import os

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Error: Could not load image at {image_path}")
    
    img_resized = cv2.resize(img, (1200, 900))
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    img_contrast = cv2.convertScaleAbs(img_gray, alpha=1.5, beta=0)
    _, img_thresh = cv2.threshold(img_contrast, 150, 255, cv2.THRESH_BINARY)
    
    output_image_path = "post_processed_image.jpg"
    cv2.imwrite(output_image_path, img_thresh)
    print(f"Post-processed image saved as {output_image_path}")
    
    return img_thresh

def extract_text(image_path, languages=['en']):
    reader = easyocr.Reader(languages, gpu=False)
    preprocessed_img = preprocess_image(image_path)
    
    result = reader.readtext(preprocessed_img, detail=0)
    extracted_text = "\n".join(result)
    
    return extracted_text

def main():
    image_path = os.path.join("images", "tmc.jpeg")
    try:
        extracted_text = extract_text(image_path)
        print("Extracted Text:", extracted_text)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()