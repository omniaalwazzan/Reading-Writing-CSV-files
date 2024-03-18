import os
import pandas as pd
import zipfile
import shutil

zip_file_path = r"D:\AstraZeneca\CellProfiler\20230919_DrugSeq_MCF7_repeat_batch3_GW.zip"

# Extract the contents of the zip file to a temporary folder
extract_folder = 'temp_extract_folder'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

folder_path = os.path.join(extract_folder, '20230919_DrugSeq_MCF7_repeat_batch3_GW')
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv') and 'Aggregated' in file]

# concatenate CSV files into a single DataFrame
dfs = []
for file in csv_files:
    df = pd.read_csv(os.path.join(folder_path, file))
    dfs.append(df)

# Concatenate all DataFrames into one
merged_df = pd.concat(dfs, ignore_index=True)

merged_df.to_csv(r'C:\Users\Omnia\Desktop\Phd\AZ\CellProfiler\20230919_DrugSeq_MCF7_repeat_batch3_GW.csv', index=False)

# Clean up: Remove the temporary extraction folder
shutil.rmtree(extract_folder)
