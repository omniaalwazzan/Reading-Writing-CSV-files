import os
import cv2
import pandas as pd
import shutil
import numpy as np
from pathlib import Path
from PIL import Image

# This code helps when creating image dataset, labelled by filename
# Thd code will take file names from one directory that match those in CSV and move them to another directory

TRAIN_DF = pd.read_csv(r"..\Test_Grade4.csv") # csv file contains image names and labels 
PATCHES_PATH = r"..\TEST_Patches" # image folder 

IMG_DIR=os.listdir(PATCHES_PATH) 

Dist_PATH=r"..\4" # lable of the images


#Training Split
for file in TRAIN_DF['Test_ID']:
    for name in IMG_DIR:
        if name.startswith(file):
            sourc = os.path.join(PATCHES_PATH,name )
            distination = os.path.join(Dist_PATH, name)
            #shutil.move(sourc, distination)
