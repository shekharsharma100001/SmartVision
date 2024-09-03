import cv2

def capture_image():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    image_path = "captured_image.jpg"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Display the captured frame
        cv2.imshow("Image", frame)

        # Capture image on pressing 'c'
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite(image_path, frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    return image_path
