import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_latest_news():
    url = 'http://api.mediastack.com/v1/news'
    params = {
        "access_key": os.getenv('MEDIASTACK_API_KEY'),
        "language": "en",
        "categories": "sports",
        "limit": 50
    }

    try:
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            news_data = response.json().get('data', [])
  
            titles = set()
            filtered_news = []

            for item in news_data:
                title = item.get('title', '').strip()
                language = item.get('language', '')
                
                if title and title not in titles and language == "en":
                    titles.add(title)
                    filtered_news.append(item)
            
            return filtered_news
        else:
            raise Exception(f"Error: Received status code {response.status_code} from API.")
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []
