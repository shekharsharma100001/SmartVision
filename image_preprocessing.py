import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Normalize the image
    normalized = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(normalized, (5, 5), 0)

    # Apply edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Segmentation using thresholding
    _, segmented = cv2.threshold(edges, 128, 255, cv2.THRESH_BINARY)

    return segmented
