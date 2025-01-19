import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_leagues():
  url = "https://v3.football.api-sports.io/leagues"
  headers = {
    "x-rapidapi-key": os.getenv('API_SPORTS_KEY'),
    "x-rapidapi-host":"v3.football.api-sports.io"
  }
  response = requests.get(url=url,headers=headers)
  data = response.json()
  return data