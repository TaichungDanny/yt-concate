import os
from yt_concate.settings import DOWNLOAD_DIR, VIDEO_DIR, CAPTION_DIR, VIDEOURL_DIR


class Utils:
    def __int__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)
        os.makedirs(VIDEOURL_DIR, exist_ok=True)


    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]



