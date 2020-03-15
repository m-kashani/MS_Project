# Implementing the data_dict() on one sample image:

# Maybe later: # http://cocodataset.org/#format-data

def read_csv():
    import pandas as pd
    # Read a comma-separated values (.csv) file into DataFrame.
    DF = pd.read_csv('../Data/Annotations/FL_Keys_Coral-export.csv') # From code 1.
    return DF

DF = read_csv()

############################################################### I took it from: 
# https://github.com/facebookresearch/detectron2/issues/349

from detectron2.data.datasets.coco import convert_to_coco_json
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.structures import BoxMode, PolygonMasks, Boxes

## Area should be 30*40=1200
def data_dict():
    return [{
        'file_name': 'image.png',
        'image_id': 'image',
        'height': 100,
        'width': 100,
        'annotations': [{
            'bbox': [70, 30, 100, 70],
            'bbox_mode': BoxMode.XYXY_ABS,
            'category_id': 0,
            'iscrowd': 0,
        }]
    }]

"""
def to_json():
    DatasetCatalog.register('test', data_dict)
    MetadataCatalog.get('test').set(thing_classes=["first"])
    convert_to_coco_json('test', output_file='./output', allow_cached=False)

if __name__ == '__main__':
    to_json()
"""

################################################################ You can add the add later.

def data_dict2(fn, bbox, image_id,height, width):
    return [{
        'file_name': fn,
        'image_id': image_id,
        'height': height,
        'width': width,
        'annotations': [{
            'bbox': bbox,
            'bbox_mode': BoxMode.XYXY_ABS,
            'category_id': 0,
            'iscrowd': 0,
        }]
    }]

fn = 'image.png',
bbox = [70, 30, 100, 70]
image_id = 'image'

""" Path and image names.
JPGImagesPATH = './Data/vott-csv-export/JPGImages/'
jpg1_str = 'A_3D_L0646_144.jpg'
"""

imagelist1 = ['A_3D_L0646_144.jpg', '3D_L0622_176.jpg', '3R010215_829.jpg', '3D_L0622_139.jpg', 'B_3D_L0647_42.jpg'] # To do later on 5 different images.
im_0 = ['3D_L0441_41.jpg'] # 4 objects lowest 3

for item in im_0: # In yek bar Run mishe -> 1 ax darim -> 4 ta object tooshe -> im_0
    NewDF = DF[DF['image'] == item] # Filter the .csv file based on the ax -> behem dataframe jadid mide baraye 1 ax.
    print(NewDF)
    print('*'*80)

    for category in [NewDF['label']]:
        # Filter based on the object ( category ) -> category id + .
        print(category)
        
 #       print(NewerDF)




    #bbox = [NewDF.xmin, NewDF.ymin, NewDF.xmax, NewDF.ymax] # ... 
    #print(bbox)

    # image NAME + image FORMAT
#    img_name = item.split('.')[0] #
#    img_frmt = item.split('.')[1] #

#    print(img_name, img_frmt)

    # image ID ?? 
#   image_id = item[-7:-4]

    # label ID ??
    # To do -> create a column in pandas.