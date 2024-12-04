# Economic Indicators and Employment Trends

## Research Question
**How do changes in GDP and inflation impact employment trends across different industries in the United States?**

## Link to Archival Record
[Zenodo Archive](https://doi.org/XXXX/zenodo.XXXXXX) (Add this once available)

## Contributors
- **Patrick Tauras (Data Engineer)**: Data acquisition, integration, cleaning, and workflow automation.
- **Justin Kutsor (Data Analyst)**: Data analysis, visualizations, and research question evaluation.

## Summary

This project explores the relationship between GDP, inflation, and employment trends in the United States, focusing on how these key economic indicators interact during times of upheaval and recovery. Using data from the Bureau of Labor Statistics (BLS) and the Federal Reserve Economic Data (FRED) APIs, we analyzed trends from 2015 to the present. We paid special attention to the years 2020 and 2021, which were deeply shaped by the economic turmoil of the COVID-19 pandemic. These two years provided a unique opportunity to study how the economy responded to one of the most significant global disruptions in recent history.

Our motivation for this project was to better understand how major economic shocks, like the pandemic, ripple through different indicators and affect the workforce. The pandemic created an unprecedented economic crisis. In 2020, widespread lockdowns and restrictions halted industries, disrupted supply chains, and slashed consumer demand. This led to a sharp decline in GDP, massive job losses, and a temporary dip in inflation before it began climbing again. By 2021, the economy started showing signs of recovery, but not all indicators rebounded at the same pace. While GDP grew steadily, inflation surged due to supply shortages and pent-up demand, and employment lagged behind as businesses faced challenges in rehiring and restructuring.

The central goal of this project was to delve deeper into these trends and explore how GDP, inflation, and employment interact. Our research question, "How do changes in GDP and inflation impact employment trends across different industries in the United States?", guided our analysis. We wanted to understand whether employment trends closely followed GDP and inflation or were driven by other factors. The pandemic years, in particular, offered valuable insights into how the economy crashed and began to recover.

Understanding the economic effects of the COVID-19 pandemic was a core focus of this project. We aimed to answer questions like: How quickly did employment recover after the initial shock of 2020? Did inflation simply lag behind GDP growth, or did it develop independently during the recovery? Were there observable patterns in the economy’s rebound, and what lessons could be drawn to help policymakers prepare for future crises?

The data from 2020 and 2021 painted a vivid picture of the chaos and eventual recovery. The sharp drop in GDP and employment during the early months of the pandemic was followed by a slow but steady recovery in 2021, though at different speeds. GDP stabilized relatively quickly, inflation followed close behind, but employment took significantly longer to recover. This delay reflected deeper challenges like labor shortages, mismatched skills, and uncertainty in the job market. These findings highlighted how economic recovery is a complex process, with each indicator telling its own part of the story.

One key insight was the way inflation seemed to follow GDP. As GDP rebounded sharply in 2021, inflation mirrored its trajectory with a slight lag, driven by increased demand and lingering supply chain disruptions. This relationship was especially evident during the pandemic recovery, where the economic bounce-back fueled inflationary pressures. Employment, while connected to GDP and inflation, had its own unique recovery pattern, reflecting the challenges of restoring jobs in a disrupted labor market.

By focusing on the pandemic’s economic impact, this project revealed important insights into the dynamics of key economic indicators during crises. These findings help explain how the economy reacts in the face of a major shock and offer valuable lessons for navigating future challenges. Policymakers can use these insights to anticipate how different economic factors might respond in times of crisis and design better strategies to support recovery efforts.

In conclusion, this project highlights the interconnected nature of GDP, inflation, and employment as fundamental measures of economic health. By examining how these indicators evolved during the pandemic, we uncovered patterns and relationships that provide a clearer understanding of the recovery process. These findings are not only relevant for understanding the unique circumstances of the COVID-19 pandemic but also for equipping policymakers, businesses, and economists with tools to navigate future economic disruptions.

---

## Data Profile

### Datasets
1. **Bureau of Labor Statistics (BLS) Employment Data**
   - **Format**: JSON
   - **Description**: Monthly total nonfarm employment data (in millions), categorized by year and month.
   - **Source**: Bureau of Labor Statistics API
   - **License**: Public Domain
   - **Key Features**: Provides granular insights into workforce dynamics across industries.

2. **Federal Reserve Economic Data (FRED) GDP Data**
   - **Format**: JSON
   - **Description**: Quarterly GDP data (in trillions) starting from 1947, capturing historical U.S. economic trends.
   - **Source**: FRED API
   - **License**: Public Domain
   - **Key Features**: Tracks economic output, offering a macroeconomic perspective.

3. **Federal Reserve Economic Data (FRED) Inflation Data**
   - **Format**: JSON
   - **Description**: Monthly Consumer Price Index (CPI) values used to calculate inflation trends.
   - **Source**: FRED API
   - **License**: Public Domain
   - **Key Features**: Measures changes in the cost of goods over time, reflecting inflationary trends.

### Data Processing
- Employment data normalized to millions for readability.
- GDP data converted to trillions to align with economic reporting standards.
- Inflation calculated as a percentage increase from a base year CPI of 100 for standardization.
- The BLS Employment API only provides data starting from 2015, so the FRED datasets were filtered to include only data from 2015 onward to ensure consistency and eliminate null values. The cleaning of the datasets are shown in the Cleaning_Datasets folder. 
- Missing data points were addressed programmatically, ensuring data integrity and completeness.

### Data Integrity
- SHA-256 checksums were employed to verify dataset integrity.
- All scripts were designed to ensure reproducibility in data retrieval, processing, and analysis.

---

## Findings

### Key Insights
Our analysis revealed a strong positive correlation between GDP, inflation, and employment, underscoring their interconnectedness as key economic indicators. These relationships were particularly evident during the COVID-19 pandemic, a period that brought unprecedented disruption to global economies. Below are the primary correlations we observed:
- **Employment vs GDP**: **0.77**
- **Employment vs Inflation**: **0.78**
- **GDP vs Inflation**: **0.99**

The analysis provided several important takeaways:
1. **Inflation Lags Behind GDP**: The "GDP and Inflation Over Time" graph illustrated that GDP typically recovers more quickly following economic disruptions, while inflation takes a longer time to stabilize. This dynamic was most evident during the COVID-19 recovery in 2021 when GDP began to rebound after the sharp declines of 2020. Inflation followed closely but with a noticeable lag, reflecting how economic adjustments, such as increased demand and constrained supply chains, impacted prices over time.

2. **Employment Stabilizes Slower**: The "Time-Lagged Change in Employment and GDP" graph revealed that while GDP began to stabilize relatively quickly in 2021, employment recovery lagged significantly. This pattern highlighted the challenges businesses faced in reabsorbing workers into the labor market after the pandemic-induced layoffs and closures. Factors like mismatched job skills, worker hesitancy, and the restructuring of industries contributed to this slower recovery timeline for employment.

3. **Inflation as a Sensitive Indicator**: Among the three indicators, inflation showed the strongest correlation with employment, suggesting it may serve as a more responsive measure of workforce changes during economic shifts. This was particularly noticeable during the pandemic recovery, where rising inflation mirrored the economic rebound and pointed to increased activity across sectors.

4. **COVID-19’s Economic Impact**: The pandemic’s effects were most visible in 2020, where all three indicators—GDP, inflation, and employment—experienced steep declines. This period underscored the immediate and widespread impact of lockdowns, supply chain disruptions, and reduced consumer demand. By 2021, as restrictions eased and businesses adapted, the recovery varied across indicators. GDP and inflation showed signs of a faster rebound, but employment’s slower stabilization highlighted the ongoing challenges in rebuilding the labor market.

## Visualizations
The project includes the following visualizations stored in the `Results` folder:
1. **Line Plot**: Trends in employment, GDP, and inflation over time.
2. **Scatter Plot**: GDP vs Employment with Inflation as Bubble Size.
3. **Scatter Plot with Trend Line**: Inflation vs Employment.
4. **Dual-Axis Plot**: Inflation and Employment over time.
5. **Heatmap**: Correlation matrix of key variables.
6. **KDE Plot**: Distribution of Inflation and Employment values.
7. **Time-Lagged Line Plot**: Temporal trends in employment and GDP.

### Regression Analysis
We further quantified these relationships using a linear regression model, which provided the following insights:
- **R² Score**: 0.61, indicating that the model moderately explains the variance in employment trends.
- **Coefficients**:
  - **GDP**: **-0.24**, suggesting a minimal and slightly negative direct impact on employment when isolated.
  - **Inflation**: **196.91**, indicating a strong and significant positive relationship with employment.

The regression analysis reinforced our observations from the visualizations. While GDP is crucial for understanding broader economic health, inflation appears to have a more immediate and direct influence on employment trends. This was evident during the recovery from the pandemic when inflation surged alongside improving employment figures.

---

## Future Work

### Incorporating Additional Economic Indicators
To truly understand the bigger picture of employment trends, it would be valuable to include more economic indicators in future analyses. For instance:
- **Interest Rates**: By looking at how changes in interest rates affect inflation, GDP, and employment, we can better understand how monetary policy shapes economic recovery.
- **Consumer Spending and Savings Rates**: Exploring consumer behavior—how much people are spending or saving—could shed light on what drives employment trends, especially during periods of uncertainty.
- **Wage Growth**: Investigating the link between wage increases and employment levels might help us understand how income trends influence job markets.
- **Labor Market Dynamics**: Including metrics like labor force participation rates, unemployment duration, and job vacancies could provide a more complete picture of how the labor market evolves over time, particularly in response to economic shocks.

### Exploring Cross-Country Comparisons
A fascinating next step would be to expand this analysis beyond the United States and include data from other countries. By comparing developed and developing nations, we could uncover new insights about how different economies respond to similar challenges. For example:
- How did other countries manage employment and inflation during the COVID-19 pandemic?
- What role did government stimulus packages play in driving recovery, and how did they vary across regions?
- Were the effects of global supply chain disruptions consistent across countries, or did some economies handle them better than others?

Cross-country comparisons like these could reveal strategies and policies that lead to more resilient recoveries, providing valuable lessons for future global crises.

### Incorporating Sector-Level Analysis
While this project provided an overview of broad economic trends, digging deeper into specific industries could add a new dimension to our findings. Different sectors—like healthcare, technology, retail, and manufacturing—experienced the pandemic’s impact in unique ways. Future work could explore:
- How employment trends varied across these industries during the pandemic.
- Whether automation and technology adoption helped mitigate job losses in certain sectors.
- How inflation affected consumer-driven industries compared to capital-intensive ones.

Breaking the data down by sector would allow us to identify which industries were most vulnerable or resilient during economic downturns, helping policymakers and businesses make better-informed decisions.

### Enhancing Analytical Methods
There’s always room to improve the way we analyze data, and incorporating more advanced techniques could yield even deeper insights. For example:
- **Time Series Analysis**: Using models like ARIMA or VAR to predict trends in GDP, inflation, and employment could help us better anticipate future economic shifts.
- **Causal Inference Models**: Techniques like Difference-in-Differences (DiD) or Propensity Score Matching could isolate the impact of specific events—like the pandemic—on employment trends.
- **Machine Learning Models**: Algorithms such as Random Forests or Gradient Boosting could uncover non-linear relationships between indicators, revealing patterns that traditional methods might miss.

By refining our analytical approach, future studies could capture the complexities of economic dynamics in even greater detail, leading to more actionable insights.

---

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


