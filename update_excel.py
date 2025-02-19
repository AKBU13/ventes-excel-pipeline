import pandas as pd

# Chemin du fichier Excel
file_path = "ventes.xlsx"

# Charger le fichier Excel existant (ou en créer un nouveau s'il n'existe pas)
try:
    df = pd.read_excel(file_path)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Produit", "Ventes"])

# Ajouter de nouvelles données (exemple)
new_data = {"Date": ["2023-10-01"], "Produit": ["Produit A"], "Ventes": [150]}
new_df = pd.DataFrame(new_data)

# Fusionner les données
df = pd.concat([df, new_df], ignore_index=True)

# Sauvegarder le fichier mis à jour
df.to_excel(file_path, index=False)
print("Fichier Excel mis à jour avec succès !")