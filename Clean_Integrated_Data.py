import pandas as pd
import numpy as np

# Load the JSON into a DataFrame
df = pd.read_json("Cleaning_Data/Data_Integration.json")

# Replace invalid GDP values
df['value_gdp'] = pd.to_numeric(df['value_gdp'], errors='coerce')  # Converts "." to NaN

# Drop rows where all key metrics are NaN
df.dropna(subset=['value_emp', 'value_gdp', 'value_inflation'], how='all', inplace=True)

# Optionally interpolate missing values (linear interpolation)
df['value_emp'] = df['value_emp'].interpolate(method='linear')
df['value_gdp'] = df['value_gdp'].interpolate(method='linear')
df['value_inflation'] = df['value_inflation'].interpolate(method='linear')

# Convert timestamp to human-readable date
df['date'] = pd.to_datetime(df['date'], unit='ms')

# Save cleaned data
df.to_json("Cleaning_Data/Cleaned_Integrated_Data.json", orient="records", indent=4)
