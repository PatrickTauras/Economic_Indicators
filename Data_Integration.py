import pandas as pd
import json

# Load Employment Data
with open("Raw_Data/Employment_data.json", "r") as employment_file:
    employment_data = json.load(employment_file)

# Load GDP Data
with open("Raw_Data/GDP_data.json", "r") as gdp_file:
    gdp_data = json.load(gdp_file)

# Load Inflation Data
with open("Raw_Data/Inflation_data.json", "r") as inflation_file:
    inflation_data = json.load(inflation_file)

# Convert Employment Data into a DataFrame
employment_df = pd.DataFrame(employment_data["Results"]["series"][0]["data"])

# Convert GDP Data into a DataFrame
gdp_df = pd.DataFrame(gdp_data["observations"])

# Convert Inflation Data into a DataFrame
inflation_df = pd.DataFrame(inflation_data["observations"])

# Date Parsing and Cleanup for Employment Data
# Create a 'date' column from year and month in employment data
employment_df['date'] = pd.to_datetime(employment_df['year'] + '-' + employment_df['period'].str[1:], errors='coerce')

# Drop rows where date parsing failed (NaT values)
employment_df = employment_df.dropna(subset=['date'])

# Convert 'value' column in employment data to numeric
employment_df['value'] = pd.to_numeric(employment_df['value'], errors='coerce')

# Resample Employment Data to Quarterly Frequency
employment_df = employment_df.set_index('date')[['value']].resample('Q').mean().reset_index()

# Rename Columns for Clarity in Employment Data
employment_df.rename(columns={'value': 'value_emp'}, inplace=True)

# Date Parsing and Cleanup for GDP and Inflation Data
gdp_df['date'] = pd.to_datetime(gdp_df['date'], errors='coerce')
inflation_df['date'] = pd.to_datetime(inflation_df['date'], errors='coerce')

# Ensure GDP and Inflation 'value' Columns Are Numeric
gdp_df['value'] = pd.to_numeric(gdp_df['value'], errors='coerce')
inflation_df['value'] = pd.to_numeric(inflation_df['value'], errors='coerce')

# Rename GDP and Inflation Columns for Clarity
gdp_df.rename(columns={'value': 'value_gdp'}, inplace=True)
inflation_df.rename(columns={'value': 'value_inflation'}, inplace=True)

# Merge Employment, GDP, and Inflation DataFrames
integrated_df = pd.merge(employment_df, gdp_df[['date', 'value_gdp']], on="date", how="outer")
integrated_df = pd.merge(integrated_df, inflation_df[['date', 'value_inflation']], on="date", how="outer")

# Save the Integrated Data to a JSON File
integrated_df.to_json("Cleaning_Data/Data_Integration.json", orient="records", indent=4)

# Initial Profiling
print("Missing Values Per Column:")
print(integrated_df.isna().sum())

print("\nOutliers in Employment Values:")
outliers = integrated_df[
    (integrated_df['value_emp'] > integrated_df['value_emp'].mean() + 3 * integrated_df['value_emp'].std()) |
    (integrated_df['value_emp'] < integrated_df['value_emp'].mean() - 3 * integrated_df['value_emp'].std())
]
print(outliers)
