from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.preflight import PreFlight
from yt_concate.pipeline.steps.postflight import PostFlight


class Pipeline:
    steps = [
        PreFlight(),
        GetVideoList(),
        DownloadCaptions(),
        PostFlight(),

    ]

    def __int__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print('Exception happened', e)
                break
        return data
