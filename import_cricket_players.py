import os
import django
import sys
import pandas as pd
import numpy as np
from datetime import datetime

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SportsEdge.settings')  # Update with your project name

# Setup Django
django.setup()

from cricket.models import CricketPlayer  # Ensure CricketPlayer model exists


def convert_date(date_str):
    """Converts date formats: MM/DD/YYYY or DD/MM/YYYY → YYYY-MM-DD"""
    if pd.isna(date_str) or date_str in ["", "0000-00-00"]:
        return None  # Return None if the date is missing or invalid
    try:
        return datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y-%m-%d")  # Try MM/DD/YYYY
    except ValueError:
        try:
            return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")  # Try DD/MM/YYYY
        except ValueError:
            print(f"⚠ Error: Invalid date format `{date_str}`")
            return None


def clean_value(value, default=0):
    """Converts NaN, empty strings, or None values to a default (0 by default)."""
    return default if pd.isna(value) or value in ["", "NaN"] else value


def clean_int_value(value, default=0):
    """Ensures the value is an integer, defaulting to 0 if invalid."""
    try:
        return int(value) if not pd.isna(value) else default
    except ValueError:
        return default


# Load CSV file
csv_path = r"C:\Users\qasim\OneDrive\Desktop\cricket_archive\players_data_with_all_info.csv"  # Update file path if needed

try:
    df = pd.read_csv(csv_path, encoding="utf-8")
except FileNotFoundError:
    print(f"❌ Error: CSV file not found at `{csv_path}`")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    sys.exit(1)

# Insert data into the database
players_to_insert = []

for _, row in df.iterrows():
    try:
        player = CricketPlayer(
            id=row["id"],  # Make sure your model allows setting an `id`
            firstname=row.get("firstname", ""),
            lastname=row.get("lastname", ""),
            fullname=row.get("fullname", ""),
            image_path=row.get("image_path", ""),
            date_of_birth=convert_date(row.get("dateofbirth", "")),
            gender=row.get("gender", ""),
            batting_style=row.get("battingstyle") or None,
            bowling_style=row.get("bowlingstyle") or None,
            position=row.get("position", ""),
            continent_id=clean_int_value(row.get("continent_id"), default=None),
            continent_name=row.get("continent_name", ""),
            country_id=clean_int_value(row.get("country_id"), default=None),
            country_name=row.get("country_name", ""),
            country_image_path=row.get("country_image_path", ""),
        )
        players_to_insert.append(player)

    except Exception as e:
        print(f"⚠ Error inserting player `{row.get('fullname', 'Unknown')}`: {e}")

# Bulk insert for better performance
if players_to_insert:
    CricketPlayer.objects.bulk_create(players_to_insert, ignore_conflicts=True)
    print(f"✅ Successfully imported {len(players_to_insert)} cricket players!")
else:
    print("⚠ No valid players found in the CSV file.")
