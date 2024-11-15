import requests
import json

# Replace with your actual FRED API key
API_KEY = "935154deca7b4c3a957baa7a73359f1c"

# URL for GDP data
series_id = "GDP"  # Change this to other series IDs for different indicators
url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={API_KEY}&file_type=json"

# Make the API request
response = requests.get(url)

if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    # Save the data to a JSON file
    with open(f"{series_id}_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data for {series_id} saved successfully.")
else:
    print(f"Failed to retrieve data: {response.status_code}")
