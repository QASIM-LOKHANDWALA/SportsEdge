import requests

class Functions:
  @staticmethod
  def getTop10():
    url = 'https://lichess.org/api/player'
    response = requests.get(url)
    data = response.json()
    
    if not data:
      raise Exception('Error fetching top 10 players!')
    return data