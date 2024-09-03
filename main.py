# Import necessary modules
from image_acquisition import capture_image
from image_preprocessing import preprocess_image
from text_extraction import extract_text
from object_classification import classify_image
from quality_check import quality_check
from data_logging import log_results

def main():
    # Step 1: Capture Image
    image_path = capture_image()

    # Step 2: Preprocess the Image
    processed_image = preprocess_image(image_path)

    # Step 3: Extract Text (OCR)
    extracted_text = extract_text(image_path)
    print("Extracted Text:", extracted_text)

    # Step 4: Classify Object
    classification_result = classify_image(image_path)
    print("Classification Result:", classification_result)

    # Step 5: Quality Check
    decision = quality_check(classification_result)
    print("Quality Control Decision:", decision)

    # Step 6: Log Results
    log_results(image_path, decision)

if __name__ == "__main__":
    main()
