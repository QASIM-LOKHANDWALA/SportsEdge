import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_latest_news():
  url = 'http://api.mediastack.com/v1/news'
  params = {"access_key":os.getenv('MEDIASTACK_API_KEY'),"language":"en"}
  
  try:
    response = requests.get(url=url,params=params).json()
    if(response.data):
      news = response['data']
      return news
    else:
      raise Exception('Error while fetching data from API.')
  except Exception as e:
    print(e)