from gtts import gTTS
from PyPDF2 import PdfReader
from pydub import AudioSegment
import os

# Specify the PDF file path
file_path = r'C:\Users\Prasad\Desktop\SARAVANAN\a.pdf'

# Open the PDF file in binary mode
with open(file_path, 'rb') as book:
    pdf_reader = PdfReader(book)
    pages = len(pdf_reader.pages)

    audio_segments = []

    # Read and convert the text from pages 7 onwards to speech using gTTS
    for num in range(0, pages):  # Changed range to start from 7th page
        page = pdf_reader.pages[num]
        text = page.extract_text()

        # Convert text to speech using gTTS
        tts = gTTS(text, lang='en', slow=False)
        tts.save(f'page_{num + 1}.mp3')

        # Load the saved MP3 file and convert it to AudioSegment
        audio_segment = AudioSegment.from_mp3(f'page_{num + 1}.mp3')
        audio_segments.append(audio_segment)

# Concatenate all audio segments
combined_audio = sum(audio_segments)

# Save the combined audio as an audiobook
combined_audio.export('audiobook.mp3', format='mp3') # type: ignore

# Clean up individual page audio files (optional)
for num in range(0, pages):
    mp3_file_path = f'page_{num + 1}.mp3'
    if os.path.exists(mp3_file_path):
        os.remove(mp3_file_path)
