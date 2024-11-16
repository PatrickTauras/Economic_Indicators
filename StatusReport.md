# Status Report

**Project:** Analyzing the Impact of GDP and Inflation on Employment Trends  
**Team Members:** Patrick Tauras (Data Engineer), Justin Kutsor (Data Analyst)  
**Date:** 11/15/2024
---

### Task Updates

- **Data Collection**: 
  - Successfully gathered data from the FRED API for GDP and inflation, and from the BLS API for employment data. The direct links to the two data sources are first https://api.stlouisfed.org/fred/series/observations for the FED API, and then https://api.bls.gov/publicAPI/v2/timeseries/data/ for the data from the BLS. Integrity checks, including SHA 256 hashing, were implemented to ensure data consistency. These should be able to be rerun, we have the hashes saved in a file to compare to, so we can consistently check to ensure the integrity of our data.
  - Encountered minor issues with API rate limits, which were resolved by implementing request delays.

- **Data Integration**: 
  - Began merging data across time periods (quarterly for GDP, monthly for CPI and employment).
  - There were some issues that we ran into, primarily given integrating the data across different timescales, particularly with the GDP data being quarterly and the CPI and employment data being monthly. We were able to overcome these challenges with some help from the datetime library and successfully converted the data to quarterly so it could all merge.

- **Data Profiling and Cleaning**:
  - Initial profiling completed, revealing some missing values in the GDP data from the early years. Missing values were handled.
  - We will continue to examine the data to ensure that it is clean and if we discover more irregularities then we will address them as they come up.

- **Analysis**:
  - Preliminary analysis has not yet started but is scheduled for completion by Week 6, with subsequent analysis and visualization occuring from weeks 6-8. Analysis will focus on correlations between variables to see how they affect employment rates in different ways. We will also use some regression analysis, using both singular and multiple linear regressions to examine how variables affect employment both alone and together.

- **Documentation, GitHub Collaboration, and Specific Tasks**:
  - Repository includes updated README.md and structured folders for each stage of the project.
  - Patrick focused on data collection scripts, while Justin reviewed data and prepared initial profiling reports. Justin also focused on doing the integrity checks and hashing, most of which can be seen in the hashes folder, with scripts and securely stored data that can be referenced for integrity checks as we go along in our project.
  -Moving forward, for analysis, Patrick will focus on the correlation analysis and singular regression analysis, while Justin will focus on multiple linear regression analysis and then visualizing the data and trends. Beyond that Justin will work on automating the workflow with snakemake while Patrick finalizes the analysis and brings it all together. Finally, Patrick will focus on citing sources and creating metadata, while Justin will work on archiving our project in Zenodo.

### Updated Timeline
- **Weeks 1-2**: Team Set up - **Completed**
- **Weeks 3-4**: Data collection and integrity checks - **Completed**
- **Week 5-6**: Data integration and profiling - **In Progress**
- **Weeks 6-8**: Analysis and visualization - **Upcoming**
- **Week 9**: Automated workflow setup - **Upcoming**
- **Weeks 10-11**: Documentation finalization and project archiving - **Upcoming**

### Changes to Project Plan

- **Timeline Adjustments**: Integration took slightly longer due to the timeline differences, so the analysis phase has been adjusted accordingly. We also expected analysis to be more in depth with these datasets than expected, while expecting the workflow portion to be smoother than expected (after working on it in lab recently) and so we planned to extend our analysis period and shorten our workflow setup period.
- **Additional Integrity Checks**: Additional/initial hashes were generated and stored to ensure data quality.


### Next Steps

We will proceed with data integration and begin analysis by November 20. The goal is to explore initial findings on how changes in GDP and inflation are associated with employment trends in the next phase. We will attempt to analyze this with a correlation analysis, visualizations to see how the numbers look on a graph, and variable analysis to consider which variables have the most effect on employment and how employment is affected by different changes.






In the Integrated_Data:

Missing values per column:
date                 0
value_emp          937
value_gdp          659
value_inflation     40
dtype: int64


### Scripts

Clean_Integrated_Data.py

Purpose: This script is used to clean the combined (integrated) dataset that includes employment, GDP, and inflation data.
Functionality: It loads the integrated dataset, performs data cleaning (such as handling missing values or standardizing formats), and saves a cleaned version as Cleaned_Integrated_Data.json for further analysis.

Data_Integration.py

Purpose: This script integrates data from multiple sources, specifically combining employment, GDP, and inflation datasets.
Functionality: It loads individual datasets, aligns them based on common fields (e.g., date), merges them into a single DataFrame, and saves the combined data in Data_Integration.json.

Employment_Data_Retrieval.py

Purpose: This script retrieves raw employment data from an external source (such as an API or a local data file).
Functionality: It fetches and saves raw employment data into Employment_data.json. This data may require further cleaning and integration with other datasets.

Filter_Data_2015_Onward.py

Purpose: A script to filter data to include only entries from March 31, 2015, onward.
Functionality: It loads Cleaned_Integrated_Data.json, filters the records to include only dates from 2015-03-31 onward, and saves the result in Filtered_Data_Onward_2015-03-31.json.

GDP_Data_Retrieval.py

Purpose: This script retrieves raw GDP data from an external source.
Functionality: It fetches GDP data and saves it as GDP_data.json, making it available for integration and analysis.

Inflation_Data_Retrieval.py

Purpose: This script retrieves raw inflation data from an external source.
Functionality: Similar to the other retrieval scripts, it fetches inflation data and saves it as Inflation_data.json for later integration and analysis.

Update_Date_Format.py

Purpose: This script updates the date format in the Cleaned_Integrated_Data.json file to a human-readable format (YYYY-MM-DD).
Functionality: It loads the JSON file, converts timestamps to a readable format, and saves the updated file back, making dates easier to interpret.

hash_api_check.py
Purpose: This script computes the initial hash values for the raw data so that we can reference them as things go along to ensure data integrity.
Functionality: It loads in the raw data files, computes the hashes for each of them, and then saves them to file_hashes.json so that we can reference them from a secure storage spot.

hash_integrity_check.py
Purpose: This script computes the current hash values for the data and then compares it to the expected values calculated from the original data from hash_api_check.py to ensure they remain the same, and it uses SHA256 hashes.
Functionality: It loads in the data files, computes the current hashes for each of them, and then compares them to our expected values from file_hashes.json.

 

#### Data Files
Cleaned_Integrated_Data.json

Purpose: Contains the cleaned and integrated dataset of employment, GDP, and inflation data.
Content: A processed version of the integrated data with consistent formatting, ready for analysis or filtering.
Data_Integration.json

Purpose: Contains the initial integrated dataset before cleaning, combining employment, GDP, and inflation data.
Content: This is the first merged version of all datasets and may contain missing or inconsistent values.
Employment_data.json

Purpose: Holds raw employment data retrieved by Employment_Data_Retrieval.py.
Content: Unprocessed employment data, which may contain missing or inconsistent entries.
Filtered_Data_Onward_2015-03-31.json

Purpose: Contains data from Cleaned_Integrated_Data.json filtered to only include entries from March 31, 2015, onward.
Content: A subset of the cleaned integrated data, with entries starting from 2015-03-31, for more focused analysis on recent years.
GDP_data.json

Purpose: Holds raw GDP data retrieved by GDP_Data_Retrieval.py.
Content: Unprocessed GDP data, possibly with missing or inconsistent values.
Inflation_data.json

Purpose: Holds raw inflation data retrieved by Inflation_Data_Retrieval.py.
Content: Unprocessed inflation data, which may need further cleaning.

