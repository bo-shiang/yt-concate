from pytube import YouTube
import time
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            # print("downloading caption for", yt.id)
            if utils.caption_file_exists(yt):
                print("found exiting caption file")
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code("a.en")
                en_caption_convert_to_srt = en_caption.generate_srt_captions()
                # print(source)
                # save the caption to a file named Output.txt
            except KeyError:
                print("KeyError when downloading caption for", yt.url)
                continue
            except AttributeError:
                print("AttributeError when downloading caption for", yt.url)
                continue
            # except TimeoutError:
            #     print("TimeoutError when downloading caption for", yt.url)
            #     continue

            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

            # except AttributeError:
            #     print("AttributeError when downloading caption for", yt.url)
            #     continue

        return data
