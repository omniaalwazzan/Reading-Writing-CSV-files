import os
import cv2
import pandas as pd

### read the csv file###
DF = pd.read_csv(r".\Patches.csv")
#print(DF.head(5))
idx = 1
### extraxt letters from cols and assign them to a new col ###
new_col = [x[:12] for x in DF['TCGA_ID']]  # can be a list, a Series, an array or a scalar   
DF.insert(loc=idx, column='ID', value=new_col)
## save it to a new dataframe
DF.to_csv(r".\Patches_with_id.csv")
