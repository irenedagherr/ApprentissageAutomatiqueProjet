import csv

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
            row = [float(item) if item.replace('.', '', 1).isdigit() else item for item in row]
            data.append(row)
    return data


data_file = 'welddb.data'

data = extract_data(data_file)

with open('weld_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(headers)

    writer.writerows(data)