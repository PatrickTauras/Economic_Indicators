import pandas as pd
import json

# Load the JSON file
with open("Cleaned_Integrated_Data.json", "r") as f:
    data = json.load(f)

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Convert the 'date' column to datetime format for filtering and formatting
df['date'] = pd.to_datetime(df['date'], unit='ms')

# Filter the data for dates from "2015-03-31" onward
filtered_df = df[df['date'] >= "2015-03-31"]

# Format the 'date' column to a human-readable string format (YYYY-MM-DD)
filtered_df['date'] = filtered_df['date'].dt.strftime('%Y-%m-%d')

# Save the filtered and formatted data to a new JSON file
filtered_df.to_json("Filtered_Data_Onward_2015-03-31.json", orient="records", indent=4)

print("Filtered data saved to Filtered_Data_Onward_2015-03-31.json with human-readable date format.")
