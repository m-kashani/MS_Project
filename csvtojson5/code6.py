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


def data_dict():
    """
    This is just a sample dictionary to test the detectron.
    I took it from:
    https://github.com/facebookresearch/detectron2/issues/349
    """
    # it handles the 'iscrowd' itself.
    print("\ndata_dict(): ", "Finished successfully!")
    return [{
        'file_name': 'image.png',
        'image_id': 'image',
        'height': 100,
        'width': 100,
        'annotations': [{
            'bbox': [70, 30, 100, 70],
            'bbox_mode': BoxMode.XYXY_ABS,
            'category_id': 0
        }]
    }]

# print(data_dict(), '\n\n\n\n') # TEST


def data_dict2():
    width = 102
    height = 102

    for IMG_id, fn in enumerate('3D_L0441_41.jpg'):
        image_id = IMG_id  # 4 objects lowest 3.
        file_name = fn  # For example -> enum()

    xmin = 72
    ymin = 32
    xmax = 102
    ymax = 72
    bbox = [xmin, ymin, xmax, ymax]
    BBOX_MODE = BoxMode.XYXY_ABS  # CONSTANT.

    object_id = 366
    THING_CLASSES = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral',
                     'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']
    #    category_id = THING_CLASSES.index(imgs_anns["label"][object_id])
    index = 9
    category_id = index  # you need to label it as well.

    return [{
        'file_name': fn,
        'image_id': image_id,
        'height': height,
            'width': width,
            'annotations': [{
                'bbox': bbox,
                'bbox_mode': BoxMode.XYXY_ABS,
                'category_id': index,
            }]
            }]

# print(data_dict2(), '\n\n\n\n') # TEST


def _json_annotation_v2():
    """
    366,3D_L0441_41.jpg,1771.9044368600685,922.25870157385,1984.1638225255965,1184.2538589588378,Ssid,261.9951573849878,212.25938566552804,55610.93115388085,0.013494864018378733
    367,3D_L0441_41.jpg,1336.3112627986347,93.8373940677966,1687.0006825938567,274.65095338983053,Antillo,180.81355932203394,350.68941979522197,63409.40220975303,0.01538728524324638
    368,3D_L0441_41.jpg,1395.3747440273034,1147.3531325665856,1519.038907849829,1304.181219733656,Antillo,156.8280871670704,123.66416382252555,19394.01426340191,0.004706261517738354
    369,3D_L0441_41.jpg,1194.1897610921499,483.39951573849885,1380.6088737201364,758.0504691283293,Antillo,274.6509533898304,186.41911262798658,51200.18701336269,0.01242452782437671
    """

    imgs_anns = makeDF(CSV_PATH)

    THING_CLASSES = list(imgs_anns.label.unique())

    datadict = []
    for IMG_id, fn in enumerate(['3D_L0441_41.jpg']):
        record = {}

        HEIGHT = 2704
        WIDTH = 1524
        # print(width, height)

        record['file_name'] = JPG_PATH + fn  # 4 objects lowest 3.
        record['image_id'] = IMG_id + 1
        record['height'] = HEIGHT
        record['width'] = WIDTH

        objs = []
        for object_id in [366, 367, 368, 369]:

            xmin = imgs_anns["xmin"][object_id]
            ymin = imgs_anns["ymin"][object_id]
            xmax = imgs_anns["xmax"][object_id]
            ymax = imgs_anns["ymax"][object_id]

            bbox = [xmin, ymin, xmax, ymax]
            BBOX_MODE = BoxMode.XYXY_ABS  # CONSTANT.

            category_id = THING_CLASSES.index(imgs_anns["label"][object_id])
            # print(category_id)

            obj = {
                'bbox': bbox,
                'bbox_mode': BBOX_MODE,
                'category_id': category_id,
            }
            objs.append(obj)
            record['annotations'] = objs

        datadict.append(record)

    return datadict


print(_json_annotation_v2())


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
    THING_CLASSES = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral',
                     'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']
    # 1
    DatasetCatalog.register('coraltest', _json_annotation_v2)
    # 2  Metadata(name='test', thing_classes=['first'])
    MetadataCatalog.get('coraltest').set(thing_classes=THING_CLASSES)
    # 3
    convert_to_coco_json('coraltest', output_file='./output',
                         allow_cached=False)  # output_folder -> output_file

    # last line:
    # print("to_json():", "Finished successfully!")


def get_coral_dicts():

    THING_CLASSES = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral',
                     'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']
    # print(object_id, ': ', THING_CLASSES)

    imgs_anns = makeDF(CSV_PATH)
    dataset_dict = []

    # object_id = range(366, 371)
    object_id = 366

    fn = imgs_anns["image"][object_id]  # Cool.
    # height, width = cv2.imread(filename).shape[:2] :TODO?
    width = 2704
    height = 1524
    # print(width, height)

    xmin = imgs_anns["xmin"][object_id]
    ymin = imgs_anns["ymin"][object_id]
    xmax = imgs_anns["xmax"][object_id]
    ymax = imgs_anns["ymax"][object_id]

    # TODO: Put this inside the object loop #FOR OBJECT ID in NEWDF.
    bbox = [xmin, ymin, xmax, ymax]
    # print(bbox)
    BBOX_MODE = BoxMode.XYXY_ABS  # CONSTANT.
    category_id = THING_CLASSES.index(imgs_anns["label"][object_id])
    # print(category_id)

    # print('get_coral_dict(object_id):, Finished Successfully!')

    return [{
        'file_name': fn,
        'image_id': object_id,
        'height': height,
            'width': width,
            'annotations': [{
                'bbox': bbox,
                'bbox_mode': BBOX_MODE,
                'category_id': category_id,
            }]
            }]


# TODO:
# Put this in a for loop.
object_id = 366
THING_CLASSES = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral',
                 'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']
# print(object_id, ': ', THING_CLASSES)

im_0 = ['3D_L0441_41.jpg']  # 4 objects lowest 3


if __name__ == '__main__':
    to_json()
    # print("__main__: Finished successfully!\n")
