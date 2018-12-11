import requests
from abc import *


class APIProxy(ABC):
    @abstractmethod
    def get(self):
        pass
