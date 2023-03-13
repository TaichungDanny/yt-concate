import os
from yt_concate.settings import CAPTION_DIR
from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR

class Utils:
    def __int__(self):
        pass

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_path(self, url):
        return os.path.join(CAPTION_DIR, self.get_video_id_from_url(url) + '.txt')

    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)