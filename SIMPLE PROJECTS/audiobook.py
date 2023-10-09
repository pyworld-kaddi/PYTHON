import pyttsx3
from PyPDF2 import PdfReader

# Specify the PDF file path
file_path = r'C:\Users\Prasad\Desktop\SARAVANAN\a.pdf'

# Open the PDF file in binary mode
with open(file_path, 'rb') as book:
    pdf_reader = PdfReader(book)
    pages = len(pdf_reader.pages)

    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()

    # Read and speak the text from pages 7 onwards
    for num in range(0,pages):  # Changed range to start from 7th page
        page = pdf_reader.pages[num]
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

    # Close the PDF file
    book.close()
