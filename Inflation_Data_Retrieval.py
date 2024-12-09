import requests
import json

# FRED API key
with open("api_keys/fred_apikey.txt", "r") as f:
    api_key = f.readline().strip()


# Define the series ID for CPI (inflation measure)
series_id = "CPIAUCSL"  # Consumer Price Index for All Urban Consumers

# Set up the FRED API request
url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={API_KEY}&file_type=json"

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Save the data to a JSON file
    with open("Raw_Data/Inflation_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Inflation data saved successfully as Inflation_data.json.")
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print(response.text)  # Print the response text to see error details
