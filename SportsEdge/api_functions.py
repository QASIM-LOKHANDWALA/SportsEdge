import requests
import html
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
            news_with_images = []
            news_without_images = []

            for item in news_data:
                title = html.unescape(item.get('title', '').strip())
                description = html.unescape(item.get('description', '').strip())
                url = item.get('url', '#')
                image = item.get('image', '')
                language = item.get('language', '')
                
                if title and title not in titles and language == "en":
                    titles.add(title)
                    news_item = {
                        'title': title,
                        'description': description,
                        'url': url,
                        'image': image
                    }
                    if image:
                        news_with_images.append(news_item)
                    else:
                        news_without_images.append(news_item)
            
            return news_with_images + news_without_images
        else:
            raise Exception(f"Error: Received status code {response.status_code} from API.")
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []