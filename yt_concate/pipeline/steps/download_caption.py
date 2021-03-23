from pytube import YouTube
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException
import time


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print('downloading caption for', url)
            if utils.caption_file_exists(url):
                print("found exiting caption file")
                continue
            try:
            yt = YouTube(url)
            caption = yt.captions.get_by_language_code("a.en")
            # print(caption.generate_srt_captions())
            # save the caption to a file named Output.txt
            except (KeyError, AssertionError):
                print('KeyError when downloading caption for', url)
                continue
            text_file = open(utils.get_caption_path(url), "w", encoding="utf-8")
            text_file.write(caption.generate_srt_captions())
            text_file.close()

        end = time.time()
        print("took", end - start, "seconds")
