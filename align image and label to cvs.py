

import csv
import os
# Define the list of image names
image_names = os.listdir(r"C:\Users\omnia\OneDrive - University of Jeddah\clustring\animals\animals\cat_pan_dog")
# Create a list of tuples with image names and labels
data = []
for name in image_names:
    label = 0  # Default label is 0 (cat)
    if 'panda' in name:
        label = 1
    elif 'dog' in name:
        label = 2
    data.append((name, label))

# Define the CSV file path
csv_file = 'image_data.csv'

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Image Name', 'Label'])
    writer.writerows(data)

print(f"CSV file '{csv_file}' has been created successfully.")
