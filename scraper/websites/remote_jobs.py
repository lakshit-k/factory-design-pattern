import requests
from bs4 import BeautifulSoup
from scraper.base_scraper import JobScraper


class RemoteJobsScraper(JobScraper):
    def scrape(self, url: str):
        response = requests.get(url)
        return response.text

    def parse(self, data: str):
        soup = BeautifulSoup(data, 'html.parser')
        jobs = soup.find_all('div', class_='job')
        return [{'title': job.find('h2').text.strip(), 'company': job.find('span').text.strip()} for job in jobs]
