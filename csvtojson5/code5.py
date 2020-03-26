# .csv to .json on 5 images creating the binary mask for each image and then using the pytococo.
# Cropper and Saver -> Do it + Function.

# Libraries and initial variables.
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

CSV_PATH = "../Data/Annotations/FL_Keys_Coral-export.csv"
JPGPATH = '../Data/vott-csv-export/JPGImages/'


def list_of_images(JPGPATH):
    """
    Arg: JPGPATH

    Return: listOf_images for cropper() function.

    Kinda got helped from.
    https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/
    """
    listOF_imgs = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(JPGPATH):
        for file in f:
            if '.jpg' in file:
                listOF_imgs.append(os.path.join(file))

    return listOF_imgs


def create_directories(list_Of_DirsInside):
    """
    given the list of names. (classes)

    Return : len(classes) subdirectory inside a parent_direcory named as Cropped_Objects.
    """
    try:
        # 10 different folder will be created inside of this 1 main folder.
        parent_dir = 'Cropped_Objects/'
        os.makedirs(parent_dir)
        for dirName in list_Of_DirsInside:
            try:
                # Create target Directory
                os.mkdir(parent_dir+dirName)
                print("Directory ", dirName,  " Created ")
            except FileExistsError:
                print("Directory ", dirName,  " already exists")
    except FileExistsError:
        print('\nmainDirectory Already exist!')
    print("created_dictionaries(): Finished Successfully!\n")
    return parent_dir, list_Of_DirsInside


def makeDF(csv_path):
    """ Read a comma-separated values (.csv) file into DataFrame.
    Arg: csv PATH:
    Return: new DF.
    """
    DF = pd.read_csv(csv_path)

    DF['height'] = DF.apply(lambda DF: abs(DF['ymax'] - DF['ymin']), axis=1)
    DF['width'] = DF.apply(lambda DF: abs(DF['xmax'] - DF['xmin']), axis=1)
    DF['objArea'] = DF.apply(lambda DF: (DF['width'] * DF['height']), axis=1)
    imageArea = 2704 * 1524
    DF['objPortion'] = DF.apply(lambda DF: (DF['objArea'] / imageArea), axis=1)

    # DF.to_csv('/NewDF.csv')

    # Looking at the first 5 rows to get the insigt on the data.
    print(DF.head(5))
    print(DF.label.unique())
    print("\nMADE_DF(): Finished successfully!\n")
    return DF


DF = makeDF(csv_path=CSV_PATH)


def cropper(imageList):
    """
    Arg: list of jpeg images.
    Return: cropped images and save them.

    # Iterating over the images in imagelist for multiple objects.

    # # _ is the object number, for example in 3D_L0215_161.jpg we have 29 objects.

    should crop the objects in images and save their renamed name in an specific directory.
    """

    # Different Classes.
    classes = ['Past', 'Gorgonia', 'SeaRods', 'Antillo', 'Fish',
               'Ssid', 'Orb', 'Other_Coral', 'Apalm', 'Galaxaura']

    parent_dir, list_Of_DirsInside = create_directories(classes)
    # print(parent_dir, list_Of_DirsInside[0])  # Test

    # You can edit the jpg1_str later. -> Here I am testing it only on one image.
    for jpg1_str in imageList:
        #    print('jpg_str:', jpg1_str)
        for object_id, row in DF[DF.image == jpg1_str].iterrows():

            xmin = row.xmin
            xmax = row.xmax
            ymin = row.ymin
            ymax = row.ymax
            # Might be unnecessary but I am keeping it here for a while + better speed performance. (To be checked later.)
            width = row.width
            height = row.height

            # I print the object_id and height and width of each object here. ( Or bounding Box.)
            # print('object_id: '+str(object_id), "objWidth: " +
            #      str(width), "objHeight: "+str(height))

            input_image = Image.open(JPGPATH + jpg1_str)
            # print(input_image)  # Test to see if the image is being read.

            for index in range(len(classes)):
                if row.label == classes[index]:
                    # print("classes[index]: ", classes[index])

                    imcr = input_image.crop((xmin, ymin, xmax, ymax))  # Test
                    # imcr.show()  # Test

                    FINALDIR = parent_dir+list_Of_DirsInside[index] + '/'
                    renameIt = jpg1_str[:-4]
                    imcr.save(FINALDIR + str(object_id) + "_" +
                              str(classes[index]) + "_" + renameIt + '.png')


if __name__ == "__main__":
    # print(list_of_images(JPGPATH))
    cropper(list_of_images(JPGPATH))

# TODO: later:
# creating the binary mask for Anitolio. -> Later On.
# output_image.save("Final" + str(jpg1_str)+'.png') # creating the binary mask for Anitolio.
