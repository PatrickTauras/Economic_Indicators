import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the Results folder path
results_folder = "Results"
data_folder = "Final_Data"
os.makedirs(data_folder, exist_ok=True)  # Ensure the folder exists
os.makedirs(results_folder, exist_ok=True)  # Ensure the folder exists

# Load the JSON file
with open("Cleaning_Data/Cleaned_Integrated_Data.json", "r") as f:
    data = json.load(f)

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Convert the 'date' column to datetime format for filtering and formatting
df['date'] = pd.to_datetime(df['date'], unit='ms')

# Filter the data for dates from "2015-03-31" onward
filtered_df = df[df['date'] >= "2015-03-31"]

# Format the 'date' column to a human-readable string format (YYYY-MM-DD)
filtered_df['date'] = filtered_df['date'].dt.strftime('%Y-%m-%d')

# Convert 'value_emp' to millions
filtered_df['value_emp'] = filtered_df['value_emp'] / 1_000

# Convert 'value_gdp' to trillions
filtered_df['value_gdp'] = filtered_df['value_gdp'] / 1_000

# Calculate 'value_inflation' as a percentage increase from the base year (base year CPI = 100)
base_year_cpi = 100
filtered_df['value_inflation'] = ((filtered_df['value_inflation'] - base_year_cpi) / base_year_cpi) * 100

# Save the filtered and formatted data to the Results folder
filtered_data_file = os.path.join(data_folder, "Filtered_Data_Onward_2015-03-31.json")
filtered_df.to_json(filtered_data_file, orient="records", indent=4)
print(f"Filtered data saved as '{filtered_data_file}'")

# Plot 1: Scatter Plot with Trend Line (Inflation vs Employment)
scatter_with_trendline_file = os.path.join(results_folder, "scatter_inflation_vs_employment_with_trendline.png")
plt.figure(figsize=(8, 6))
sns.regplot(x=filtered_df['value_inflation'], y=filtered_df['value_emp'], color='blue', ci=None)
plt.xlabel("Inflation (%)")
plt.ylabel("Employment (Millions)")
plt.title("Inflation vs Employment with Trend Line")
plt.tight_layout()
plt.savefig(scatter_with_trendline_file)
plt.close()
print(f"Scatter plot with trend line saved as '{scatter_with_trendline_file}'")

# Plot 2: Dual-Axis Line Plot (Inflation and Employment Over Time)
dual_axis_plot_file = os.path.join(results_folder, "dual_axis_inflation_vs_employment.png")
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.set_xlabel("Date")
ax1.set_ylabel("Employment (Millions)", color="blue")
ax1.plot(filtered_df['date'], filtered_df['value_emp'], color="blue", label="Employment")
ax1.tick_params(axis="y", labelcolor="blue")
ax1.tick_params(axis="x", rotation=45)

ax2 = ax1.twinx()
ax2.set_ylabel("Inflation (%)", color="red")
ax2.plot(filtered_df['date'], filtered_df['value_inflation'], color="red", linestyle="--", label="Inflation")
ax2.tick_params(axis="y", labelcolor="red")

fig.tight_layout()
plt.title("Inflation and Employment Over Time")
plt.savefig(dual_axis_plot_file)
plt.close()
print(f"Dual-axis line plot saved as '{dual_axis_plot_file}'")

# Plot 3: KDE Plot for Distribution
kde_plot_file = os.path.join(results_folder, "kde_distribution_inflation_employment.png")
plt.figure(figsize=(8, 6))
sns.kdeplot(filtered_df['value_inflation'], label="Inflation (%)", fill=True, color="red", alpha=0.6)
sns.kdeplot(filtered_df['value_emp'], label="Employment (Millions)", fill=True, color="blue", alpha=0.6)
plt.xlabel("Values")
plt.ylabel("Density")
plt.title("Distribution of Inflation and Employment")
plt.legend()
plt.tight_layout()
plt.savefig(kde_plot_file)
plt.close()
print(f"KDE distribution plot saved as '{kde_plot_file}'")
