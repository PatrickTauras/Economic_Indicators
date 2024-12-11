import requests
import json

# FRED API key
with open("api_keys/fred_apikey.txt", "r") as f:
    api_key = f.readline().strip()


# URL for GDP data
series_id = "GDP"  # Change this to other series IDs for different indicators
url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"

# Make the API request
response = requests.get(url)

if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    # Save the data to a JSON file
    with open("Raw_Data/GDP_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data for {series_id} saved successfully.")
else:
    print(f"Failed to retrieve data: {response.status_code}")
