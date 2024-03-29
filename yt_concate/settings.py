import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

DOWNLOADS_DIR = "downloads"
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, "videos")
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, "captions")
