import json
import csv

def load_fhir_data(file_name):
    """Load FHIR data from a JSON file and return the data"""
    with open(file_name, 'r') as f:
        fhir_data = json.load(f)
    return fhir_data

def extract_entries(fhir_data):
    """Extract the relevant information from the FHIR data and return the entries"""
    entries = []
    for entry in fhir_data['entry']:
        resource = entry['resource']
        entries.append({
            'id': resource['id'],
            'name': resource['name'][0]['given'][0],
            'gender': resource['gender'],
            'birthdate': resource['birthDate'],
        })
    return entries

def write_to_csv(entries, file_name):
    """Write the extracted information to a CSV file"""
    with open(file_name, 'w') as f:
        fieldnames = ['id', 'name', 'gender', 'birthdate']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

def fhir_to_csv(json_file, csv_file):
    """Main function to convert FHIR data to CSV file"""
    fhir_data = load_fhir_data(json_file)
    entries = extract_entries(fhir_data)
    write_to_csv(entries, csv_file)

# Usage example
fhir_to_csv('fhir_data.json', 'fhir_data.csv')
