
import requests
from dotenv import load_dotenv
import os

load_dotenv()

FAMOUS_LEAGUES = {
    39: "Premier League", 
    140: "La Liga",
    78: "Bundesliga",
    135: "Serie A", 
    61: "Ligue 1",
    2: "UEFA Champions League",
    3: "UEFA Europa League",
    4: "Euro Championship",
    5: "World Cup"
}

API_URL = "https://v3.football.api-sports.io"
HEADERS = {
    "x-rapidapi-key": os.getenv('API_SPORTS_KEY'),
    "x-rapidapi-host": "v3.football.api-sports.io"
}

def get_leagues():
    response = requests.get(f"{API_URL}/leagues", headers=HEADERS)
    data = response.json()
    if "response" in data:
        filtered_leagues = [
            league for league in data["response"]
            if league["league"]["id"] in FAMOUS_LEAGUES
        ]
        return {"get": data["get"], "response": filtered_leagues}
    return data

def search_leagues(query):
    leagues = get_leagues().get("response", [])
    return [league for league in leagues if query.lower() in league["league"]["name"].lower()]

def get_league_details(league_id):
    response = requests.get(f"{API_URL}/leagues?id={league_id}", headers=HEADERS)
    data = response.json()
    return data["response"][0] if "response" in data and data["response"] else None

def get_league_standings(league_id, season):
    url = f"https://v3.football.api-sports.io/standings?league={league_id}&season={2023}"
    headers = {
        "x-rapidapi-key": os.getenv('API_SPORTS_KEY'),
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    response = requests.get(url=url, headers=headers)
    data = response.json()
    if "response" in data and data["response"]:
        return data["response"][0].get("league", {}).get("standings", [])
    
    return []

def get_top_scorers(league_id, season):
    response = requests.get(f"{API_URL}/players/topscorers?league={league_id}&season={2023}", headers=HEADERS)
    data = response.json()
    return data["response"] if "response" in data else []