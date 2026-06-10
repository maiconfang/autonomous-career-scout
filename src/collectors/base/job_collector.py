from abc import ABC, abstractmethod


class JobCollector(ABC):

    @abstractmethod
    def collect(self):
        pass