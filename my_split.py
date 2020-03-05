# -*- coding: utf-8 -*-
"""
Given the JPEG images, We create set of text files for train.txt, test.txt and val.txt
Solution (1) -> the Github idea from BCCD.
To-Do -> Solution (2) -> sklean.model_selection.train_test_split(*array, **options)
"""

import os
import argparse as ap
import random
import math

BCCD_Path = "./Data/vott-csv-export/JPGImages/" #chance
Out_Path = "./Data/ImageSets/Main/" #change

# https://docs.python.org/3/library/argparse.html

if __name__ == "__main__":
    # Argument Parser
    parser = ap.ArgumentParser()
    parser.add_argument("--images", help="Path to images",
                        default=BCCD_Path)
    parser.add_argument("--output", help="Path to output directory",
                        default=Out_Path)
    args = vars(parser.parse_args())

    images_path = args["images"]
    output_dir = args["output"]

    trainval_rate = 0.9 # 10% validation.
    train_rate = 0.8    # Completely train.

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    images_names = os.listdir(images_path)
    images_list = []
    for img in images_names:
        images_list.append(img.split('.')[0])
    random.shuffle(images_list)

    annotation_num = len(images_list) #400

    trainval_num = int(math.ceil(trainval_rate * annotation_num)) #360
    train_num = int(math.ceil(trainval_num * train_rate)) # 320
    trainval = images_list[0:trainval_num] # 0 to 320

#------------------------------------------------------------------
    test = images_list[trainval_num:] # 320 to 360
    train = trainval[0:train_num] # 0 to 320 
    val = trainval[train_num:trainval_num] # 320 to 360
#------------------------------------------------------------------

    trainval = sorted(trainval)
    train = sorted(train)
    val = sorted(val)
    test = sorted(test)

    fout = open(os.path.join(output_dir, "trainval.txt"), 'w')
    for line in trainval:
        fout.write(line + "\n")
    fout.close()
    fout = open(os.path.join(output_dir, "train.txt"), 'w')
    for line in train:
        fout.write(line + "\n")
    fout.close()
    fout = open(os.path.join(output_dir, "val.txt"), 'w')
    for line in val:
        fout.write(line + "\n")
    fout.close()
    fout = open(os.path.join(output_dir, "test.txt"), 'w')
    for line in test:
        fout.write(line + "\n")
    fout.close()
    
    print(annotation_num, len(trainval), len(test), len(train), len(val))