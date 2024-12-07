import requests
from scraper.base_scraper import JobScraper
from bs4 import BeautifulSoup

class LinkedInScraper(JobScraper):

    def scrape(self, url: str):
        response = requests.get(url)
        return response.text

    def parse(self, data: str):
        soup = BeautifulSoup(data, 'html.parser')
        jobs = soup.find_all('li', class_='result-card')
        return [{'title': job.find('h3').text.strip(), 'company': job.find('h4').text.strip()} for job in jobs]
