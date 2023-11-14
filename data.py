from pathlib import Path
import pandas as pd
import glob
import os
import math

df = pd.read_csv("HAM10000_metadata.csv")
# print(df["dx"].unique())
classes = {
    "nv": "melanocytic nevi",
    "mel": "melanoma",
    "bkl": "benign keratosis-like lesions",
    "bcc": "basal cell carcinoma",
    "vasc": "pyogenic granulomas and hemorrhage",
    "akiec": "Actinic keratoses and intraepithelial carcinomae",
    "df": "dermatofibroma",
}
# image_path = Path("data/Ham10000")
images_path = glob.glob("data/Ham10000/*.jpg")
image_index = [image[14:26] for image in images_path]
# print(images_path[0],image_index[0])
image_id_list = list(df["image_id"])
class_list = list(df["dx"])
# print(images_path[image_index.index(image_id_list[0])], image_id_list[0])
image_number = 10015
for i in range(image_number):
    if i < math.floor((image_number*0.7)):
        os.rename(images_path[image_index.index(image_id_list[i])], "data/train/"+classes[class_list[i]]+"/"+images_path[image_index.index(image_id_list[i])][14:30])
    else:
       os.rename(images_path[image_index.index(image_id_list[i])], "data/test/"+classes[class_list[i]]+"/"+images_path[image_index.index(image_id_list[i])][14:30]) 
