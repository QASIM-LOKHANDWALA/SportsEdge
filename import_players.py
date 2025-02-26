import os
import django
import sys
import pandas as pd
from datetime import datetime

def convert_date(date_str):
    try:
        # Try MM/DD/YYYY format first
        return datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y-%m-%d")
    except ValueError:
        try:
            # Try DD/MM/YYYY format
            return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print(f"Error: Invalid date format {date_str}")
            return None  # Return None if the format is unknown
        
import numpy as np

def clean_value(value):
    """Convert NaN values to 0 or appropriate default."""
    return 0 if (value is None or value == "" or (isinstance(value, float) and np.isnan(value))) else value

def clean_int_value(value, default=0):
    """Ensure value is an integer, defaulting to 0 if None or empty."""
    try:
        return int(value) if value not in [None, "", "NaN"] else default
    except ValueError:
        return default



# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SportsEdge.settings')  # Change to your project name

django.setup()

from football.models import Player  # Ensure Player model exists

# Load CSV file
csv_path = "fifa_players.csv"  # Make sure the path is correct
df = pd.read_csv(csv_path)

# Insert data into the database
for _, row in df.iterrows():
    Player.objects.create(
    name=row["name"],
    full_name=row["full_name"],
    birth_date=convert_date(row["birth_date"]),  
    age=row["age"],
    height_cm=row["height_cm"],
    weight_kgs=row["weight_kgs"],
    positions=row["positions"],
    nationality=row["nationality"],
    overall_rating=row["overall_rating"],
    potential=row["potential"],
    value_euro=clean_value(row["value_euro"]),
    wage_euro=clean_value(row["wage_euro"]),
    release_clause_euro=clean_value(row.get("release_clause_euro")),
    preferred_foot=row["preferred_foot"],
    international_reputation=row.get("international_reputation"),
    weak_foot=clean_int_value(row.get("weak_foot"), default=1),  # Default to 1 if missing
    skill_moves=clean_int_value(row.get("skill_moves"), default=1),  # Default to 1
    body_type=row["body_type"]
)

    
print("Data imported successfully!")
