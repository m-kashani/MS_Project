# Validate the detectron dataset + other stuff that can happen here.
# Maybe later: # http://cocodataset.org/#format-data

# If NameError: name 'BoxMode' is not defined. -> python setup.py install <- detectron2.

from detectron2.structures import Boxes, BoxMode, PolygonMasks
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets.coco import convert_to_coco_json


#####

""" Path and image names.
JPGImagesPATH = './Data/vott-csv-export/JPGImages/'
jpg1_str = 'A_3D_L0646_144.jpg'
"""

CSV_PATH = "../Data/Annotations/FL_Keys_Coral-export.csv"
JPGPATH = '../Data/vott-csv-export/JPGImages/'

# List of images for later on tests.
imagelist1 = ['A_3D_L0646_144.jpg', '3D_L0622_176.jpg', '3R010215_829.jpg',
              '3D_L0622_139.jpg', 'B_3D_L0647_42.jpg']  # To do later on 5 different images.
im_0 = ['3D_L0441_41.jpg']  # 4 objects lowest 3


def makeDF(csv_path):
    """ Read a comma-separated values (.csv) file into DataFrame.
    Arg: csv PATH:
    Return: new DF.
    """
    import pandas as pd
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
#####


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

# print(data_dict(), '\n\n\n\n')


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

    # 1
    DatasetCatalog.register('test', data_dict2)

    # 2  Metadata(name='test', thing_classes=['first'])
    MetadataCatalog.get('test').set(thing_classes=["first"])

    # 3
    convert_to_coco_json('test', output_file='./output',
                         allow_cached=False)  # output_folder -> output_file
    # last line:
    print("to_json(): ", "Finished successfully!")


################################ FROM HERE I AM WRITING ############################
# fn, object_id, height, width, xmin, ymin, xmax, ymax, BBOX_MODE, image_id, index)
def data_dict2():
    object_id = "366"  # for example
    index = 0
    width = 102
    height = 102

    fn = 'image.png'

    xmin = 72
    ymin = 32
    xmax = 102
    ymax = 72
    bbox = [xmin, ymin, xmax, ymax]
    BBOX_MODE = BoxMode.XYXY_ABS  # Constant.

    category_id = index  # you need to label it as well.
    image_id = object_id

    return [{
        'file_name': fn,
        'image_id': object_id,
        'height': height,
            'width': width,
            'annotations': [{
                'bbox': bbox,
                'bbox_mode': BoxMode.XYXY_ABS,
                'category_id': index,
            }]
            }]


if __name__ == '__main__':
    to_json()
    print("__main__: Finished successfully!\n")


##################################################################################

for item in im_0:  # In yek bar Run mishe -> 1 ax darim -> 4 ta object tooshe -> im_0
    # Filter the .csv file based on the ax -> behem dataframe jadid mide baraye 1 ax.
    NewDF = DF[DF['image'] == item]
    print(NewDF)
    print('*'*80)

    for category in [NewDF['label']]:
        # Filter based on the object ( category ) -> category id + .
        print(category)

 #       print(NewerDF)

    # bbox = [NewDF.xmin, NewDF.ymin, NewDF.xmax, NewDF.ymax] # ...
    # print(bbox)

    # image NAME + image FORMAT
#    img_name = item.split('.')[0] #
#    img_frmt = item.split('.')[1] #

#    print(img_name, img_frmt)

    # image ID ??
#   image_id = item[-7:-4]

    # label ID ??
    # To do -> create a column in pandas.
