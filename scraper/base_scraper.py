from abc import ABC, abstractmethod


class JobScraper(ABC):    
    @abstractmethod
    def scrape(self, url: str,**kwargs):
        pass

    @abstractmethod
    def parse(self, data: str,**kwargs):
        pass
