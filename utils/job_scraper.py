# job_scraper.py
from bs4 import BeautifulSoup
import requests

class JobScraper:
    def extract_job_details(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract job title, description, requirements
        # Return structured dictionary
        return {
            'title': extracted_title,
            'description': extracted_description,
            'requirements': extracted_requirements
        }