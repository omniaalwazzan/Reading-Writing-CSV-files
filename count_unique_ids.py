import pandas as pd 
import matplotlib.pyplot as plt
path = r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/DNA_methyalation/CSV/all_data_MvalSentrix_20GT.csv"

df = pd.read_csv(path)
#%%
thresh_1=0.60

filtered_ids = df[df.iloc[:, 21] <= thresh_1]['Folder'].tolist()

filtered_df = df[df['Folder'].isin(filtered_ids)]


mask = ~df['Folder'].isin(filtered_ids)

# Apply the mask to df to get the DataFrame without the filtered IDs in the 'Folder' column
filtered_df_without = df[mask]

#%%

def count_unique_ids(df):
    # Group by 'Label' and count unique 'ID's within each group
    unique_ids_per_label = df.groupby(df.iloc[:, 20])['Folder'].nunique()
    # Plotting
    plt.figure(figsize=(10, 10))
    bars = unique_ids_per_label.plot(kind='bar', color='skyblue')
    plt.title('Count of Unique IDs per Label')
    plt.xlabel('Label')
    plt.ylabel('Count of Unique IDs')
    
    # Rotate x-axis labels by 90 degrees
    plt.xticks(rotation=90)
    
    # Display the count of unique IDs on top of each bar
    for i, val in enumerate(unique_ids_per_label):
        bars.text(i, val + 0.1, str(val), ha='center')    
    plt.tight_layout()
    plt.show()
