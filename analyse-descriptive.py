import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def displayMissingValues(df) :
    # Calculer le nombre de valeurs manquantes par colonne
    missing_values = df.isnull().sum()

    # Créer l'histogramme
    plt.figure(figsize=(10,6))
    bars = plt.bar(missing_values.index, missing_values.values)

    # Ajouter les valeurs exactes au-dessus de chaque barre
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=5)

    # Rotation des labels de l'axe des x
    plt.xticks(rotation=45, ha='right', fontsize=6)

    # Ajouter un titre et labels des axes
    plt.title(f'Nombre de valeurs manquantes par colonne, nbreligne = {df.shape[0]}')
    plt.ylabel('Nombre de valeurs manquantes')

    # Afficher le graphique
    plt.tight_layout()  # Pour éviter que les labels soient coupés
    plt.show()

    return None

def displayMatrixCorr(df, val_manquante = None):
    # Filtrer les colonnes ayant moins de 400 valeurs manquantes
    if val_manquante == None :
        corr_matrix = df.corr()
    else :
        filtered_df = df.loc[:, df.isnull().sum() < val_manquante]
    
        # Calculer la matrice de corrélation
        corr_matrix = filtered_df.corr()
    
    # Afficher la matrice de corrélation
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    plt.title("Matrice de corrélation")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

df_raw = pd.read_csv("weld_data_raw.csv")
#print('Valeur unique de la colone "Type of weld" from df_raw : ', df_raw['Type of weld'].unique())

# Charger le fichier CSV
df = pd.read_csv("weld_data.csv")
df = df.replace(-1, np.nan)

df_without_ID = df.iloc[:, :-1]
df_new = df_without_ID.iloc[:, -5:]
df_cleaned = df_new.dropna()
print(df_cleaned.shape[0])
print(df_cleaned.isnull().sum())

#displayMatrixCorr(df_cleaned)


#print('Valeur unique de la colonne "Type of weld from df après preprocessing : ', df['Type of weld'].unique())
df_without_ID = df.iloc[:, :-1]
displayMatrixCorr(df_without_ID,50)

displayMissingValues(df)



# Trier les lignes en fonction de la colonne D dans l'ordre décroissant
df_sorted = df.sort_values(by='Yield strength (MPa)', ascending=False)

# Sélectionner les 20 premières lignes et afficher les colonnes B, C, et D
#top_20 = df_sorted[['Yield strength (MPa)', 'Ultimate tensile strength (MPa)', 'Type of weld']].head(30)
top_20 = df_sorted.head(30)

# Afficher le résultat
print(top_20)

print(df.info())

for col in df.columns:
    print(col)

n = 2

if n == 1 :
    # Parcourir les colonnes du DataFrame
    for col in df.columns:
        print(f"\nColonne: {col}")
        
        # Pourcentage de données manquantes
        missing_percentage = df[col].isnull().mean() * 100
        print(f"Pourcentage de données manquantes: {missing_percentage:.2f}%")
        
        # Valeurs uniques de la colonne
        unique_values = df[col].dropna().unique()
        print(f"Valeurs uniques: {unique_values}")
        
        # Si la colonne est numérique, afficher les statistiques
        if pd.api.types.is_numeric_dtype(df[col]):
            print("Statistiques:")
            print(f"  Max: {df[col].max()}")
            print(f"  Min: {df[col].min()}")
            print(f"  Moyenne: {df[col].mean()}")
            print(f"  Médiane: {df[col].median()}")
            print(f"  Écart-type: {df[col].std()}")
        else:
            print("Colonne non numérique, statistiques non calculées.")

else :
    # Parcourir les colonnes du DataFrame
    for col in df.columns:
        # Calcul du pourcentage de valeurs manquantes
        missing_percentage = df[col].isnull().mean() * 100
        
        # Si plus de 80% des valeurs sont manquantes, afficher les informations
        if missing_percentage > 80:
            print(f"\nColonne: {col}")
            print(f"Pourcentage de données manquantes: {missing_percentage:.2f}%")

            # Valeurs uniques et leur nombre d'apparitions
            unique_values_counts = df[col].value_counts(dropna=False)
            print("\nValeurs uniques avec leur nombre d'apparition:")
            print(unique_values_counts)

            # Si la colonne est numérique, afficher les statistiques
            if pd.api.types.is_numeric_dtype(df[col]):
                print("\nStatistiques pour les colonnes numériques:")
                print(f"  Max: {df[col].max()}")
                print(f"  Min: {df[col].min()}")
                print(f"  Moyenne: {df[col].mean()}")
                print(f"  Médiane: {df[col].median()}")
                print(f"  Écart-type: {df[col].std()}")


