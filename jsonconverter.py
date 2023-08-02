import json
import csv
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    
with open('data1.csv', 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['name', 'organizers', 'email', 'keywords', 'description', 'events'])

    # Write data rows
    for item in data:
        csv_writer.writerow([item['name'], item['organizers'], item['email'], item['keywords'], item['description'], item['events']])
