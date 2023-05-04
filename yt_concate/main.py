from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils

CHANNEL_ID = 'UCBJycsmduvYEL83R_U4JriQ'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    utils = Utils()
    p = Pipeline()
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
