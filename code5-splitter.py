# Idea from https://medium.com/@mishraishan31/data-set-split-
# It's originally to spread the cropped images.

import os  # files and dirs manipulation
import math  # split calculate
import shutil  # copy images to train, test and valid dirs
import json  # create the


def create_directories(list_Of_DirsInside, parent_dir):
    """
    Given the list of names. (list of different classes).

    Return : len(classes) subdirectory inside a parent_direcory named as Cropped_Objects.
    """
    try:
        # 10 different folder will be created inside of this 1 main folder.
        os.makedirs(parent_dir)
        # os.chmod(parent_dir, mode=777)
        for dirName in list_Of_DirsInside:
            try:
                # Create target Directory
                os.mkdir(parent_dir+'/'+dirName)
                # os.chmod(parent_dir+dirName, mode=777)

                print("Directory ", dirName,  " Created. ")
            except FileExistsError:
                print("Directory ", dirName,  " already exists!")
    except FileExistsError:
        print('\nmainDirectory Already exist!')
    print("created_dictionaries(): Finished Successfully!\n")
    return parent_dir, list_Of_DirsInside


def create_categorical_dataset(IMG_PATH, train_prop):
    """
    # Cropped_Objects.

    # function to split data of each category into trainning, validation and testing set.
    """

    def get_category_folder_list(parent_dir):
        """
        return category folder list.
        """
        os.chdir(parent_dir)
        category_list = list(filter(lambda x: os.path.isdir(x), os.listdir()))
        # for category in category_list:
        #     print(category)
        return category_list

    category_list = get_category_folder_list(IMG_PATH)
    print('\nCATEGORY_LIST:\n', category_list)

    # Define proportion of data.
    valid_prop = test_prop = (1-train_prop)/2

    for ii, cat in enumerate(category_list):
        # Used for the Cropped_Objects (Labeled with folders.)
        src_path = IMG_PATH + cat
        # print(src_path)

        dest_dir1 = IMG_PATH + 'SPLITTED_OBJECTs/'+'train/'
        dest_dir2 = IMG_PATH + 'SPLITTED_OBJECTs/'+'valid/'
        dest_dir3 = IMG_PATH + 'SPLITTED_OBJECTs/'+'test/'

        dest_dirs_list = [dest_dir1, dest_dir2, dest_dir3]
        # print(dest_dirs_list)  # Test.

        # TODO: Remove the bellow later if needed.
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
    print('\ncreate_categorical_dataset is finished. -> Congrates!')


def ImageSplitter(IMG_PATH_Object_Enhanced, train_prop):
    """
    # Given the enhanced images ( Preprocessed Images).
    # Function to split files in ONE directory into trainning, validation and testing set.
    """

    # Define proportion of data.
    valid_prop = test_prop = (1-train_prop)/2

    SRC_PATH = IMG_PATH_Object_Enhanced

    DEST_DIR1 = IMG_PATH_Object_Enhanced+'SPLITTED_OBJECTs/train/'
    DEST_DIR2 = IMG_PATH_Object_Enhanced+'SPLITTED_OBJECTs/valid/'
    DEST_DIR3 = IMG_PATH_Object_Enhanced+'SPLITTED_OBJECTs/test/'

    DEST_DIRS_LIST = [DEST_DIR1, DEST_DIR2, DEST_DIR3]
    print(DEST_DIRS_LIST)  # Test.

    os.chdir(SRC_PATH)
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
        train_path = SRC_PATH + '/' + train_data
        shutil.copy(train_path, DEST_DIR1)

    for valid_data in valid_data_list:
        valid_path = SRC_PATH + '/' + valid_data
        shutil.copy(valid_path, DEST_DIR2)

    for test_data in test_data_list:
        test_path = SRC_PATH + '/' + test_data
        shutil.copy(test_path, DEST_DIR3)


if __name__ == "__main__":

    """
    # Path Configuration _ 1
    IMG_PATH_Cropped = '/Users/mac7/Desktop/MS_Project/Data/Cropped_Objects/'
    CROPPED_OBJECTS_PATH = './Data/Cropped_Objects/'

    # Create training, validation, testing directories inside the SPLITTED_OBJECTs directory.
    parent_dir = './Data/Cropped_Objects/SPLITTED_OBJECTs/'

    parent_dir, list_Of_DirsInside = create_directories(
        parent_dir=parent_dir, list_Of_DirsInside=['test', 'train', 'valid'])
    print('parent_dir:', parent_dir, '\nlist_of_DirsInsied:', list_Of_DirsInside)

    create_categorical_dataset(IMG_PATH_Cropped, train_prop=0.5)
    """

    # """
    # Path Configuration _ 2
    IMG_PATH_Object_Enhanced = '/Users/mac7/Desktop/MS_Project/Data/Enhanced/'
    ENGANCED_IMG_PATH = './Data/Enhanced/'

    # Create training, validation, testing directories inside the SPLITTED_OBJECTs directory.
    parent_dir = './Data/Enhanced/SPLITTED_OBJECTs/'

    parent_dir, list_Of_DirsInside = create_directories(
        parent_dir=parent_dir, list_Of_DirsInside=['test', 'train', 'valid'])
    print('parent_dir:', parent_dir, '\nlist_of_DirsInsied:', list_Of_DirsInside)

    ImageSplitter(IMG_PATH_Object_Enhanced, train_prop=0.8)
    # """
