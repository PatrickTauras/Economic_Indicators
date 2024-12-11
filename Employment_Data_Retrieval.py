import requests
import json

# Your BLS API key
with open("api_keys/bls_apikey.txt", "r") as f:
    api_key = f.readline().strip()


# Define the series ID for employment data
series_id = "CES0000000001"  # Example: Total nonfarm employment, U.S.

# Set up the BLS API request
url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
headers = {"Content-Type": "application/json"}
payload = json.dumps({
    "seriesid": [series_id],
    "startyear": "2015",  # Adjust the year range based on your project needs
    "endyear": "2023",
    "registrationkey": api_key
})

# Make the API request
response = requests.post(url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Save the data to a JSON file with the specified name
    with open("Raw_Data/Employment_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Employment data saved successfully as Employment_data.json.")
else:
    print(f"Failed to retrieve data: {response.status_code}")
