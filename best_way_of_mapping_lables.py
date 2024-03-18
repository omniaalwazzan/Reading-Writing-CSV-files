# If we have two large data frames, merging them to map the label from one to another is nearly impossible due memory allocation issue. The best way to do it is to use a dictionary, which can run in a second

import pandas as pd 

path_2_CP = r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/AZ/CellProfiler/DrugSeq_A549_batch1_2_GW.csv"
path_2_DrugSeq_map = r"C:/Users/omnia/OneDrive - University of Jeddah/PhD progress/AZ/CellProfiler/Combined_metadata_QMUL.xlsx"

CP_df = pd.read_csv(path_2_CP)
DS_df = pd.read_excel(path_2_DrugSeq_map)
#%%
# only get important columns to map with CP data 
filter_1 = DS_df[(DS_df['treatment_duration'] == '24h') & (DS_df['cell_line'] == 'A549')]

# The df2_subset 
df2_subset = filter_1[['compound_code', 'MOA']]

compound_mapping = dict(zip(df2_subset['compound_code'], df2_subset['MOA']))
CP_df['MOA'] = CP_df['SAMPLEIDDISPLAY'].map(compound_mapping)
