import yt_dlp
import os
from yt_concate.pipeline.steps.step import Step, StepException
from yt_concate.settings import CAPTION_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            print('downloading caption for', url)

            ydl_opts = {
                'skip_download': True,
                'writesubtitles': True,
                'writeautomaticsub': True,
                'subtitlelangs': ['en'],
                'outtmpl': os.path.join(CAPTION_DIR, utils.get_video_id_from_url(url)),
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    print(ydl.download([url]))
            except Exception as e:
                print(e)
                print("An Error occur for", url)
                continue

        return data


