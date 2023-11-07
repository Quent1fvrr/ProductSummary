import requests
from urllib.parse import urlencode
import Scraping.config_key as config_key

class GoogleSearchScraper:
    def __init__(self, api_key, cse_id):
        self.api_key = api_key
        self.cse_id = cse_id
        self.base_url = 'https://www.googleapis.com/customsearch/v1'

    def search(self, query, num=10):
        params = {
            'q': query,
            'cx': self.cse_id,
            'key': self.api_key,
            'num': num
        }
        url = self.base_url + '?' + urlencode(params)
        print(f"Requesting: {url}")  # Debug: print the request URL
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f'HTTP Error: {e.response.status_code}')
            print(e.response.text)
        except requests.exceptions.RequestException as e:
            print(f'Request Exception: {e}')
        except ValueError as e:
            print(f'JSON Decode Error: {e}')
            print('Response content is not valid JSON')
            print(response.text)
        return None
    
    
# Usage
if __name__ == "__main__":
    api_key = config_key.api_key
    cse_id = config_key.cse_id
    # Initialize the Google search scraper
    scraper = GoogleSearchScraper(api_key, cse_id)
    keywords = 'Airbus A320'
    
    # Perform the search
# Perform the search
    search_results = scraper.search(keywords)

    # Check if search_results is not None
    if search_results:
        # Process the search results
        for item in search_results.get('items', []):
            print(item['title'])
            print(item['link'])
    else:
        print('No search results to display.')
