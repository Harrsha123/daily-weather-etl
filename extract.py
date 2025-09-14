import requests
import json
import os

def extract_weather_data():
    """
    Fetches daily weather forecast data and saves it to a raw JSON file.
    """
    print("📍 EXTRACT: Fetching data from Open-Meteo API...")
    
    LATITUDE = 38.99
    LONGITUDE = -76.94
    URL = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset&timezone=America%2FNew_York"
    
    try:
        response = requests.get(URL)
        response.raise_for_status()
        
        raw_data = response.json()
        
        # Save the extracted data to a file for the next step
        with open('raw_data.json', 'w') as f:
            json.dump(raw_data, f)
            
        print("✅ EXTRACT: Raw data saved to raw_data.json")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ EXTRACT: Failed to retrieve data. Error: {e}")
        # Ensure a potentially old file is not used by mistake
        if os.path.exists('raw_data.json'):
            os.remove('raw_data.json')

if __name__ == "__main__":
    extract_weather_data()
