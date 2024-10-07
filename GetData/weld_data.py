import csv
import re  
from pathlib import Path

weld_type_mapping = {
    "MMA": 0,
    "SA": 1,
    "FCA": 2,
    "TSA": 3,
    "ShMA": 4,
    "NGSAW": 5,
    "NGGMA": 6,
    "GMAA": 7,
    "GTAA": 8,
    "SAA": 9
}

headers = [
    "Carbon concentration (weight%)", "Silicon concentration (weight%)",
    "Manganese concentration (weight%)", "Sulphur concentration (weight%)",
    "Phosphorus concentration (weight%)", "Nickel concentration (weight%)",
    "Chromium concentration (weight%)", "Molybdenum concentration (weight%)",
    "Vanadium concentration (weight%)", "Copper concentration (weight%)",
    "Cobalt concentration (weight%)", "Tungsten concentration (weight%)",
    "Oxygen concentration (ppm)", "Titanium concentration (ppm)",
    "Nitrogen concentration (ppm)", "Aluminium concentration (ppm)",
    "Boron concentration (ppm)", "Niobium concentration (ppm)",
    "Tin concentration (ppm)", "Arsenic concentration (ppm)",
    "Antimony concentration (ppm)", "Current (A)", "Voltage (V)",
    "AC or DC", "Electrode positive or negative", "Heat input (kJ/mm)",
    "Interpass temperature (deg C)", "Type of weld",
    "Post weld heat treatment temperature (deg C)", "Post weld heat treatment time (hours)",
    "Yield strength (MPa)", "Ultimate tensile strength (MPa)",
    "Elongation (%)", "Reduction of Area (%)",
    "Charpy temperature (deg C)", "Charpy impact toughness (J)",
    "Hardness (kg/mm2)", "50 % FATT",
    "Primary ferrite in microstructure (%)", "Ferrite with second phase (%)",
    "Acicular ferrite (%)", "Martensite (%)",
    "Ferrite with carbide aggregate (%)", "Weld ID"
]

def extract_data(data_file):
    data = []
    with open(data_file, 'r') as file:
        for line in file:
            row = line.strip().split()
            # Convert numeric fields where applicable and replace 'N' with -1
            row = [
                float(item) if item.replace('.', '', 1).isdigit() else -1 if item == 'N' else item 
                for item in row
            ]

            # Calculate midpoint for interpass temperature range
            interpass_temp = row[26]
            if isinstance(interpass_temp, str) and '-' in interpass_temp:
                lower_bound, upper_bound = map(float, interpass_temp.split('-'))
                row[26] = (lower_bound + upper_bound) / 2  # Replace with midpoint

            # Process concentrations prefixed with '<'
            for index in [3, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 38]:  # Molybdenum, Aluminium, Boron, Niobium
                if isinstance(row[index], str) and row[index].startswith('<'):
                    row[index] = float(row[index][1:])

            # Transform Nitrogen concentration (ppm) for values like '66totndres'
            nitrogen_concentration = row[14]  
            if isinstance(nitrogen_concentration, str):
                match = re.match(r'(\d+)', nitrogen_concentration)
                if match:
                    nitrogen_concentration = float(match.group(1))
                else:
                    nitrogen_concentration = -1  
            row[14] = nitrogen_concentration 

            weld_type = row[27]
            if weld_type in weld_type_mapping:
                row[27] = weld_type_mapping[weld_type]  # Replace with mapped value
            else:
                continue  

            # Transform Hardness (kg/mm²) for values like '144(Hv30)' and '224Hv10'
            hardness = row[36]  
            if isinstance(hardness, str):
                match = re.match(r'(\d+)', hardness)
                if match:
                    hardness = float(match.group(1))
                else:
                    hardness = -1 
            row[36] = hardness  

            # Handle "Electrode positive or negative" column (index 24)
            if row[24] == '+':
                row[24] = 1
            elif row[24] == '-':
                row[24] = 2
            else :
                row[24] = 0
            
            # Handle "AC or DC" column (index 23)
            if row[23] == 'AC':
                row[23] = 1  # Replace "AC" with 1
            elif row[23] == 'DC':
                row[23] = 0  # Replace "DC" with 0
            
            if row[24] != '' and len(row) == len(headers):  
                data.append(row)

    return data

script_dir = Path(__file__).parent  # Obtenir le répertoire du script
data_file = script_dir.parent / 'InformationPublique-Donnees' / 'welddb.data'  

# Extract the data
data = extract_data(data_file)

# Write the data to a CSV file
with open('weld_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the headers
    writer.writerow(headers)

    # Write the data rows
    writer.writerows(data)

