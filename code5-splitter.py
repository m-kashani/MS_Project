# Idea from https://medium.com/@mishraishan31/data-set-split-ec0835a52ec6

import os  # files and dirs manipulation
import math  # split calculate
import shutil  # copy images to train, test and valid dirs
import json  # create the

# path configuration.
cropped_objects_PATH = './Data/Cropped_Objects/'
enhanced_objects_PATH = './Data/enhanced'

IMG_PATH = cropped_objects_PATH


def get_category_folder_list(parent_dir):
    """
    return category folder list.
    """
    os.chdir(parent_dir)
    category_list = list(filter(lambda x: os.path.isdir(x), os.listdir()))
    # for category in category_list:
    #     print(category)
    return category_list


# create training,validation,testing directories.
category_list = get_category_folder_list(IMG_PATH)
print(category_list)


def create_directories(list_Of_DirsInside):
    """
    given the list of names. (classes)

    Return : len(classes) subdirectory inside a parent_direcory named as Cropped_Objects.
    """
    try:
        # 10 different folder will be created inside of this 1 main folder.
        parent_dir = 'SPLITTED_OBJECTs/'
        os.makedirs(parent_dir)
        # os.chmod(parent_dir, mode=777)
        for dirName in list_Of_DirsInside:
            try:
                # Create target Directory
                os.mkdir(parent_dir+dirName)
                # os.chmod(parent_dir+dirName, mode=777)

                print("Directory ", dirName,  " Created. ")
            except FileExistsError:
                print("Directory ", dirName,  " already exists!")
    except FileExistsError:
        print('\nmainDirectory Already exist!')
    print("created_dictionaries(): Finished Successfully!\n")
    return parent_dir, list_Of_DirsInside


parent_dir, list_Of_DirsInside = create_directories(
    list_Of_DirsInside=['test', 'train', 'valid'])

# print(parent_dir)

DEST_DIR1 = '/Users/mac7/Desktop/MS_Project/Data/Cropped_Objects/SPLITTED_OBJECTs/test'
DEST_DIR2 = '/Users/mac7/Desktop/MS_Project/Data/Cropped_Objects/SPLITTED_OBJECTs/train'
DEST_DIR3 = '/Users/mac7/Desktop/MS_Project/Data/Cropped_Objects/SPLITTED_OBJECTs/valid'

DEST_DIRS_LIST = [DEST_DIR1, DEST_DIR2, DEST_DIR3]

# ------------------------------------------------------------------------------------------
# define proportion of data.
train_prop = 0.6
valid_prop = test_prop = (1-train_prop)/2
# function to split data of each category into trainning, validation and testing set.


def create_dataset():
    for ii, cat in enumerate(category_list):
        PTH = '/Users/mac7/Desktop/MS_Project/Data/Cropped_Objects/'
        src_path = PTH + '/' + cat
        dest_dir1 = PTH + parent_dir+'train/'
        dest_dir2 = PTH + parent_dir+'valid/'
        dest_dir3 = PTH + parent_dir+'test/'

        dest_dirs_list = [dest_dir1, dest_dir2, dest_dir3]
        # for dirs in dest_dirs_list:
        #     os.mkdir(dirs, 755)

        # get files' names list from respective directories.
        os.chdir(src_path)
        files = [f for f in os.listdir() if os.path.isfile(f)]

        # get training, testing and validation files count.
        train_count = math.ceil(train_prop*len(files))
        valid_count = int((len(files)-train_count)/2)
        test_count = valid_count

        # get files to segragate for train,test and validation data set.
        train_data_list = files[0: train_count]
        valid_data_list = files[train_count+1:train_count+1+valid_count]
        test_data_list = files[train_count+valid_count:]

        for train_data in train_data_list:
            train_path = src_path + '/' + train_data
            shutil.copy(train_path, dest_dir1)

        for valid_data in valid_data_list:
            valid_path = src_path + '/' + valid_data
            shutil.copy(valid_path, dest_dir2)

        for test_data in test_data_list:
            test_path = src_path + '/' + test_data
            shutil.copy(test_path, dest_dir3)


create_dataset()
print('music on!')
