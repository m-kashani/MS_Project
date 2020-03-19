# Should be merged with code6.py.
# Just trying to go through 1 image and see the pattern.

CSV_PATH = "../Data/Annotations/FL_Keys_Coral-export.csv"
JPGPATH = '../Data/vott-csv-export/JPGImages/'


def makeDF(csv_path):
    """ Read a comma-separated values (.csv) file into DataFrame.
    Arg: csv PATH
    Displays the first 5 rows.
    Return: new_DF
    """
    import pandas as pd
    DF = pd.read_csv(csv_path)

    DF['height'] = DF.apply(lambda DF: abs(DF['ymax'] - DF['ymin']), axis=1)
    DF['width'] = DF.apply(lambda DF: abs(DF['xmax'] - DF['xmin']), axis=1)
    DF['objArea'] = DF.apply(lambda DF: (DF['width'] * DF['height']), axis=1)
    imageArea = 2704 * 1524
    DF['objPortion'] = DF.apply(lambda DF: (DF['objArea'] / imageArea), axis=1)

    # DF.to_csv('/NewDF.csv').

    # Looking at the first 5 rows to get the insigt on the data.
    print(DF.head(5))
    print('\nLabels: ', DF.label.unique())
    print("\nMADE_DF(): Finished successfully!\n", 130*'*')
    return DF


DF = makeDF(csv_path=CSV_PATH)

im_0 = '3D_L0441_41.jpg'  # 4 objects lowest 3.
im = im_0
print(DF[DF['image'] == im])  # test.

# Example-0 : A coco dataset should have 5 different segments.
info_val0 = {"date_created": "2020-03-15 04:59:45.442988",
             "description": "Automatically generated COCO json file for Detectron2."}
images0 = [{"id": "image", "width": 100,
            "height": 100, "file_name": "image.png"}]
annotations0 = [{"id": 1, "image_id": "image", "bbox": [70.0, 30.0, 30.0, 40.0],
                 "area": 1200.0, "iscrowd": 0, "category_id": 0}]
categories0 = [{"id": 0, "name": "first"}]
licence0 = 'null'

sample_output = {"info": info_val0,
                 "images": images0,
                 "annotations": annotations0,
                 "categories": categories0,
                 "licenses": licence0}
print(sample_output, 'n\n\n\n\n')

# 1- "info" section: contain high level information about the dataset. # Done. (Whatever is appropriate.)
info_VAL = {
    "description": "Coral REEF Dataset",
    "url": "hopkinsonlab.org",
    "version": "Version 1.0",
    "year": "2019",
    "contributor": "Hopkinson Lab",
    "date_created": "2019-9-3 2:07 PM", }
sample_infoDone = {"info": info_VAL,
                   "images": images0,
                   "annotations": annotations0,
                   "categories": categories0,
                   "licenses": licence0}
print(sample_infoDone, '\n\n\n\n')

# 2- images
# "coco_url": null
# "flickr_url": null

# it will repeat 1 time.
images_VAL = [{
    "id": "?idImage",
    "licence": "?licenceImage",
    "width": DF.loc[[366, 'width']],
    "file_name": DF.loc[366, 'image'],
    "date_captured":'?date_capturedImage'}]
sample_infoDone = {"info": info_VAL,
                   "images": images_VAL,
                   "annotations": [{"id": 1, "image_id": "image", "bbox": [70.0, 30.0, 30.0, 40.0], "area": 1200.0, "iscrowd": 0, "category_id": 0}],
                   "categories": [{"id": 0, "name": "first"}],
                   "licenses": 'null'}
print(sample_infoDone, '\n\n\n\n')

# for index ...
# category_id = index


"""
# 3- annotations
# "iscroud" : 0, # ------------------> I have a code to calculate it. (later project.)
# "segmentation": [[1, 1, 2, 2, 3, 3, 4, 4][9, 9, 8, 8, 7, 7, 6, 6]],

# it will repeat 4 times.
for objects_id in each_image:
    "annotations": [
        {"id": object_id,
         "category_id": classes.index('Past'),
         "image_id": int(1)
         "area": float(1)
         bbox": list(1)
         'bbox_mode': BoxMode.XYXY_ABS,
         },
        {"id": 2,
         #        ...
         }
    ]

classes = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral',
           'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']

# 4- "categories" object contains a list of categories (e.g. 'Antillo', 'Ssid', 'Past', 'Gorgonia', ...)
# for label in range(len(classes)):
"categories": [
    {"supercategory": "CoralReef", id: label, name: classes[j]},
    #         ...
]

# 5- "licence" section: contains a list of image licences that apply to images in the dataset.

for id in image_id:
    # If you are sharing or selling your dataset make sure your licences are correctly specified and that you are not infringing on copyright.

    "url": "s3-bucket"
    "id": id,
    "name": "University of Georgia Licence"
"""


# Sample images to check my function.
im_0 = '3D_L0441_41.jpg'  # 4 objects lowest 3
# Almost 53 objects which are mostly `Galaxaura`.
im_1 = 'A_3D_L0646_144.jpg'

imagelist1 = ['A_3D_L0646_144.jpg', '3D_L0622_176.jpg',
              '3R010215_829.jpg', '3D_L0622_139.jpg', 'B_3D_L0647_42.jpg']

im = im_0

NewDF = DF[DF['image'] == im]
# NewDF.to_json('json_annotation.json')  # test.
print(NewDF)

# How many classes do we have in label?
print(NewDF['label'].value_counts()[:])
''' result:
    Antillo    3
    Ssid       1
    '''
