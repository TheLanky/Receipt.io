import os
from google.cloud import vision

# Set the path to your service account key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'd:/Users/k1nik/Documents/Vic Uni/NEF3001(project1)/recieptscannernit-133cb4c4df2e.json'

def extract_text(image_file):
    """Extracts all text from the image as a string.

    Args:
        image_file: path to the image file.

    Returns:
        A string containing all the extracted text.
    """
    client = vision.ImageAnnotatorClient()

    with open(image_file, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    # Extract the text from the full_text_annotation
    extracted_text = document.text

    return extracted_text
