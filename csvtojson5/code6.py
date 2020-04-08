# Validate the detectron dataset + other stuff that can happen here.
# Maybe later: # http://cocodataset.org/#format-data
# https://github.com/akTwelve/cocosynth
# If NameError: name 'BoxMode' is not defined. -> python setup.py install <- detectron2.

import json
from detectron2.structures import Boxes, BoxMode, PolygonMasks
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets.coco import convert_to_coco_json

""" Path and image names.
JPGImagesPATH = './Data/vott-csv-export/JPGImages/'
jpg1_str = 'A_3D_L0646_144.jpg'
"""

CSV_PATH = "../Data/Annotations/FL_Keys_Coral-export.csv"
JPG_PATH = '../Data/vott-csv-export/JPGImages/'


def makeDF(csv_path):
    """ Read a comma-separated values (.csv) file into DataFrame.
    Arg: csv PATH:
    Return: new DF.
    """
    import pandas as pd
    DF = pd.read_csv(csv_path)

    # DF['height'] = DF.apply(lambda DF: abs(DF['ymax'] - DF['ymin']), axis=1)
    # DF['width'] = DF.apply(lambda DF: abs(DF['xmax'] - DF['xmin']), axis=1)
    # DF['objArea'] = DF.apply(lambda DF: (DF['width'] * DF['height']), axis=1)
    HEIGHT = 2704
    WIDTH = 1524
    imageArea = HEIGHT * WIDTH
    # DF['objPortion'] = DF.apply(lambda DF: (DF['objArea'] / imageArea), axis=1)

    # DF.to_csv('/NewDF.csv')

    # Looking at the first 5 rows to get the insigt on the data.
    # print(DF.head(5))
    # print(DF.label.unique())
    # print("\nMADE_DF(): Finished successfully!\n")
    return DF


# DF = makeDF(csv_path=CSV_PATH)


def list_of_images(JPGPATH):
    """
    Arg: JPGPATH

    Return: listOf_images for creating the xml files.

    Used also in code5,.py
    """
    import os
    listOF_imgs = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(JPGPATH):
        for file in f:
            if '.jpg' in file:
                listOF_imgs.append(os.path.join(file))

    return listOF_imgs


# LIMG = list_of_images(JPG_PATH)
# print(LIMG)

def _get_coral_dicts():

    imgs_anns = makeDF(CSV_PATH)
    # print(type(imgs_anns))

    THING_CLASSES = list(imgs_anns.label.unique())
    # print(THING_CLASSES)

    datadict = []
    for IMG_id, fn in enumerate(list_of_images(JPG_PATH)):
        record = {}

        HEIGHT = 1524
        WIDTH = 2704
        # print(width, height)

        record['file_name'] = fn  # 4 objects lowest 3.
        record['image_id'] = IMG_id + 1
        record['height'] = HEIGHT
        record['width'] = WIDTH

        objs = []
        # print(imgs_anns[imgs_anns['image'] == fn].iterrows())  # Test
        for object_id, _ in imgs_anns[imgs_anns['image'] == fn].iterrows():
            # print(object_id, _) # Test

            xmin = imgs_anns["xmin"][object_id]
            ymin = imgs_anns["ymin"][object_id]
            xmax = imgs_anns["xmax"][object_id]
            ymax = imgs_anns["ymax"][object_id]

            bbox = [xmin, ymin, xmax, ymax]
            BBOX_MODE = BoxMode.XYXY_ABS  # CONSTANT.

            category_id = THING_CLASSES.index(imgs_anns["label"][object_id])
            # print(imgs_anns['label'][object_id], category_id)

            obj = {
                'bbox': bbox,
                'bbox_mode': BBOX_MODE,
                'category_id': category_id,
            }
            """
            #TODO:
            I can say: 'segmentation': <input that he can provide.
            """
            objs.append(obj)
            record['annotations'] = objs

        datadict.append(record)

    return datadict


print(_get_coral_dicts())


def to_json():
    # /Users/mac7/Desktop/MS_Project/csvtojson5/detectron2/detectron2/data/catalog.py
    """
    1 :
        DatasetCatalog.register(name, func):
        Args:
            name (str): the name that identifies a dataset, e.g. "coco_2014_train".
            func (callable): a callable which takes no arguments and returns a list of dicts.

        Call the registered function and return its results.

    2 :
        Args:
            name (str): the name that identifies a dataset, e.g. "coco_2014_train".

        Returns:
            list[dict]: dataset annotations.0

        A class that supports simple attribute setter/getter.
        It is intended for storing metadata of a dataset and make it accessible globally.

        Examples:

        .. code-block: : python

        somewhere when you load the data:
        MetadataCatalog.get("mydataset").thing_classes = ["person", "dog"]

        somewhere when you print statistics or visualize:
        classes = MetadataCatalog.get("mydataset").thing_classes

    3 :
        Convert it to the coco.
        .
        .
        .
    """
    THING_CLASSES = ['Past', 'Gorgonia', 'SeaRods', 'Antillo',
                     'Fish', 'Ssid', 'Orb', 'Other_Coral', 'Apalm', 'Galaxaura']
    # 1
    DatasetCatalog.register('coraltest', _get_coral_dicts)
    # 2  Metadata(name='test', thing_classes=['first'])
    MetadataCatalog.get('coraltest').set(thing_classes=THING_CLASSES)
    # 3
    convert_to_coco_json('coraltest', output_file='./output',
                         allow_cached=False)  # output_folder -> output_file

    # print("to_json():", "Finished successfully!")


# TODO:
if __name__ == '__main__':
    to_json()
    # print("__main__: Finished successfully!\n")
