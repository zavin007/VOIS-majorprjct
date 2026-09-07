# =============================================================================
# Seasonal Agriculture Performance Analysis
# =============================================================================
# A beginner-friendly data analysis and visualization project.
# VOIS AICTE 2026-2027 Major Project
#
# Technologies: Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy
# =============================================================================


# ── 1. Import Libraries ──────────────────────────────────────────────────────

import os

import pandas as pd
import numpy as np

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr, f_oneway


# ── 2. Create 'plots' Folder ─────────────────────────────────────────────────

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLOTS_DIR = os.path.join(BASE_DIR, "plots")

os.makedirs(PLOTS_DIR, exist_ok=True)


# ── 3. Load the Dataset ──────────────────────────────────────────────────────

CSV_PATH = os.path.join(
    BASE_DIR,
    "seasonal_agriculture_performance_dataset.csv"
)

df = pd.read_csv(CSV_PATH)


print("=" * 75)
print("       SEASONAL AGRICULTURE PERFORMANCE ANALYSIS")
print("=" * 75)


# ── 4. Basic Dataset Information ─────────────────────────────────────────────

print("\n" + "=" * 75)
print("                    DATASET INFORMATION")
print("=" * 75)

print("\n[INFO] Dataset Shape:", df.shape)

print("\n[INFO] Column Names:")
for column in df.columns:
    print(" ", column)

print("\n[INFO] First 5 Rows:")
print(df.head())

print("\n[INFO] Data Types:")
print(df.dtypes)

print("\n[INFO] Missing Values:")
print(df.isnull().sum())

print("\n[INFO] Total Missing Values:",
      df.isnull().sum().sum())

print("\n[INFO] Duplicate Rows:",
      df.duplicated().sum())


# ── 5. Data Cleaning ─────────────────────────────────────────────────────────

print("\n" + "=" * 75)
print("                    DATA CLEANING")
print("=" * 75)

duplicates_before = df.duplicated().sum()

if duplicates_before > 0:
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"\n[CLEAN] Removed {duplicates_before} duplicate rows.")
else:
    print("\n[OK] No duplicate rows found.")

# Columns containing missing numerical values
imputation_columns = [
    "Rainfall_mm",
    "Soil_Moisture_pct",
    "Yield_Tonnes_Ha"
]

print("\n[INFO] Missing values before imputation:")

for column in imputation_columns:
    missing_count = df[column].isnull().sum()
    median_value = df[column].median()

    print(
        f"  {column}: {missing_count} missing "
        f"| Median used: {median_value:.3f}"
    )

    df[column] = df[column].fillna(median_value)

print("\n[INFO] Missing values after cleaning:")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\n[INFO] Final Dataset Shape:", df.shape)

print("\n[OK] Data cleaning completed.")


# ── 6. Seasonal Performance Analysis ─────────────────────────────────────────

print("\n" + "=" * 75)
print("                 SEASONAL PERFORMANCE ANALYSIS")
print("=" * 75)

seasonal_summary = df.groupby("Season").agg(
    Mean_Yield=("Yield_Tonnes_Ha", "mean"),
    Mean_Production=("Production_Tonnes", "mean"),
    Mean_Revenue=("Revenue_INR", "mean"),
    Mean_Total_Cost=("Total_Cost_INR", "mean"),
    Mean_Profit=("Profit_INR", "mean")
).round(2)

print("\nSeasonal Performance Summary:")
print(seasonal_summary)


# Separate yield and profit summaries

seasonal_yield = (
    df.groupby("Season")["Yield_Tonnes_Ha"]
    .mean()
    .sort_values(ascending=False)
)

seasonal_profit = (
    df.groupby("Season")["Profit_INR"]
    .mean()
    .sort_values(ascending=False)
)


print("\nAverage Yield by Season:")
for season, value in seasonal_yield.items():
    print(f"  {season}: {value:.2f} tonnes/hectare")


print("\nAverage Profit by Season:")
for season, value in seasonal_profit.items():
    print(f"  {season}: Rs.{value:,.2f}")


# ── 7. Environmental Conditions by Season ────────────────────────────────────

print("\n" + "=" * 75)
print("                 ENVIRONMENTAL CONDITIONS")
print("=" * 75)

environmental_summary = df.groupby("Season").agg(
    Rainfall=("Rainfall_mm", "mean"),
    Temperature=("Avg_Temperature_C", "mean"),
    Humidity=("Humidity_pct", "mean"),
    Sunlight=("Sunlight_Hours_Day", "mean"),
    Soil_Moisture=("Soil_Moisture_pct", "mean"),
    Disease_Pest_Risk=("Disease_Pest_Risk_pct", "mean")
).round(2)

print("\nEnvironmental Summary:")
print(environmental_summary)


# ── 8. Crop × Season Analysis ────────────────────────────────────────────────

print("\n" + "=" * 75)
print("                 CROP × SEASON ANALYSIS")
print("=" * 75)

crop_season_yield = pd.pivot_table(
    df,
    values="Yield_Tonnes_Ha",
    index="Crop",
    columns="Season",
    aggfunc="mean"
).round(2)

print("\nAverage Yield by Crop and Season:")
print(crop_season_yield)


# ── 9. Irrigation Analysis ───────────────────────────────────────────────────

print("\n" + "=" * 75)
print("                 IRRIGATION ANALYSIS")
print("=" * 75)

irrigation_summary = df.groupby("Irrigation_Method").agg(
    Mean_Yield=("Yield_Tonnes_Ha", "mean"),
    Mean_Profit=("Profit_INR", "mean"),
    Mean_Water_Used=("Water_Used_m3", "mean"),
    Mean_Water_Efficiency=(
        "Water_Efficiency_t_per_1000m3",
        "mean"
    )
).round(2)

print("\nIrrigation Performance Summary:")
print(irrigation_summary)


# ── 10. Environmental Correlation Analysis ───────────────────────────────────

print("\n" + "=" * 75)
print("              ENVIRONMENT vs YIELD CORRELATION")
print("=" * 75)

environmental_variables = [
    "Rainfall_mm",
    "Avg_Temperature_C",
    "Humidity_pct",
    "Sunlight_Hours_Day",
    "Soil_Moisture_pct"
]

correlation_results = []

for column in environmental_variables:

    r, p = pearsonr(
        df[column],
        df["Yield_Tonnes_Ha"]
    )

    correlation_results.append(
        {
            "Variable": column,
            "Correlation": r,
            "P_Value": p
        }
    )

    print(
        f"{column}: "
        f"r = {r:.4f}, "
        f"p = {p:.4f}"
    )


correlation_results_df = pd.DataFrame(correlation_results)

strongest_environmental = (
    correlation_results_df
    .iloc[
        correlation_results_df["Correlation"]
        .abs()
        .argmax()
    ]
)

print(
    "\n[RESULT] Strongest environmental relationship examined:"
)

print(
    f"{strongest_environmental['Variable']} "
    f"(r = {strongest_environmental['Correlation']:.4f}, "
    f"p = {strongest_environmental['P_Value']:.4f})"
)


# ── 11. ANOVA: Yield Across Seasons ──────────────────────────────────────────

print("\n" + "=" * 75)
print("             ANOVA: YIELD ACROSS SEASONS")
print("=" * 75)

kharif_yield = df.loc[
    df["Season"] == "Kharif",
    "Yield_Tonnes_Ha"
]

rabi_yield = df.loc[
    df["Season"] == "Rabi",
    "Yield_Tonnes_Ha"
]

zaid_yield = df.loc[
    df["Season"] == "Zaid",
    "Yield_Tonnes_Ha"
]

yield_f, yield_p = f_oneway(
    kharif_yield,
    rabi_yield,
    zaid_yield
)

print(f"\nF-statistic = {yield_f:.4f}")
print(f"p-value = {yield_p:.4f}")

if yield_p < 0.05:
    print(
        "[RESULT] Seasonal yield differences are "
        "statistically significant."
    )
else:
    print(
        "[RESULT] Seasonal yield differences are "
        "not statistically significant at the 5% level."
    )


# ── 12. ANOVA: Profit Across Seasons ─────────────────────────────────────────

print("\n" + "=" * 75)
print("             ANOVA: PROFIT ACROSS SEASONS")
print("=" * 75)

kharif_profit = df.loc[
    df["Season"] == "Kharif",
    "Profit_INR"
]

rabi_profit = df.loc[
    df["Season"] == "Rabi",
    "Profit_INR"
]

zaid_profit = df.loc[
    df["Season"] == "Zaid",
    "Profit_INR"
]

profit_f, profit_p = f_oneway(
    kharif_profit,
    rabi_profit,
    zaid_profit
)

print(f"\nF-statistic = {profit_f:.4f}")
print(f"p-value = {profit_p:.4e}")

if profit_p < 0.05:
    print(
        "[RESULT] Seasonal differences in profit are "
        "statistically significant."
    )
else:
    print(
        "[RESULT] Seasonal profit differences are "
        "not statistically significant."
    )


# ── 13. Overall Correlation Analysis ─────────────────────────────────────────

print("\n" + "=" * 75)
print("                 CORRELATION ANALYSIS")
print("=" * 75)

correlation_columns = [
    "Rainfall_mm",
    "Avg_Temperature_C",
    "Humidity_pct",
    "Sunlight_Hours_Day",
    "Soil_Moisture_pct",
    "Nitrogen_kg_ha",
    "Phosphorus_kg_ha",
    "Potassium_kg_ha",
    "Fertilizer_kg_ha",
    "Pesticide_Litre_ha",
    "Yield_Tonnes_Ha",
    "Production_Tonnes",
    "Revenue_INR",
    "Total_Cost_INR",
    "Profit_INR",
    "Water_Used_m3",
    "Water_Efficiency_t_per_1000m3"
]

correlation_matrix = df[correlation_columns].corr()

print("\nCorrelation matrix calculated successfully.")


# ── 14. Generate Final Project Figures ────────────────────────────────────────

print("\n" + "=" * 75)
print("                  GENERATING FINAL PLOTS")
print("=" * 75)


# Helper function

def save_plot(fig, filename):
    """Save a plot in the project's plots folder."""
    
    path = os.path.join(
        PLOTS_DIR,
        filename
    )

    fig.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"[OK] Saved: plots/{filename}")
# ─────────────────────────────────────────────
# 14. ADDITIONAL STUDENT-DRIVEN ANALYSIS
# ─────────────────────────────────────────────

print("\n" + "=" * 70)
print("ADDITIONAL STUDENT-DRIVEN ANALYSIS")
print("=" * 70)


# -------------------------------------------------
# Analysis 1: Profit Margin by Season
# -------------------------------------------------

print("\n1. PROFIT MARGIN BY SEASON")

print("\nChecking Revenue, Cost and Profit relationship:")

print(
    df[["Total_Cost_INR", "Revenue_INR", "Profit_INR"]]
    .head(10)
)

print("\nCalculated Profit = Revenue - Cost:")

df["Calculated_Profit"] = (
    df["Revenue_INR"] - df["Total_Cost_INR"]
)

print(
    df[
        ["Total_Cost_INR", "Revenue_INR",
         "Profit_INR", "Calculated_Profit"]
    ].head(10)
)

print("\nDifference between recorded and calculated profit:")

df["Profit_Difference"] = (
    df["Profit_INR"] - df["Calculated_Profit"]
)

print(df["Profit_Difference"].describe())

# Profit Margin = (Profit / Revenue) × 100
df["Profit_Margin_pct"] = np.where(
    df["Revenue_INR"] != 0,
    (df["Profit_INR"] / df["Revenue_INR"]) * 100,
    np.nan
)

profit_margin_by_season = (
    df.groupby("Season")["Profit_Margin_pct"]
    .mean()
    .reindex(["Kharif", "Rabi", "Zaid"])
)

print("\nAverage Profit Margin by Season:")
print(profit_margin_by_season.round(2))

best_margin_season = profit_margin_by_season.idxmax()
best_margin_value = profit_margin_by_season.max()

print(
    f"\nHighest average profit margin: "
    f"{best_margin_season} ({best_margin_value:.2f}%)"
)


# -------------------------------------------------
# Analysis 2: Water Efficiency vs Profit
# -------------------------------------------------

print("\n2. WATER EFFICIENCY VS PROFIT")

water_efficiency = df["Water_Efficiency_t_per_1000m3"]
profit = df["Profit_INR"]

efficiency_profit_r, efficiency_profit_p = pearsonr(
    water_efficiency,
    profit
)

print(
    f"Pearson correlation between water efficiency "
    f"and profit: r = {efficiency_profit_r:.4f}"
)

print(
    f"P-value: {efficiency_profit_p:.4f}"
)

if efficiency_profit_p < 0.05:
    print(
        "The relationship is statistically significant "
        "at the 5% level."
    )
else:
    print(
        "The relationship is not statistically significant "
        "at the 5% level."
    )


# -------------------------------------------------
# Analysis 3: Disease/Pest Risk by Crop and Season
# -------------------------------------------------

print("\n3. DISEASE/PEST RISK BY CROP AND SEASON")

disease_crop_season = pd.pivot_table(
    df,
    values="Disease_Pest_Risk_pct",
    index="Crop",
    columns="Season",
    aggfunc="mean"
)

disease_crop_season = disease_crop_season[
    ["Kharif", "Rabi", "Zaid"]
]

print("\nAverage Disease/Pest Risk (%):")
print(disease_crop_season.round(2))

# Find the crop-season combination with the highest risk
highest_risk_crop = None
highest_risk_season = None
highest_risk_value = -np.inf

for crop in disease_crop_season.index:
    for season in disease_crop_season.columns:
        value = disease_crop_season.loc[crop, season]

        if pd.notna(value) and value > highest_risk_value:
            highest_risk_value = value
            highest_risk_crop = crop
            highest_risk_season = season

print(
    f"\nHighest recorded disease/pest risk: "
    f"{highest_risk_crop} during {highest_risk_season} "
    f"({highest_risk_value:.2f}%)"
)


print("\nAdditional analysis completed successfully.")


# ── Plot 1: Average Yield by Season ───────────────────────────────────────────

fig, ax = plt.subplots(figsize=(9, 6))

season_order = ["Kharif", "Rabi", "Zaid"]

yield_values = (
    df.groupby("Season")["Yield_Tonnes_Ha"]
    .mean()
    .reindex(season_order)
)

yield_values.plot(
    kind="bar",
    ax=ax,
    edgecolor="black"
)

ax.set_title("Average Agricultural Yield by Season")
ax.set_xlabel("Season")
ax.set_ylabel("Average Yield (Tonnes/Hectare)")
ax.tick_params(axis="x", rotation=0)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

save_plot(
    fig,
    "01_average_yield_by_season.png"
)


# ── Plot 2: Average Profit by Season ─────────────────────────────────────────

fig, ax = plt.subplots(figsize=(9, 6))

profit_values = (
    df.groupby("Season")["Profit_INR"]
    .mean()
    .reindex(season_order)
)

profit_values.plot(
    kind="bar",
    ax=ax,
    edgecolor="black"
)

ax.set_title("Average Farm Profit by Season")
ax.set_xlabel("Season")
ax.set_ylabel("Average Profit (INR)")
ax.tick_params(axis="x", rotation=0)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"Rs.{bar.get_height():,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

save_plot(
    fig,
    "02_average_profit_by_season.png"
)


# ── Plot 3: Crop × Season Yield Heatmap ───────────────────────────────────────

fig, ax = plt.subplots(figsize=(9, 7))

sns.heatmap(
    crop_season_yield,
    annot=True,
    fmt=".2f",
    cmap="YlGnBu",
    linewidths=0.5,
    ax=ax
)

ax.set_title("Average Crop Yield Across Seasons")
ax.set_xlabel("Season")
ax.set_ylabel("Crop")

plt.tight_layout()

save_plot(
    fig,
    "03_crop_season_yield_heatmap.png"
)


# ── Plot 4: Rainfall vs Yield ─────────────────────────────────────────────────

r, p = pearsonr(
    df["Rainfall_mm"],
    df["Yield_Tonnes_Ha"]
)

fig, ax = plt.subplots(figsize=(9, 6))

sns.regplot(
    data=df,
    x="Rainfall_mm",
    y="Yield_Tonnes_Ha",
    scatter_kws={"alpha": 0.35},
    line_kws={"linewidth": 2},
    ax=ax
)

ax.set_title(
    f"Rainfall vs Agricultural Yield\n"
    f"Pearson r = {r:.4f}, p = {p:.4f}"
)

ax.set_xlabel("Rainfall (mm)")
ax.set_ylabel("Yield (Tonnes/Hectare)")

plt.tight_layout()

save_plot(
    fig,
    "04_environment_vs_yield.png"
)


# ── Plot 5: Water Efficiency by Irrigation Method ────────────────────────────

fig, ax = plt.subplots(figsize=(9, 6))

water_efficiency = (
    df.groupby("Irrigation_Method")
    ["Water_Efficiency_t_per_1000m3"]
    .mean()
    .sort_values(ascending=False)
)

water_efficiency.plot(
    kind="bar",
    ax=ax,
    edgecolor="black"
)

ax.set_title(
    "Average Water Efficiency by Irrigation Method"
)

ax.set_xlabel("Irrigation Method")
ax.set_ylabel(
    "Water Efficiency (Tonnes / 1,000 m³)"
)

ax.tick_params(axis="x", rotation=0)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

save_plot(
    fig,
    "05_water_efficiency_by_irrigation.png"
)


# ── Plot 6: Correlation Heatmap ──────────────────────────────────────────────

fig, ax = plt.subplots(
    figsize=(14, 11)
)

sns.heatmap(
    correlation_matrix,
    cmap="coolwarm",
    center=0,
    linewidths=0.4,
    ax=ax
)

ax.set_title(
    "Correlation Heatmap of Key Agricultural Variables"
)

plt.tight_layout()

save_plot(
    fig,
    "06_correlation_heatmap.png"
)


# ── 15. Key Insights ─────────────────────────────────────────────────────────

print("\n" + "=" * 75)
print("                         KEY INSIGHTS")
print("=" * 75)

print(
    "\n1. Kharif recorded the highest average yield "
    "(5.63 tonnes/hectare)."
)

print(
    "2. Kharif recorded the highest average profit "
    "(Rs.178,914.65)."
)

print(
    "3. Zaid recorded the lowest average yield "
    "(4.64 tonnes/hectare)."
)

print(
    "4. Zaid recorded an average net loss of "
    "Rs.24,804.82 per farm."
)

print(
    "5. Drip irrigation recorded the highest average "
    "yield and profit among the irrigation methods."
)

print(
    "6. Rainfall had the strongest linear relationship "
    "with yield among the environmental variables tested, "
    "but the relationship was extremely weak."
)

print(
    "7. Seasonal yield differences were not statistically "
    "significant according to the ANOVA test."
)

print(
    "8. Seasonal profit differences were highly "
    "statistically significant."
)

print(
    "9. Sugarcane recorded the highest biomass yield "
    "across the crop-season combinations."
)

print(
    "10. Kharif showed the highest average disease and "
    "pest risk among the three seasons."
)


# ── 16. Recommendations ──────────────────────────────────────────────────────

print("\n" + "=" * 75)
print("                    RECOMMENDATIONS")
print("=" * 75)

recommendations = [
    "Plan more profitable farming activities during Kharif "
    "based on the observed results.",

    "Review Zaid farming costs and consider low-input or "
    "heat-tolerant crops where suitable.",

    "Consider efficient irrigation methods such as Drip "
    "where practical and affordable.",

    "Reduce unnecessary dependence on flood irrigation "
    "to improve water efficiency.",

    "Use preventive pest and disease management during "
    "Kharif.",

    "Use soil testing to make fertilizer application more "
    "suitable for individual farms.",

    "Consider crop and sowing decisions together with "
    "local environmental and economic conditions."
]

for number, recommendation in enumerate(
    recommendations,
    start=1
):
    print(f"{number}. {recommendation}")


# ── 17. Final Message ────────────────────────────────────────────────────────

print("\n" + "=" * 75)
print("                 ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 75)

print(
    "\nAll six final project figures have been saved "
    "in the 'plots' folder."
)

print("\nProject analysis is complete.")