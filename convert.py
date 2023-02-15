import os
import json
import csv
import yaml
import xml.etree.ElementTree as ET
from tkinter import filedialog, Tk

# Prompt the user to select the input file using a file dialog
root = Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=(
    ("CSV files", "*.csv"), ("JSON files", "*.json"), ("XML files", "*.xml"), ("YAML files", "*.yaml")))

# Read the input file and determine its format based on the file extension
_, file_extension = os.path.splitext(input_file_path)
if file_extension == ".csv":
    with open(input_file_path, 'r') as f:
        data = list(csv.DictReader(f))
elif file_extension == ".json":
    with open(input_file_path, 'r') as f:
        data = json.load(f)
elif file_extension == ".xml":
    tree = ET.parse(input_file_path)
    root = tree.getroot()
    data = []
    for child in root:
        data.append(child.attrib)
elif file_extension == ".yaml":
    with open(input_file_path, 'r') as f:
        data = yaml.safe_load(f)

# Prompt the user to select the output format
output_format = input("Enter the output format (csv, json, xml, or yaml): ")

# Convert the data to the selected output format
if output_format == "csv":
    _, file_extension = os.path.splitext(input_file_path)
    output_file_path = os.path.splitext(input_file_path)[0] + ".csv"
    with open(output_file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)
elif output_format == "json":
    _, file_extension = os.path.splitext(input_file_path)
    output_file_path = os.path.splitext(input_file_path)[0] + ".json"
    with open(output_file_path, 'w') as f:
        json.dump(data, f, indent=4)
elif output_format == "xml":
    _, file_extension = os.path.splitext(input_file_path)
    output_file_path = os.path.splitext(input_file_path)[0] + ".xml"
    root = ET.Element("data")
    for row in data:
        child = ET.SubElement(root, "row")
        for key, value in row.items():
            child.set(key, value)
    tree = ET.ElementTree(root)
    tree.write(output_file_path)
elif output_format == "yaml":
    _, file_extension = os.path.splitext(input_file_path)
    output_file_path = os.path.splitext(input_file_path)[0] + ".yaml"
    with open(output_file_path, 'w') as f:
        yaml.dump(data, f)
else:
    print("Invalid output format")

print(f"Converted {input_file_path} to {output_file_path}")
