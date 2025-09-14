import pandas as pd
import json
from datetime import datetime
import os

def transform_data():
    """
    Reads the raw data, transforms it, and saves it as a transformed CSV.
    """
    # Check if the raw data file exists
    if not os.path.exists('raw_data.json'):
        print("❌ TRANSFORM: raw_data.json not found. Run extract.py first.")
        return

    print("🔄 TRANSFORM: Cleaning and restructuring data...")
    
    # Read the raw data from the file
    with open('raw_data.json', 'r') as f:
        raw_data = json.load(f)

    if not raw_data or 'daily' not in raw_data:
        print("❌ TRANSFORM: Invalid or empty raw data provided.")
        return
        
    daily_data = raw_data['daily']
    df = pd.DataFrame(daily_data)
    
    # --- Transformations ---
    df.rename(columns={
        'time': 'date',
        'weathercode': 'weather_condition_code',
        'temperature_2m_max': 'max_temp_celsius',
        'temperature_2m_min': 'min_temp_celsius'
    }, inplace=True)
    
    df['date'] = pd.to_datetime(df['date'])
    df['temp_range_celsius'] = df['max_temp_celsius'] - df['min_temp_celsius']
    df['processed_at_utc'] = datetime.utcnow()
    
    # Save the transformed data to an intermediate CSV file
    df.to_csv('transformed_data.csv', index=False)
    
    print("✅ TRANSFORM: Transformed data saved to transformed_data.csv")

if __name__ == "__main__":
    transform_data()
