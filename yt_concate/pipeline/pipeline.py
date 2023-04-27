from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.steps.get_video_list import GetVideoList


class Pipeline:
    steps = [
        GetVideoList(),
    ]

    def __int__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs)
            except StepException as e:
                print('Exception happened', e)
                break
