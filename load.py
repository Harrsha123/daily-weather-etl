import os
from datetime import datetime

def load_data():
    """
    Loads the transformed data into its final destination by renaming the file.
    Also cleans up the raw data file.
    """
    if not os.path.exists('transformed_data.csv'):
        print("❌ LOAD: transformed_data.csv not found. Run transform.py first.")
        return

    print("💾 LOAD: Loading data to final destination...")

    # Generate the final, date-stamped filename
    today_str = datetime.now().strftime("%Y-%m-%d")
    final_file_name = f"college_park_weather_{today_str}.csv"

    # Rename the file to its final name (simulating a 'load' operation)
    os.rename('transformed_data.csv', final_file_name)
    
    # Clean up the intermediate raw data file
    if os.path.exists('raw_data.json'):
        os.remove('raw_data.json')
    
    print(f"✅ LOAD: Data loaded successfully into '{final_file_name}'")
    print("🧼 Cleanup: Intermediate files removed.")

if __name__ == "__main__":
    load_data()