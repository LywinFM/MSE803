import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("Sample_dataset.csv")

# --- Data Cleaning ---

# Convert numeric columns, coercing errors to NaN
numeric_cols = ["Age", "Net worth", "Salary"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", ""), errors="coerce")

# Drop rows where all numeric values are missing
df_clean = df.dropna(subset=numeric_cols, how="all")

# --- Compute Statistics ---

# Mean
mean_values = df_clean[numeric_cols].mean()

# Variance
variance_values = df_clean[numeric_cols].var()

# Standard Deviation
std_values = df_clean[numeric_cols].std()

# Covariance Matrix
covariance_matrix = df_clean[numeric_cols].cov()

# --- Display Results ---
print("=== MEAN ===")
print(mean_values, "\n")

print("=== VARIANCE ===")
print(variance_values, "\n")

print("=== STANDARD DEVIATION ===")
print(std_values, "\n")

print("=== COVARIANCE MATRIX ===")
print(covariance_matrix, "\n")
