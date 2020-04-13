# First run -> dupfinder.py
import pandas as pd

CSV_PATH = "./Data/Annotations/FL_Keys_Coral-export.csv"
validation_data_PATH = '/Users/mac7/Desktop/MS_Project/Data/Enhanced/Enhanced_Splitted/val/'


def list_of_images(IMGs_PATH):
    """
    Arg: JPGPATH

    Return: listOf_images for creating the xml files.

    Used also in code5,.py
    """
    import os
    listOF_imgs = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(IMGs_PATH):
        for file in f:
            if '.jpg' in file or '.png' in file:
                listOF_imgs.append(os.path.join(file))

    return listOF_imgs


LIMG = list_of_images(validation_data_PATH)
print(LIMG)

DF = pd.read_csv(CSV_PATH)
# print(DF.head())

New = DF[DF["image"] == LIMG[0].split('.')[0]+'.jpg']
# print('New:', New)
for img in LIMG[1:]:
    NewerDF = DF[DF["image"] == img.split('.')[0]+'.jpg']
    # print(NewerDF)
    NewerDF = pd.concat([New, NewerDF])

print(NewerDF)
NewerDF.to_csv('validationDF.csv')
