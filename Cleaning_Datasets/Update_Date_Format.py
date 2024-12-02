import pandas as pd
import json

# Load the JSON file
with open("Cleaned_Integrated_Data.json", "r") as f:
    data = json.load(f)

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Convert the timestamp to a human-readable date format (YYYY-MM-DD)
df['date'] = pd.to_datetime(df['date'], unit='ms').dt.strftime('%Y-%m-%d')

# Save the updated DataFrame back to a JSON file
df.to_json("Cleaned_Integrated_Data.json", orient="records", indent=4)

print("Date format updated to human-readable form in Cleaned_Integrated_Data_Human_Readable.json")
