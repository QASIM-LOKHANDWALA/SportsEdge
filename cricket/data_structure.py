from .api_functions import CricketDataAPI

class MatchNode:
    def __init__(self, match_data):
        self.data = match_data
        self.next = None

class SeriesNode:
    def __init__(self, series_data):
        self.data = series_data
        self.next = None

class CricketDataStructure:
    def __init__(self):
        self.matches_head = None
        self.series_head = None
        self.matches_count = 0
        self.series_count = 0
    
    def add_match(self, match_data):
        new_node = MatchNode(match_data)
        if not self.matches_head:
            self.matches_head = new_node
        else:
            current = self.matches_head
            while current.next:
                current = current.next
            current.next = new_node
        self.matches_count += 1
    
    def add_series(self, series_data):
        new_node = SeriesNode(series_data)
        if not self.series_head:
            self.series_head = new_node
        else:
            current = self.series_head
            while current.next:
                current = current.next
            current.next = new_node
        self.series_count += 1
    
    def get_all_matches(self):
        matches = []
        current = self.matches_head
        while current:
            matches.append(current.data)
            current = current.next
        return matches
    
    def get_all_series(self):
        series = []
        current = self.series_head
        while current:
            series.append(current.data)
            current = current.next
        return series
    
    def search_match_by_name(self, name):
        current = self.matches_head
        while current:
            if current.data.get('name', '').lower() == name.lower():
                return current.data
            current = current.next
        return None
    
    def search_series_by_name(self, name):
        current = self.series_head
        while current:
            if current.data.get('name', '').lower() == name.lower():
                return current.data
            current = current.next
        return None

class CricketDataManager:
    def __init__(self):
        self.api = CricketDataAPI()
        self.data_structure = CricketDataStructure()
    
    def refresh_data(self):
        self.data_structure = CricketDataStructure()
        
        matches = self.api.get_current_matches()
        if matches:
            for match in matches:
                self.data_structure.add_match(match)
        
        series = self.api.get_series()
        if series:
            for s in series:
                self.data_structure.add_series(s)
        
        return {
            'matches': self.data_structure.get_all_matches(),
            'series': self.data_structure.get_all_series()
        }