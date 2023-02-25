from abc import ABC, abstractmethod


class Step(ABC):
    def __int__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):
    pass
