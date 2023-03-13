from pytube import YouTube
from yt_concate.pipeline.steps.step import Step



class DownloadYTCaption(Step):
    def process(self, data, inputs, utils):
        for url in data:
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)
            text_file = open(utils.get_caption_path(url), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break



