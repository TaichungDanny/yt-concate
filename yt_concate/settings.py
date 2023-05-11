import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')

DOWNLOAD_DIR = 'download'
CAPTION_DIR = os.path.join(DOWNLOAD_DIR, 'caption')
VIDEO_DIR = os.path.join(DOWNLOAD_DIR, 'video')
VIDEOURL_DIR = os.path.join(DOWNLOAD_DIR, 'videolist')

