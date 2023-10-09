import pyttsx3
from PyPDF2 import PdfReader
from pydub import AudioSegment

# Specify the PDF file path
file_path = r'C:\Users\Prasad\Desktop\SARAVANAN\a.pdf'

# Open the PDF file in binary mode
with open(file_path, 'rb') as book:
    pdf_reader = PdfReader(book)
    pages = len(pdf_reader.pages)

    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()

    # Change the voice (optional, you can skip this part if you want the default voice)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)  # Change index to select a different voice

    # Read and speak the text from pages 7 onwards
    audio_segments = []
    for num in range(0, pages):  # Changed range to start from 7th page
        page = pdf_reader.pages[num]
        text = page.extract_text()
        speaker.save_to_file(text, f'page_{num + 1}.mp3')  # Save each page as an individual MP3 file
        speaker.runAndWait()

        # Load the saved MP3 file and convert it to AudioSegment
        audio_segment = AudioSegment.from_mp3(f'page_{num + 1}.mp3')
        audio_segments.append(audio_segment)

    # Concatenate all audio segments
    combined_audio = sum(audio_segments)

    # Save the combined audio as an audiobook in the same location as the PDF
   # combined_audio.export('audiobook.mp3', format='mp3')

    # Close the PDF file
    book.close()
