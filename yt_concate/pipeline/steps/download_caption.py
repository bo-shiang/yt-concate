from pytube import YouTube
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs):
        for url in data:
            yt = YouTube(url)
            caption = yt.captions.get_by_language_code("a.en")
            print(caption.generate_srt_captions())
            save the caption to a file named Output.txt
            text_file = open("Output.txt", "w")
            text_file.write(caption_convert_to_srt)
            text_file.close()
            break