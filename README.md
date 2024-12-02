# Economic Indicators and Employment Trends

## Link to Archival Record
[Zenodo Archive](https://doi.org/XXXX/zenodo.XXXXXX) (Add this once available)

## Contributors
- **Patrick Tauras (Data Engineer)**: Data acquisition, integration, cleaning, and workflow automation.
- **Justin Kutsor (Data Analyst)**: Data analysis, visualizations, and research question evaluation.

## Summary
This project investigates how changes in GDP and inflation impact employment trends across different industries in the United States. The analysis uses datasets from the Bureau of Labor Statistics (BLS) and the Federal Reserve Economic Data (FRED) APIs, spanning from 2015 to the present. The project involves programmatically retrieving, cleaning, and integrating the datasets, followed by detailed analysis and visualizations.

Key findings demonstrate that inflation shows a stronger positive correlation with employment trends than GDP, while both indicators provide valuable insights into economic patterns. This project applies modern data curation and analysis techniques to answer critical research questions and deliver actionable insights.

## Research Question
**How do changes in GDP and inflation impact employment trends across different industries in the United States?**

## Data Profile
### Datasets
1. **Bureau of Labor Statistics (BLS) Employment Data**
   - **Format**: JSON
   - **Description**: Monthly total nonfarm employment data (in millions) categorized by year and month.
   - **License**: Public Domain

2. **Federal Reserve Economic Data (FRED) GDP Data**
   - **Format**: JSON
   - **Description**: Quarterly GDP data (in trillions) starting from 1947, aligned with historical U.S. economic trends.
   - **License**: Public Domain

3. **Federal Reserve Economic Data (FRED) Inflation Data**
   - **Format**: JSON
   - **Description**: Monthly Consumer Price Index (CPI) values used to calculate inflation trends.
   - **License**: Public Domain

### Data Processing
- Employment data normalized to millions for readability.
- GDP data converted to trillions to match economic standards.
- Inflation calculated as a percentage increase from a base year CPI of 100.
- Missing data points handled programmatically with documented checks.

### Data Integrity
- SHA-256 checksums used for integrity verification.
- All scripts designed to retrieve and process data reproducibly.

## Timeline
**Week 1-2**: 
- Define roles, organize GitHub repository, finalize research question.
- Retrieve datasets from APIs, ensuring distinct formats and licenses.

**Week 3-4**: 
- Integrate datasets using Python and document the process.

**Week 5**: 
- Profile and clean data, ensuring readiness for analysis.

**Week 6-7**: 
- Analyze data and create visualizations to address the research question.
- Package analysis into a reproducible format.

**Week 8-9**: 
- Build and automate end-to-end workflow for seamless execution.

**Week 10-11**: 
- Finalize documentation, cite sources, create metadata, and archive the project on Zenodo.

## Visualizations
The project includes the following visualizations stored in the `Results` folder:
1. **Line Plot**: Trends in employment, GDP, and inflation over time.
2. **Scatter Plot**: GDP vs Employment with Inflation as Bubble Size.
3. **Scatter Plot with Trend Line**: Inflation vs Employment.
4. **Dual-Axis Plot**: Inflation and Employment over time.
5. **Heatmap**: Correlation matrix of key variables.
6. **KDE Plot**: Distribution of Inflation and Employment values.
7. **Time-Lagged Line Plot**: Temporal trends in employment and GDP.

## Findings
### Correlation Matrix
- Employment vs GDP: **0.77**
- Employment vs Inflation: **0.78**
- GDP vs Inflation: **0.99**

### Regression Analysis
- **R² Score**: 0.61
- **Coefficients**:
  - GDP: -0.24
  - Inflation: 196.91

### Key Insights
- Inflation shows a stronger positive correlation with employment trends than GDP.
- Employment trends closely align with inflation during periods of economic fluctuation.
- Visualizations highlight the complex relationships among these indicators.

## Future Work
- Add more economic indicators for example interest rates, consumer spending for deeper insights.
- Explore cross-country datasets for international comparisons.
- Incorporate advanced statistical and machine learning models.
- Refine workflow automation with tools like Snakemake or Airflow.

## Reproducing the Project
### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/illinois-data-curation/is477-fa24-TEAM_NAME.git
2. Nagivate to project directory:
    cd is477-fa24-TEAM_NAME
3. Install dependencies:
    pip install -r requirements.txt (in terminal)
4. Run the analysis and visualization script:
    python analyze_and_visualize.py (in terminal)
5. Execute automated workflows (if applicable):
    snakemake --cores 4


## References
- Bureau of Labor Statistics: https://www.bls.gov/
- Federal Reserve Economic Data: https://fred.stlouisfed.org/

## Libraries Used:
- matplotlib
- seaborn
- pandas
- numpy
- json
- requests
- sklearn.linear_model
- sklearn.metrics


