# Seasonal Agriculture Performance Analysis

## VOIS AICTE 2026–2027 Major Project

---

## 1. Project Overview

This is a **Data Analytics** project that studies how agricultural performance changes across the three main Indian farming seasons — **Kharif**, **Rabi**, and **Zaid**. Using a dataset of 4,000 farm records with 28 columns, the project explores crop yield, production, profit, environmental conditions, irrigation methods, and resource usage. The goal is to identify useful seasonal patterns and provide practical, data-supported recommendations.

This is **not** a machine learning or prediction project. It focuses on data cleaning, exploratory data analysis, seasonal comparison, statistical testing, visualization, and interpretation.

---

## 2. Problem Statement

Agricultural performance can change across Kharif, Rabi, and Zaid seasons because environmental conditions, farming practices, resource availability, and market conditions vary throughout the year. Without looking at the data carefully, it is difficult to know which seasons are more productive or profitable, which crops do better in which season, or how irrigation methods compare.

This project analyzes the given agricultural dataset to understand these seasonal differences and identify useful patterns that can help with farm planning and decision-making.

---

## 3. Project Objectives

1. Explore and understand the agricultural dataset.
2. Clean and prepare the data for analysis.
3. Compare agricultural performance (yield, production, profit) across seasons.
4. Identify important seasonal patterns.
5. Examine environmental conditions across seasons.
6. Compare resource and irrigation usage.
7. Study crop performance across seasons.
8. Analyze economic outcomes by season.
9. Identify relationships between variables using correlation analysis.
10. Apply suitable statistical methods (ANOVA) to test for significant differences.
11. Develop findings and practical recommendations based on the data.

---

## 4. Dataset Description

| Detail | Value |
|---|---|
| **File** | `seasonal_agriculture_performance_dataset.csv` |
| **Total Records** | 4,000 farm records |
| **Total Columns** | 28 |
| **Seasons** | Kharif (1,779), Rabi (1,627), Zaid (594) |
| **Crops** | Rice (690), Wheat (614), Maize (551), Cotton (508), Pulses (496), Groundnut (424), Chilli (412), Sugarcane (305) |
| **States** | 8 states |
| **Districts** | 10 agricultural districts |
| **Irrigation Methods** | Flood (1,310), Rainfed (1,041), Drip (915), Sprinkler (734) |

The dataset covers identifiers, geography, environmental conditions, soil parameters, farming inputs, crop yield, economics, and disease/pest risk.

---

## 5. Technologies Used

- **Python 3.13**
- **Pandas** — Data loading, cleaning, grouping, and pivot tables
- **NumPy** — Numerical calculations
- **Matplotlib** — Charts and visualizations
- **Seaborn** — Statistical plots and heatmaps
- **SciPy** — Pearson correlation and One-Way ANOVA tests

---

## 6. Data Cleaning

| Check | Result |
|---|---|
| Initial missing values | 120 total |
| Rainfall_mm missing | 48 (1.20%) |
| Soil_Moisture_pct missing | 40 (1.00%) |
| Yield_Tonnes_Ha missing | 32 (0.80%) |
| Imputation method | Median imputation |
| Missing values after cleaning | 0 |
| Duplicate rows | 0 |
| Final dataset shape | 4,000 rows × 28 columns |

Median imputation was chosen because median is less sensitive to outliers compared to mean, and the percentage of missing values was small (1.20% or less per column).

---

## 7. Main Analysis Performed

The project covers the following analyses:

1. **Data Loading and Exploration** — Understanding the dataset structure, columns, and basic statistics.
2. **Data Cleaning** — Handling missing values and checking for duplicates.
3. **Seasonal Performance Analysis** — Comparing yield, production, revenue, cost, and profit across Kharif, Rabi, and Zaid.
4. **Environmental Conditions by Season** — Comparing rainfall, temperature, humidity, sunlight, and soil moisture.
5. **Crop × Season Analysis** — Average yield for each crop in each season.
6. **Irrigation Analysis** — Comparing yield, profit, water used, and water efficiency across irrigation methods.
7. **Economic Analysis** — Comparing revenue, cost, and profit across seasons.
8. **Correlation Analysis** — Pearson correlation between environmental variables and yield, and among key numerical variables.
9. **Statistical Hypothesis Testing (ANOVA)** — Testing whether seasonal differences in yield and profit are statistically significant.
10. **Additional Student-Driven Analyses** — Profit margin by season, water efficiency vs profit, and disease/pest risk by crop and season.

---

## 8. Key Analytical Questions and Verified Findings

### Q1. How does agricultural performance vary across seasons?

| Season | Mean Yield (t/ha) | Mean Production (t) | Mean Revenue (₹) | Mean Total Cost (₹) | Mean Profit (₹) |
|---|---|---|---|---|---|
| **Kharif** | 5.63 | 46.31 | 710,719.06 | 531,804.41 | 178,914.65 |
| **Rabi** | 5.04 | 41.49 | 601,526.05 | 513,836.58 | 87,689.47 |
| **Zaid** | 4.64 | 38.89 | 519,171.90 | 543,976.73 | -24,804.82 |

Kharif performed the best overall. Zaid recorded an average net loss.

### Q2. Which season has the highest and lowest average yield?

- **Highest:** Kharif (5.63 t/ha)
- **Lowest:** Zaid (4.64 t/ha)

### Q3. How do environmental conditions differ across seasons?

| Season | Rainfall (mm) | Temp (°C) | Humidity (%) | Sunlight (hrs/day) | Soil Moisture (%) | Disease/Pest Risk (%) |
|---|---|---|---|---|---|---|
| **Kharif** | 849.20 | 28.45 | 71.81 | 6.79 | 31.15 | 54.47 |
| **Rabi** | 437.62 | 23.49 | 57.89 | 7.59 | 24.07 | 40.48 |
| **Zaid** | 304.65 | 31.04 | 52.01 | 8.18 | 19.28 | 38.22 |

Kharif has the highest rainfall and humidity; Zaid has the highest temperature and sunlight hours.

### Q4. How does resource usage vary across seasons?

Water usage was similar across seasons. Fertilizer application was relatively uniform (~185–187 kg/ha). Kharif recorded the highest water efficiency (5.89 t/1,000m³) and Zaid the lowest (4.41 t/1,000m³).

### Q5. Which crops perform best in different seasons?

| Crop | Kharif | Rabi | Zaid |
|---|---|---|---|
| Chilli | 1.73 | 1.47 | 1.20 |
| Cotton | 1.37 | 1.20 | 0.96 |
| Groundnut | 1.48 | 1.23 | 1.04 |
| Maize | 2.97 | 2.60 | 2.29 |
| Pulses | 1.04 | 0.88 | 0.67 |
| Rice | 2.70 | 2.32 | 1.90 |
| Sugarcane | 53.46 | 43.29 | 38.42 |
| Wheat | 2.25 | 2.06 | 1.75 |

Sugarcane recorded the highest biomass yield across all seasons, which is expected since it is a high-biomass crop. Among the food-grain crops, Maize led in all three seasons.

### Q6. Does irrigation method show differences in yield, profit, and water efficiency?

| Irrigation Method | Mean Yield (t/ha) | Mean Profit (₹) | Mean Water Used (m³) | Water Efficiency (t/1,000m³) |
|---|---|---|---|---|
| **Drip** | 6.58 | 219,626.00 | 5,918.75 | 6.27 |
| **Sprinkler** | 5.16 | 91,121.08 | 6,208.26 | 4.67 |
| **Flood** | 4.86 | 73,354.02 | 8,026.47 | 3.44 |
| **Rainfed** | 4.60 | 79,050.37 | 3,549.55 | 7.56 |

- Drip recorded the highest observed average yield and profit in this dataset.
- Rainfed recorded the highest water-efficiency value (7.56 t/1,000m³).
- Flood consumed the most water and had the lowest water efficiency.

### Q7. Which environmental variable has the strongest relationship with yield?

| Variable | Pearson r | p-value |
|---|---|---|
| Rainfall_mm | +0.0310 | 0.0503 |
| Avg_Temperature_C | +0.0100 | 0.5274 |
| Humidity_pct | +0.0123 | 0.4368 |
| Sunlight_Hours_Day | -0.0153 | 0.3320 |
| Soil_Moisture_pct | +0.0110 | 0.4868 |

Rainfall showed the strongest linear correlation among the environmental variables examined, but the relationship was extremely weak and not statistically significant at the 5% level (p = 0.0503 > 0.05). Environmental variables alone are not strong linear predictors of yield in this dataset.

### Q8. How do economic outcomes vary across seasons?

- Kharif generated the highest mean revenue (₹710,719.06) and the highest mean profit (₹178,914.65).
- Rabi generated ₹601,526.05 revenue and ₹87,689.47 profit.
- Zaid generated ₹519,171.90 revenue but total costs (₹543,976.73) exceeded revenue, resulting in an average net loss of -₹24,804.82.

### Q9. Which numerical variables have the strongest relationships with yield and profit?

- **Yield** correlated most strongly with Water Efficiency (r = +0.9126) and Production (r = +0.8828).
- **Profit** correlated most strongly with Revenue (r = +0.8873), followed by Production (r = +0.5542), Water Efficiency (r = +0.4895), and Yield (r = +0.4885).

### Q10. Are there noticeable differences in disease/pest risk across seasons?

- Kharif showed the highest average disease/pest risk (54.47%), compared to Rabi (40.48%) and Zaid (38.22%).
- This is associated with the higher humidity during the monsoon season.

---

## 9. Statistical Hypothesis Testing (ANOVA)

Both tests were performed at a significance level of α = 0.05.

### A. One-Way ANOVA — Yield Across Seasons

- **Null Hypothesis (H₀):** The mean yield is the same across Kharif, Rabi, and Zaid.
- **F-statistic:** 1.5439
- **p-value:** 0.2137
- **Conclusion:** Fail to reject H₀. Seasonal yield differences are **not statistically significant** at the 5% level.

### B. One-Way ANOVA — Profit Across Seasons

- **Null Hypothesis (H₀):** The mean profit is the same across Kharif, Rabi, and Zaid.
- **F-statistic:** 34.2918
- **p-value:** 1.7124 × 10⁻¹⁵
- **Conclusion:** Reject H₀. Seasonal profit differences are **highly statistically significant** (p < 0.001).

---

## 10. Additional Student-Driven Analyses

These analyses were added beyond the main project requirements.

### Analysis 1: Profit Margin by Season

**Formula:** Profit Margin (%) = (Profit / Revenue) × 100

| Season | Average Profit Margin (%) |
|---|---|
| Kharif | -38.64 |
| Rabi | -44.27 |
| Zaid | -69.35 |

Kharif has the highest (least negative) average profit margin. The negative profit margins are verified as correct — a validation check confirmed that Profit = Revenue − Total Cost exactly for all 4,000 records.

### Analysis 2: Water Efficiency vs Profit

- **Pearson r:** +0.4895
- **p-value:** < 0.001 (statistically significant)

Water efficiency showed a moderate positive association with profit in the dataset. Since the analysis is observational, this association does not prove causation.

### Analysis 3: Disease/Pest Risk by Crop and Season

The crop-season combination with the highest recorded average disease/pest risk was **Wheat during Kharif** at **55.58%**.

This is an observational finding — the analysis does not claim that any specific environmental factor caused the higher risk.

---

## 11. Six Final Visualizations

All six report figures are saved in the `plots/` folder:

| # | File | Description |
|---|---|---|
| 1 | `01_average_yield_by_season.png` | Bar chart of mean yield across Kharif (5.63), Rabi (5.04), and Zaid (4.64) |
| 2 | `02_average_profit_by_season.png` | Bar chart of mean profit: Kharif (+₹178,915), Rabi (+₹87,689), Zaid (-₹24,805) |
| 3 | `03_crop_season_yield_heatmap.png` | Heatmap showing mean yield for all 8 crops across 3 seasons |
| 4 | `04_environment_vs_yield.png` | Scatter plot of Rainfall vs Yield (r = +0.0310, p = 0.0503) |
| 5 | `05_water_efficiency_by_irrigation.png` | Bar chart of water efficiency: Rainfed (7.56), Drip (6.27), Sprinkler (4.67), Flood (3.44) |
| 6 | `06_correlation_heatmap.png` | Correlation matrix of key agricultural, environmental, and financial variables |

---

## 12. Key Insights

1. Kharif recorded the highest average yield (5.63 tonnes/hectare).
2. Zaid recorded the lowest average yield (4.64 tonnes/hectare).
3. Kharif recorded the highest average profit (₹178,914.65).
4. Zaid recorded a negative average profit (-₹24,804.82), meaning an average net loss.
5. Drip irrigation recorded the highest observed average yield (6.58 t/ha) and highest profit (₹219,626.00) among the irrigation methods.
6. Rainfed recorded the highest water efficiency (7.56 t/1,000m³).
7. Flood irrigation consumed the most water (8,026.47 m³) and had the lowest water efficiency (3.44 t/1,000m³).
8. Rainfall showed the strongest linear correlation with yield among environmental variables, but it was extremely weak (r = +0.0310) and not statistically significant.
9. Seasonal yield differences were not statistically significant (ANOVA p = 0.2137), while seasonal profit differences were highly significant (p < 0.001).
10. Kharif showed the highest average disease/pest risk (54.47%) among the three seasons.

---

## 13. Data-Driven Recommendations

1. **Seasonal crop planning:** Plan farming activities based on observed seasonal profitability. Kharif showed the strongest economic outcomes in this dataset.
2. **Zaid cost review:** Review Zaid farming costs and consider suitable low-input or heat-tolerant crops, since Zaid showed an average net loss.
3. **Irrigation planning:** Consider efficient irrigation methods such as Drip where practical and affordable, as it recorded the highest observed yield and profit.
4. **Reduce flood irrigation dependence:** Reduce unnecessary dependence on Flood irrigation, which consumed the most water and had the lowest water efficiency.
5. **Pest and disease management:** Use preventive pest and disease management during higher-risk periods, particularly Kharif.
6. **Soil testing:** Use soil testing for better fertilizer decisions, since uniform fertilizer application showed near-zero correlation with yield.
7. **Combined decision-making:** Consider crop, season, environmental, and economic conditions together rather than focusing on a single factor.

---

## 14. Project Structure

```
seasonal-agriculture-performance-analysis/
├── seasonal_agriculture_performance.py
├── 01_Seasonal_Agriculture_Performance_Analysis.ipynb
├── seasonal_agriculture_performance_dataset.csv
├── plots/
│   ├── 01_average_yield_by_season.png
│   ├── 02_average_profit_by_season.png
│   ├── 03_crop_season_yield_heatmap.png
│   ├── 04_environment_vs_yield.png
│   ├── 05_water_efficiency_by_irrigation.png
│   └── 06_correlation_heatmap.png
├── README.md
└── requirements.txt
```

---

## 15. How to Run the Python Script

1. Open a terminal or command prompt in the `seasonal-agriculture-performance-analysis` folder.

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis:

   ```bash
   python seasonal_agriculture_performance.py
   ```

4. The analysis results will appear in the terminal and the six figures will be saved in the `plots/` folder.

---

## 16. How to Run the Jupyter Notebook

1. Make sure Jupyter is installed:

   ```bash
   pip install jupyter
   ```

2. Open a terminal in the `seasonal-agriculture-performance-analysis` folder and start the notebook server:

   ```bash
   jupyter notebook 01_Seasonal_Agriculture_Performance_Analysis.ipynb
   ```

3. Run all cells using **Kernel → Restart & Run All**.

The notebook contains the same analysis as the Python script, presented with Markdown explanations and inline outputs.

---

## 17. Conclusion

This project analyzed 4,000 farm records across Kharif, Rabi, and Zaid seasons. The analysis showed that Kharif recorded the highest average yield and profit, while Zaid recorded the lowest yield and an average net loss. However, the ANOVA test showed that overall pooled seasonal yield differences were not statistically significant, while seasonal profit differences were highly significant.

Drip irrigation recorded the highest observed yield and profit among the irrigation methods, while Rainfed had the highest water efficiency. Environmental variables showed very weak linear correlations with yield, meaning yield is likely influenced by a combination of factors rather than any single environmental variable.

Sugarcane recorded the highest biomass yield across all seasons, while Maize led among the food-grain crops. Kharif also showed the highest average disease/pest risk, which may require preventive management during the monsoon season.

The findings and recommendations in this project are based entirely on the patterns observed in the dataset. Since this is an observational analysis, the results show associations and patterns rather than proven cause-and-effect relationships.

---

*Project completed as part of VOIS AICTE 2026–2027 internship programme.*