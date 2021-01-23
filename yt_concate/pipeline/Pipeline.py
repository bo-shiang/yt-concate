import sys

sys.path.append("/Users/Shiang/Desktop/yt-concate")

from yt_concate.pipeline.steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        for step in self.steps:
            try:
                step.process(inputs)
            except StepException as e:
                print("Exception:", e)
                break