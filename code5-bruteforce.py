import pandas as pd

CSV_PATH = "./Data/Annotations/FL_Keys_Coral-export.csv"

THING_CLASSES = ['Past', 'Gorgonia', 'SeaRods', 'Antillo',
                 'Fish', 'Ssid', 'Orb', 'Other_Coral', 'Apalm', 'Galaxaura']
# TODO:
MoshtAzKharvar = "3D_L0215_161.jpg", "3D_L0457_89.jpg", "3D_L0457_89.jpg", "3D_L0453_283.jpg", "3D_L0457_173.jpg", "3D_L0457_173.jpg", "D_3D_L0649_425.jpg", "3L040215_169.jpg", "3D_L0457_56.jpg", "D_3D_L0649_83.jpg", "D_3D_L0649_83.jpg"
imgs_anns = pd.read_csv(CSV_PATH)

new = imgs_anns[imgs_anns['label'] == THING_CLASSES[0]].head(1)
# print(new)
for i in range(1, 10):
    newer = imgs_anns[imgs_anns['label'] == THING_CLASSES[i]].head(1)
    # print(newer)
    new = pd.concat([new, newer])

# new.to_csv('Brute_val.csv')

# TODO: -> Dictionary?
# 4 : 3D_L0457_189.jpg
# 5 :
# 6 :
# 7 :
# 8 :
# 9 :
# 10 :


def _bruteSplitter(IMG_PATH_Object_Enhanced):
    import shutil
    import os
    brutal_val_PATH = "/Users/mac7/Desktop/MS_Project/Brute_val.csv"

    SRC_PATH = IMG_PATH_Object_Enhanced
    DEST_DIR_VAL = "/Users/mac7/Desktop/MS_Project/Data/Enhanced/Enhanced_Splitted/val"

    os.chdir(SRC_PATH)
    files = [f for f in os.listdir() if os.path.isfile(f)]

    print(files)

    MoshtAzKharvar = new["image"].unique()
    valid_data_list = MoshtAzKharvar

    for vd in valid_data_list:
        valid_IMGs = SRC_PATH + '/' + vd.split(".")[0]+'.png'
        shutil.copy(valid_IMGs, DEST_DIR_VAL)


_bruteSplitter('/Users/mac7/Desktop/MS_Project/Data/Enhanced')
