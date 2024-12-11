rule reproduce_all:
    input:
        "Raw_Data/Inflation_data.json",
        "Raw_Data/GDP_data.json",
        "Raw_Data/Employment_data.json",
        "hash_storage/file_hashes.json",    
        "Cleaning_Data/Data_Integration.json",
        "Cleaning_Data/Cleaned_Integrated_Data.json",
        "Final_Data/Filtered_Data_Onward_2015-03-31.json",
        "Results/scatter_inflation_vs_employment_with_trendline.png",
        "Results/dual_axis_inflation_vs_employment.png",
        "Results/kde_distribution_inflation_employment.png",
        "Results/line_plot_trends.png",
        "Results/scatter_gdp_vs_employment.png",
        "Results/scatter_inflation_vs_employment.png",
        "Results/heatmap_correlations.png",
        "Results/bubble_plot_gdp_vs_employment.png",
        "Results/time_lagged_trends.png",
        "Results/dual_axis_gdp_inflation.png",
        "Results/employment_shaded_gdp_inflation.png",
        "Results/analysis_results.md"


rule inflation_data_retrieval:
    input:
        "api_keys/fred_apikey.txt"
    output:
        "Raw_Data/Inflation_data.json"
    shell:
        "python Inflation_Data_Retrieval.py"


rule GDP_data_retrieval:
    input:
        "api_keys/fred_apikey.txt"
    output:
        "Raw_Data/GDP_data.json"
    shell:
        "python GDP_Data_Retrieval.py"


rule employment_data_retrieval:
    input:
        "api_keys/bls_apikey.txt"
    output:
        "Raw_Data/Employment_data.json"
    shell:
        "python Employment_Data_Retrieval.py"





rule hash_api_check:
    input:
        "Raw_Data/Inflation_data.json",
        "Raw_Data/GDP_data.json",
        "Raw_Data/Employment_data.json"
    output:
        "hash_storage/file_hashes.json"
    shell:
        "python hash_api_check.py"


rule hash_integrity_check:
    input:
        "Raw_data/Inflation_data.json",
        "Raw_data/GDP_data.json",
        "Raw_data/Employment_data.json"
    shell:
        "python hash_api_check.py"


rule data_integration:
    input:
        "Raw_Data/Inflation_data.json",
        "Raw_Data/GDP_data.json",
        "Raw_Data/Employment_data.json"
    output:
        "Cleaning_Data/Data_Integration.json"
    shell:
        "python Data_Integration.py"


rule clean_integrated_data:
    input:
        "Cleaning_Data/Data_Integration.json"
    output:
        "Cleaning_Data/Cleaned_Integrated_Data.json"
    shell:
        "python Clean_Integrated_Data.py"


rule filter_data_2015_onward:
    input:
        "Cleaning_Data/Cleaned_Integrated_Data.json"
    output:
        "Final_Data/Filtered_Data_Onward_2015-03-31.json",
        "Results/scatter_inflation_vs_employment_with_trendline.png",
        "Results/dual_axis_inflation_vs_employment.png",
        "Results/kde_distribution_inflation_employment.png"
    shell:
        "python Filter_Data_2015_Onward.py"


rule analyze_and_visualize:
    input:
        "Final_Data/Filtered_Data_Onward_2015-03-31.json"
    output:
        "Results/line_plot_trends.png",
        "Results/scatter_gdp_vs_employment.png",
        "Results/scatter_inflation_vs_employment.png",
        "Results/heatmap_correlations.png",
        "Results/bubble_plot_gdp_vs_employment.png",
        "Results/time_lagged_trends.png",
        "Results/dual_axis_gdp_inflation.png",
        "Results/employment_shaded_gdp_inflation.png",
        "Results/analysis_results.md"
    shell:
        "python analyze_and_visualize.py"