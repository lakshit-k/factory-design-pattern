import requests
from scraper.base_scraper import JobScraper
from bs4 import BeautifulSoup

class NaukriScraper(JobScraper):
    def scrape(self, url: str):
        response = requests.get(url)
        return response.text

    def parse(self, data: str):
        soup = BeautifulSoup(data, 'html.parser')
        jobs = soup.find_all('article', class_='jobTuple')
        return [{'title': job.find('a').text.strip(), 'company': job.find('span', class_='org').text.strip()} for job in jobs]
