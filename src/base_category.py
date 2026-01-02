from abc import ABC, abstractmethod


class BaseCategory(ABC):

    @abstractmethod
    def __str__(self, *args, **kwargs):
        pass
