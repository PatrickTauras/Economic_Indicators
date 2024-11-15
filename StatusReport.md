# Status Report

**Project:** Analyzing the Impact of GDP and Inflation on Employment Trends  
**Team Members:** Patrick Tauras (Data Engineer), Justin Kutsor (Data Analyst)  
**Date:** 11/15/2024
---

### Task Updates

- **Data Collection**: 
  - Successfully gathered data from the FRED API for GDP and inflation, and from the BLS API for employment data. Integrity checks, including [mention checks], were implemented to ensure data consistency.
  - Encountered minor issues with API rate limits, which were resolved by implementing request delays.

- **Data Integration**: 
  - Began merging data across time periods (quarterly for GDP, monthly for CPI and employment).
  - [Any specific issues or challenges you faced, like aligning data on different timescales].

- **Data Profiling and Cleaning**:
  - Initial profiling completed, revealing some missing values in the GDP data from the early years. Missing values were [handled/are planned to be handled].
  - Additional data cleaning steps planned include [list planned steps if any].

- **Analysis**:
  - Preliminary analysis has not yet started but is scheduled for completion by [expected date]. Analysis will focus on [outline briefly the analytical approach].

- **Documentation and GitHub Collaboration**:
  - Repository includes updated README.md and structured folders for each stage of the project.
  - Patrick focused on data collection scripts, while Justin reviewed data and prepared initial profiling reports.

### Updated Timeline

- **Weeks 1-2**: Data collection and integrity checks - **Completed**
- **Weeks 3-4**: Data integration and profiling - **In Progress**
- **Weeks 5-6**: Analysis and visualization - **Upcoming**
- **Weeks 7-8**: Automated workflow setup - **Upcoming**
- **Weeks 9-10**: Documentation finalization and project archiving - **Upcoming**

### Changes to Project Plan

- **Adjusted Analysis Approach**: Due to [reason], we decided to modify our analysis approach to include [specific change].
- **Timeline Adjustments**: Integration took slightly longer due to [reason], so the analysis phase has been adjusted accordingly.
- **Additional Integrity Checks**: Added additional [mention specific checks] to ensure data quality.

---

### Next Steps

We will proceed with data integration and begin analysis by [expected start date]. The goal is to explore initial findings on how changes in GDP and inflation are associated with employment trends in the next phase.






In the Integrated_Data:

Missing values per column:
date                 0
value_emp          937
value_gdp          659
value_inflation     40
dtype: int64


###Scripts

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


####Data Files
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

