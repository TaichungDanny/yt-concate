from yt_concate.pipeline.steps.step import Step


class PostFlight(Step):
    def process(self, data, inputs, utils):
        print('Postflight')
