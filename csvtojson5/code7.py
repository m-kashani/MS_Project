# Should be merged with code6.py
# Just trying to go through 1 image and see the pattern.
"""
               image         xmin         ymin         xmax         ymax    label      height       width       objArea  objPortion
366  3D_L0441_41.jpg  1771.904437   922.258702  1984.163823  1184.253859     Ssid  261.995157  212.259386  55610.931154    0.013495
367  3D_L0441_41.jpg  1336.311263    93.837394  1687.000683   274.650953  Antillo  180.813559  350.689420  63409.402210    0.015387
368  3D_L0441_41.jpg  1395.374744  1147.353133  1519.038908  1304.181220  Antillo  156.828087  123.664164  19394.014263    0.004706
369  3D_L0441_41.jpg  1194.189761   483.399516  1380.608874   758.050469  Antillo  274.650953  186.419113  51200.187013    0.012425
"""

sample_output = {"info": {"date_created": "2020-03-15 04:59:45.442988", "description": "Automatically generated COCO json file for Detectron2."},
                 "images": [{"id": "image", "width": 100, "height": 100, "file_name": "image.png"}],
                 "annotations": [{"id": 1, "image_id": "image", "bbox": [70.0, 30.0, 30.0, 40.0], "area": 1200.0, "iscrowd": 0, "category_id": 0}],
                 "categories": [{"id": 0, "name": "first"}],
                 "licenses": null}

# 1- "info" section: contain high level information about the dataset. # Done. (Whatever is appropriate.)
"info": [{
    "description": "Coral REEF Dataset",
    "url": "hopkinsonlab.org",
    "version": "Version 1.0",
    "year": "2019",
    "contributor": "Hopkinson Lab",
    "date_created" "2019-9-3 2:07 PM",
}
]

# 2- images
# "coco_url": null
# "flickr_url": null

# it will repeat 1 time.
"images": [{
    "id":
    "licence":
    "width": DF.['width']
    "file_name": DF['image']
    "date_captured":}
]

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
