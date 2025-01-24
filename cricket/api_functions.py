import requests
import os
from dotenv import load_dotenv

load_dotenv()

class CricketDataAPI:
  BASE_URL = "https://api.cricapi.com/v1/"
  
  def __init__(self):
    self.api_key = os.getenv('CRICKET_DATA_API_KEY')
    print(self.get_current_matches())
  
  def get_current_matches(self):
    url = f"{self.BASE_URL}currentMatches"
    
    try:
      response = requests.get(
        url, 
        params={'apikey': self.api_key}
      )
      
      if response.status_code == 200:
        data = response.json()
        matches = data.get('data')
        print(matches)
        return matches
      
      else:
        print(f"Error fetching matches: {response.status_code}")
        return []
    except requests.RequestException as e:
      print(f"Request error: {e}")
      return []
    