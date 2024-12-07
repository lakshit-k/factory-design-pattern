from scraper.websites import *
from utility.constants import WebsiteEnum

class ScraperFactory:
    scraper = {
        WebsiteEnum.LINKEDIN.value: LinkedInScraper,
        WebsiteEnum.REMOTE_JOBS.value: RemoteJobsScraper,
        WebsiteEnum.NAUKRI.value: NaukriScraper
    }

    @classmethod
    def create_scraper(cls,platform: str):
        scraper = cls.scraper.get(platform)
        if not scraper:
            raise ValueError(f"Unknown platform: {platform}")
        return scraper()
    


