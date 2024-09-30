import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("weld_data_raw.csv")

# Spécifier la colonne et la valeur à rechercher
colonne = "Sulphur concentration (weight%)"  # Remplacez par le nom de votre colonne
valeur_recherchee = "<0.002"    # Remplacez par la valeur que vous recherchez

# Compter le nombre de fois que la valeur apparaît dans la colonne
nombre_occurrences = df[colonne].value_counts().get(valeur_recherchee, 0)

print(f"La valeur '{valeur_recherchee}' apparaît {nombre_occurrences} fois dans la colonne '{colonne}'.")

# Spécifier la colonne et la valeur à rechercher
colonne2 = "Interpass temperature (deg C)"  # Remplacez par le nom de votre colonne
valeur_recherchee2 = "150-200"    # Remplacez par la valeur que vous recherchez

# Compter le nombre de fois que la valeur apparaît dans la colonne
nombre_occurrences2 = df[colonne2].value_counts().get(valeur_recherchee2, 0)

print(f"La valeur '{valeur_recherchee2}' apparaît {nombre_occurrences2} fois dans la colonne '{colonne2}'.")

