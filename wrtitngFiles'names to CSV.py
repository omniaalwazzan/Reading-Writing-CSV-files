# To write image names into a csv file
Val_IMG_DIR = '../data/Validation_Patches/'
PATCH_PATH = '../data/ValPatch.csv' # empty csv file(output)
with open(PATCH_PATH, 'w') as f: # this will open the csv file and start writng names in it
    for img_name in os.listdir(Val_IMG_DIR):
        img_array = cv2.imread(os.path.join(Val_IMG_DIR, img_name)) 
        f.write(img_name + "\n")
