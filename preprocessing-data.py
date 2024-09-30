import pandas as pd
import numpy as np

from statsmodels.imputation import mice
import statsmodels.api as sm

df = pd.read_csv('weld_data_raw.csv')
df = df.replace("N", np.nan)


print("Number of rows:", len(df)) #nombre de lignes


print("Number of columns:", len(df.columns)) #nombres de colonnes


total_cells = len(df) * len(df.columns) # nombre total de cellules
print("Total number of cells:", total_cells)

count_missing = df.isnull().sum().sum()
print("Number of cells containing missing values ('N'):", count_missing)


percentage_missing = (count_missing / total_cells) * 100
print(f"Percentage of cells containing missing values ('N'): {percentage_missing:.2f}%")

#################################

# Visualize missing data patterns
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Data Pattern")
plt.show()


import missingno as msno
import matplotlib.pyplot as plt

# Visualize the missing data pattern
msno.matrix(df)
plt.title("Missing Data Pattern Visualization")
plt.show()




# Nombre de valeurs manquantes par colonne
missing_per_column = df.isnull().sum()
print("\nNumber of missing values per column:")
print(missing_per_column)

# Total de données par colonne (c'est-à-dire nombre total de cellules non manquantes)
total_data_per_column = df.notnull().sum()
print("\nTotal number of data per column:")
print(total_data_per_column)

# Afficher le pourcentage de valeurs manquantes par colonne
percentage_missing_per_column = (missing_per_column / len(df)) * 100
print("\nPercentage of missing values per column:")
print(percentage_missing_per_column)