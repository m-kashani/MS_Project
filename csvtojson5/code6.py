# Validate the detectron dataset + other stuff that can happen here.
# Maybe later: # http://cocodataset.org/#format-data
# https://github.com/akTwelve/cocosynth
# If NameError: name 'BoxMode' is not defined. -> python setup.py install <- detectron2.

import json
from detectron2.structures import Boxes, BoxMode, PolygonMasks
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets.coco import convert_to_coco_json

CSV_PATH = "../Data/Annotations/FL_Keys_Coral-export.csv"

ENHANCED_PATH = "../Data/Enhanced/"
ENHANCED_PATH_train = "../Data/Enhanced/SPLITTED_OBJECTs/train/"
ENHANCED_PATH_valid = "/Users/mac7/Desktop/MS_Project/Data/Enhanced/SPLITTED_OBJECTs/val/"
# Enhanced_test = "/Users/mac7/Desktop/MS_Project/Data/Enhanced/SPLITTED_OBJECTs/test/" not implemented

# TODO: Making a loop mabe ... (automating it.)
IMG_FORMAT = '.png'  # '.jpg'
IMGs_PATH = ENHANCED_PATH_valid
OP = './enhanced_valid.json'

# List of images for later on tests.
imagelist1 = ['A_3D_L0646_144.jpg', '3D_L0622_176.jpg', '3R010215_829.jpg',
              '3D_L0622_139.jpg', 'B_3D_L0647_42.jpg']  # To do later on 5 different images.


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


def data_dict0():
    """
    generated from code7.py. However, is not compatible with the
    25, in convert_to_coco_json
    coco_dict = convert_to_coco_dict(dataset_name)
    File "/Users/mac7/opt/anaconda3/envs/myenvpy/lib/python3.7/site-packages/detectron2-0.1.1-py3.7-macosx-10.9-x86_64.egg/detectron2/data/datasets/coco.py", line 314, in convert_to_coco_dict
    "width": image_dict["width"],
    KeyError: 'width'
    """

    # 0- Sample from detectron2 -> 5 different sections.
    info_val0 = [{"date_created": "2020-03-15 04:59:45.442988",
                  "description": "Automatically generated COCO json file for Detectron2."}]
    images0 = [{"id": "image", "width": 100,
                "height": 100, "file_name": "image.png"}]
    annotations0 = [{"id": 1, "image_id": "image", "bbox": [70.0, 30.0, 30.0, 40.0],
                     "area": 1200.0, "iscrowd": 0, "category_id": 0}]
    categories0 = [{"id": 0, "name": "first"}]
    licence0 = 'null'

    return [{"info": info_val0,
             "images": images0,
             "annotations": annotations0,
             "categories": categories0,
             "licenses": licence0}]

# print(data_dict0(), '\n\n\n') # test above function.


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
            if '.jpg' in file or '.png' in file:
                listOF_imgs.append(os.path.join(file))

    return listOF_imgs


# LIMG = list_of_images(IMGs_PATH)
# print(LIMG)


def _get_coral_dicts():

    imgs_anns = makeDF(CSV_PATH)
    # print(type(imgs_anns))

    THING_CLASSES = list(imgs_anns.label.unique())
    # print(THING_CLASSES)

    datadict = []
    for IMG_id, fn in enumerate(list_of_images(IMGs_PATH)):
        record = {}

        HEIGHT = 1524
        WIDTH = 2704
        # print(width, height)
        image_name = fn.split('.')[0]
        record['file_name'] = image_name + IMG_FORMAT
        record['image_id'] = IMG_id + 1
        record['height'] = HEIGHT
        record['width'] = WIDTH

        objs = []
        # print(imgs_anns[imgs_anns['image'] == fn].iterrows())  # Test
        # print(image_name)
        for object_id, _ in imgs_anns[imgs_anns['image'] == (image_name+'.jpg')].iterrows():
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
            list[dict]: dataset annotations.

        A class that supports simple attribute setter/getter.
        It is intended for storing metadata of a dataset and make it accessible globally.

        Examples:

        .. code-block: : python

        somewhere when you load the data:
        MetadataCatalog.get("mydataset").thing_classes = ["person", "dog"]

        somewhere when you print statistics or visualize:
        classes = MetadataCatalog.get("mydataset").thing_classes.

    3 :
        Convert it to the coco.
        .
        .
        .
    """
    THING_CLASSES = ['Past', 'Gorgonia', 'SeaRods', 'Antillo',
                     'Fish', 'Ssid', 'Orb', 'Other_Coral', 'Apalm', 'Galaxaura']
    # 1
    DatasetCatalog.register('coral', _get_coral_dicts)
    # 2  Metadata(name='test', thing_classes=['first'])
    MetadataCatalog.get('coral').set(thing_classes=THING_CLASSES)
    # 3
    convert_to_coco_json('coral', output_file=OP,
                         allow_cached=False)  # output_folder -> output_file

    # print("to_json():", "Finished successfully!")


# TODO:
if __name__ == '__main__':
    to_json()
    # print("__main__: Finished successfully!\n")
