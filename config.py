# config.py
# All constants are defined here.
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

DEVICE = "cuda"

AUDIO_FILE = "example-audio.mp3"

BATCH_SIZE = 16  # Reduce if low on GPU memory

COMPUTE_TYPE = "float16"  # Change to "int8" if low on GPU memory

# LANGUAGE: If the SRT for the video will be translated, set this to the target language code (e.g., 'en' for English). If not, use the original language code.
LANGUAGE = "en"  # 'tr' for Turkish, 'en' for English, etc.

# SRT_PATH is now automatically set based on AUDIO_FILE
SRT_PATH = f"subtitle-{LANGUAGE.upper()}-{os.path.splitext(AUDIO_FILE)[0]}.srt"
