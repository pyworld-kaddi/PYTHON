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

    # Set voice properties (change voice, rate, or volume as needed)
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"  # Example voice ID, change it to match the desired voice on your system
    speaker.setProperty('voice', voice_id)
    speaker.setProperty('rate', 150)  # You can adjust the speaking rate (words per minute)
    speaker.setProperty('volume', 1.0)  # You can adjust the volume (0.0 to 1.0)

    # Read and speak the text from all pages
    for num in range(0, pages):
        page = pdf_reader.pages[num]
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

    # Close the PDF file
    book.close()
