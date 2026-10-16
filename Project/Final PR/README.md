# Stock Market Securities Data Analysis

## Overview
This project performs Exploratory Data Analysis (EDA) on a stock market securities dataset (`stock.csv`). It involves data cleaning, filtering, grouping, and visualization to uncover insights about different stocks, ETFs, and their listing exchanges[cite: 6]. 

## Technologies and Libraries Used
The following Python libraries are utilized for data manipulation and visualization[cite: 6]:
* **NumPy:** For numerical operations.
* **Pandas:** For data loading, manipulation, and analysis.
* **Matplotlib & Seaborn:** For generating data visualizations.

## Dataset
* **File:** `stock.csv`[cite: 6]
* **Key Columns:** `Symbol`, `Security Name`, `Listing Exchange`, `Market Category`, `ETF`, `Round Lot Size`, and `Financial Status`[cite: 6].

## Key Operations Performed
1. **Data Loading & Inspection:** Read the CSV file and inspected the head, tail, and null value counts[cite: 6].
2. **Data Cleaning:** Handled missing data by filling `NaN` values in the `Financial Status` column with the string `'Unknown'`[cite: 6].
3. **Data Filtering:**
   * Segregated regular stocks (`ETF == 'N'`) and ETFs (`ETF == 'Y'`) into separate dataframes[cite: 6].
   * Filtered securities by keyword, extracting companies containing the word "Gold" in their `Security Name`[cite: 6].
   * Applied multi-condition filtering to find ETFs specifically listed on exchange 'P'[cite: 6].
4. **Data Grouping:** Grouped the dataset by `Listing Exchange` to count the total number of securities per exchange[cite: 6].

## Visualizations Generated
The notebook includes the following visual plots to represent the data distribution[cite: 6]:
* **Bar Chart:** Total count of securities grouped by `Listing Exchange`[cite: 6].
* **Pie Chart:** Percentage proportion of ETFs versus Regular Stocks[cite: 6].
* **Bar Chart:** Count of securities categorized by `Market Category`[cite: 6].
* **Stacked Bar Chart:** Comparison of ETF and Stock counts within each `Listing Exchange`[cite: 6].