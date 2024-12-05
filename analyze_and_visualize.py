import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_json("Final_Data/Filtered_Data_Onward_2015-03-31.json")

# Data Exploration
print("Dataset Info:")
print(data.info())
print("\nDescriptive Statistics:")
print(data.describe())

# 1. Line Plot: Trends over Time
plt.figure(figsize=(12, 6))
plt.plot(data['date'], data['value_emp'], label='Employment', color='blue')
plt.plot(data['date'], data['value_gdp'], label='GDP', color='green')
plt.plot(data['date'], data['value_inflation'], label='Inflation', color='red')
plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Trends in Employment, GDP, and Inflation (2015 Onward)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Results/line_plot_trends.png")
plt.close()
print("Graph 1: Line Plot saved.")

# 2. Scatterplot: GDP vs Employment
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data['value_gdp'], y=data['value_emp'], color='green')
plt.xlabel("GDP")
plt.ylabel("Employment")
plt.title("Relationship between GDP and Employment")
plt.tight_layout()
plt.savefig("Results/scatter_gdp_vs_employment.png")
plt.close()
print("Graph 2: Scatter Plot (GDP vs Employment) saved.")

# 3. Scatterplot: Inflation vs Employment
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data['value_inflation'], y=data['value_emp'], color='red')
plt.xlabel("Inflation")
plt.ylabel("Employment")
plt.title("Relationship between Inflation and Employment")
plt.tight_layout()
plt.savefig("Results/scatter_inflation_vs_employment.png")
plt.close()
print("Graph 3: Scatter Plot (Inflation vs Employment) saved.")

# 4. Heatmap of Correlations
correlation_matrix = data[['value_emp', 'value_gdp', 'value_inflation']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.savefig("Results/heatmap_correlations.png")
plt.close()
print("Graph 4: Heatmap saved.")

# 5. Bubble Plot: GDP vs Employment with Inflation as Size
plt.figure(figsize=(8, 6))
bubble_sizes = (data['value_inflation'] - data['value_inflation'].min()) * 10  # Scale inflation
plt.scatter(data['value_gdp'], data['value_emp'], s=bubble_sizes, alpha=0.5, color="purple")
plt.xlabel("GDP")
plt.ylabel("Employment")
plt.title("Bubble Plot: GDP vs Employment with Inflation")
plt.tight_layout()
plt.savefig("Results/bubble_plot_gdp_vs_employment.png")
plt.close()
print("Graph 5: Bubble Plot saved.")

# 6. Time-Lagged Line Plot: Change Over Time
plt.figure(figsize=(12, 6))
data['value_emp_diff'] = data['value_emp'].diff()  # Employment change
data['value_gdp_diff'] = data['value_gdp'].diff()  # GDP change
plt.plot(data['date'], data['value_emp_diff'], label="Change in Employment", color="blue")
plt.plot(data['date'], data['value_gdp_diff'], label="Change in GDP", color="green")
plt.xlabel("Date")
plt.ylabel("Change in Values")
plt.title("Time-Lagged Change in Employment and GDP")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Results/time_lagged_trends.png")
plt.close()
print("Graph 6: Time-Lagged Line Plot saved.")

# 7. GDP and Inflation Over Time (Dual Y-Axis)
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.set_xlabel('Date')
ax1.set_ylabel('GDP (Trillions)', color='green')
ax1.plot(data['date'], data['value_gdp'], label='GDP', color='green')
ax1.tick_params(axis='y', labelcolor='green')

ax2 = ax1.twinx()  # Second y-axis
ax2.set_ylabel('Inflation (CPI Index)', color='red')
ax2.plot(data['date'], data['value_inflation'], label='Inflation', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title("GDP and Inflation Over Time")
fig.tight_layout()
plt.savefig("Results/dual_axis_gdp_inflation.png")
plt.close()
print("Graph 7: Dual Y-Axis Plot saved.")

# 8. Employment vs Time with GDP and Inflation Shading
plt.figure(figsize=(12, 6))
plt.plot(data['date'], data['value_emp'], label='Employment', color='blue')
plt.fill_between(data['date'], data['value_gdp'], color='green', alpha=0.2, label='GDP Shading')
plt.fill_between(data['date'], data['value_inflation'], color='red', alpha=0.2, label='Inflation Shading')
plt.xlabel("Date")
plt.ylabel("Employment")
plt.title("Employment Over Time with GDP and Inflation Shading")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Results/employment_shaded_gdp_inflation.png")
plt.close()
print("Graph 8: Employment Shaded by GDP and Inflation saved.")

# Regression Analysis
X = data[['value_gdp', 'value_inflation']]
y = data['value_emp']
model = LinearRegression()
model.fit(X, y)

# Predictions and Evaluation
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# Save Results to Markdown
analysis_results_file = "Results/analysis_results.md"
with open(analysis_results_file, "w") as f:
    f.write("# Analysis Results\n\n")
    f.write("## Correlation Matrix\n")
    f.write(correlation_matrix.to_string())
    f.write("\n\n## Regression Analysis\n")
    f.write(f"Intercept: {model.intercept_}\n")
    f.write(f"Coefficients (GDP, Inflation): {model.coef_}\n")
    f.write(f"R^2 Score: {r2}\n\n")
    f.write("## Graphs Generated:\n")
    f.write("1. Line Plot: Trends over Time\n")
    f.write("2. Scatter Plot: GDP vs Employment\n")
    f.write("3. Scatter Plot: Inflation vs Employment\n")
    f.write("4. Heatmap of Correlations\n")
    f.write("5. Bubble Plot: GDP vs Employment with Inflation\n")
    f.write("6. Time-Lagged Line Plot\n")
    f.write("7. Dual Y-Axis: GDP and Inflation Over Time\n")
    f.write("8. Employment Shaded by GDP and Inflation\n")

print(f"All results saved. Check the 'analysis_results.md' file.")
