# Smart Vision Quality Testing System

This project implements a smart vision-based quality testing system for an e-commerce company. It utilizes camera vision technology, OCR, and machine learning to assess the quality and quantity of products. The system is designed to be modular, with each component focusing on a specific part of the process.

## Project Structure

The project is divided into several Python scripts, each handling a specific task in the system:

- **image_acquisition.py**: Captures images from the camera.
- **image_preprocessing.py**: Preprocesses the captured images, including normalization, filtering, and segmentation.
- **text_extraction.py**: Extracts text from images using OCR (Optical Character Recognition).
- **object_classification.py**: Classifies objects in images using a pre-trained machine learning model.
- **custom_model.py**: Provides a template for creating and training a custom machine learning model.
- **quality_check.py**: Implements quality control logic based on the classification results.
- **data_logging.py**: Logs the results of the quality check into a CSV file.
- **main.py**: The main script that integrates all the components and runs the quality testing system.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-vision-quality-testing.git
   cd smart-vision-quality-testing
2. Install the required dependencies:
   ```bash
   pip install opencv-python-headless tensorflow keras numpy pytesseract

## How to Run

1. Ensure all files are saved in the same directory:
2. Run the main.py file using:
   ```bash
   python main.py


