import os
import urllib.request
import json
from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import API_KEY
from yt_concate.settings import VIDEOURL_DIR


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(API_KEY,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        for x in range(10):
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
            # for a in video_links:
            #     text_file = open(os.path.join(VIDEOURL_DIR, utils.get_video_id_from_url(a)), "w")
            #     text_file.write(a)
            #     text_file.close()
        return video_links
