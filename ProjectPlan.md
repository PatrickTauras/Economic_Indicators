**Overview**

Analyzing the impact of GDP and inflation on employment trends. We are looking to see how employment rates change when GDP and inflation fluctuate.

**Research Question:**

 How do changes in GDP and inflation impact employment trends across different industries in the United States?

**Team:**

Patrick Tauras (Data Engineer) and Justin Kutsor (Data Analyst). Patrick will gather and clean the data and allow Justin to use the data sets to see if changes in GDP and inflation impact employment trends. 

**Datasets:**

The Employment Data from the Bureau of Labor Statistics (BLS) includes a JSON structure that begins with a status field indicating the success of the request, labeled as "REQUEST_SUCCEEDED". The results section identifies the data series with the ID "CES0000000001", which corresponds to Total Nonfarm Employment in the U.S. Each data entry within this series provides information by year and period, such as "2023" and "M12" for December. Additionally, the "PeriodName" field offers a human-readable month name, such as "December", and the "Value" field represents the employment count (e.g., "157304"), which is given in thousands. The BLS data is structured on a month-by-month basis, categorized by year, making it suitable for detailed employment data analysis.

The GDP Data from the Federal Reserve Economic Data (FRED) API features metadata fields like "realtime_start", "realtime_end", "observation_start", "observation_end", and "count", which provide context about the time frame and structure of the dataset. Each observation in the dataset includes a "Date" field for the specific date of the GDP observation (e.g., "1946-01-01") and a "Value" field that denotes the GDP value (e.g., "243.164"), typically representing GDP in billions of dollars, depending on FRED’s series specifications. Some entries contain a "value": ".", indicating missing data for certain periods. The GDP data is organized on a quarterly basis, which is typical for long-term GDP trends, with actual values beginning in 1947, aligning with the historical availability of U.S. GDP data.

The Inflation Data from the Federal Reserve Economic Data (FRED) API includes a JSON structure designed to provide insights into inflation trends over time. The dataset begins with metadata fields, such as "realtime_start", "realtime_end", "observation_start", "observation_end", and "count", which define the time frame and structure of the data retrieved. Each observation within this dataset contains a "date" field that specifies the exact date of the inflation measurement (e.g., "1947-01-01"), along with a "value" field representing the Consumer Price Index (CPI) for that month (e.g., "123.45"). This CPI value is an index number, typically used to calculate inflation by tracking changes in the cost of a basket of goods over time. Some entries in the dataset may contain "value": ".", indicating missing data points. The inflation data is generally structured on a monthly basis, making it compatible with employment data for detailed analysis of inflation trends over time. This setup enables the examination of inflation's impact in relation to GDP and employment trends in the U.S.

**Timeline:**

Our project timeline is designed to hit all the key requirements in manageable steps. In Weeks 1-2, we’ll set up roles, organize our GitHub repo, and finalize our main research question. We’ll grab data from the FRED and BLS APIs, making sure each dataset has distinct licenses and formats, and we’ll add integrity checks to keep things reproducible.

Moving to Weeks 3-4, we’ll focus on integrating the datasets with Python and document the process. Week 5 is for data profiling and cleanup, making sure everything’s ready for analysis. This may include some formatting changes, examining where there may be missing data, and more. From Weeks 6-7, we’ll dive into analysis and visualizations to explore how GDP and inflation impact employment trends, packaging it all in a reproducible format.

In Weeks 8-9, we’ll build an automated workflow to run everything smoothly from start to finish. This may include a tool such as Snakemake or some other tool in order to seamlessly connect all of our code. For the final touches in Weeks 10-11, we’ll wrap up documentation, cite all our sources, create metadata, and archive the project on Zenodo for a persistent identifier. Our GitHub repo will track progress and contributions, keeping us organized and on target.