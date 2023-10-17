import pandas as pd
import dask.dataframe as dd
import numpy as np 
import time 

## Method 1 ##
beta_850k = "/data/DERI-MMH/DNA_meth/beta-vals/all_beta.csv"
start_time = time.time()

ddf = dd.read_csv(beta_850k)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Time taken to read the DataFrame using Dask: {elapsed_time:.2f} seconds")

num_rows = ddf.shape[0].compute()
num_columns = ddf.shape[1]

# Print the number of rows and columns
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)


## Method 2 ##
# Reading huge CSV with chunck
  
# time taken to read data 
start_time = time.time()
chunk = pd.read_csv(beta_850k, chunksize=1000) 
end_time = time.time()
elapsed_time1 = end_time - start_time

df = pd.concat(chunk) 
#print("With chunks: ", (e_time_chunk-s_time_chunk), "sec") 
print(f"Time taken to read the DataFrame using chunks: {elapsed_time1:.2f} seconds") 
# data 
#df.sample(10)
