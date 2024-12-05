#add rule to run all (easy)


rule inflation_data_retrieval:
    output:
        "Cleaning_Datasets/Inflation_data.json"
    shell:
        "python Cleaning_Datasets/Inflation_Data_Retrieval.py"


rule GDP_data_retrieval:
    output:
        "Cleaning_Datasets/GDP_data.json"
    shell:
        "python Cleaning_Datasets/GDP_Data_Retrieval.py"


rule employment_data_retrieval:
    output:
        "Cleaning_Datasets/Employment_data.json"
    shell:
        "python Cleaning_Datasets/Employment_Data_Retrieval.py"





rule hash_api_check:
    input:
        "Cleaning_datasets/Inflation_data.json"
        "Cleaning_datasets/GDP_data.json"
        "Cleaning_datasets/Employment_data.json"
    output:
        "hashes/file_hashes.json"
    shell:
        "python hashes/hash_api_check.py"

#Check if need an output file here or if just printing out the values is alright
rule hash_integrity_check:
    input:
        "Cleaning_datasets/Inflation_data.json"
        "Cleaning_datasets/GDP_data.json"
        "Cleaning_datasets/Employment_data.json"
    shell:
        "python hashes/hash_api_check.py"






rule data_integration:
    input:
        "Cleaning_datasets/Inflation_data.json"
        "Cleaning_datasets/GDP_data.json"
        "Cleaning_datasets/Employment_data.json"
    output:
        "Cleaning_Datasets/Data_Integration.json"
    shell:
        "python Cleaning_Datasets/Data_Integration.py"


rule clean_integrated_data:
    input:
        "Cleaning_datasets/Data_Integration.json"
    output:
        "Cleaning_Datasets/Cleaned_Integration_Data.json"
    shell:
        "python Cleaning_Datasets/Clean_Integrated_Data.py"

#Check if this one is needed # DELETE
rule update_date_format:
    input:
        "Cleaning_datasets/Cleaned_Integration_Data.json"
    output:
        "Cleaning_Datasets/Cleaned_Integration_Data_Readable.json"
    shell:
        "python Cleaning_Datasets/Update_Date_Format.py"







rule filter_data_2015_onward:
    input:
        "Cleaning_datasets/Cleaned_Integrated_Data.json"
    output:
        "Final_Dataset/Filtered_Data_Onward_2015-03-31.json"
        "Results/scatter_inflation_vs_employment_with_trendline.png"
        "Results/dual_axis_inflation_vs_employment.png"
        "Results/kde_distribution_inflation_employment.png"
    shell:
        "python Final_Dataset/Filter_Data_2015_Onward.py"


rule analyze_and_visualize:
    input:
        "Final_Dataset/Filtered_Data_Onward_2015-03-31.json"
    output:
        "Results/line_plot_trends.png"
        "Results/scatter_gdp_vs_employment.png"
        "Results/scatter_inflation_vs_employment.png"
        "Results/heatmap_correlations.png"
        "Results/bubble_plot_gdp_vs_employment.png"
        "Results/time_lagged_trends.png"
        "Results/dual_axis_gdp_inflation.png"
        "Results/employment_shaded_gdp_inflation.png"
        "Results/analysis_results.md"
    shell:
        "python Final_Dataset/analyze_and_visualize.py"