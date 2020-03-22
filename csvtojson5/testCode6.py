import json
from detectron2.structures import Boxes, BoxMode, PolygonMasks
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets.coco import convert_to_coco_json

THING_CLASSES = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral',
                 'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']

JSON_PATH_all = '/Users/mac7/Desktop/MS_Project/json_annot_all.json'
#JSON_URL_sample = 'https://github.com/m-kashani/MS_Project/blob/master/csvtojson5/json_annotation_v1.json'


def _readDict(JsonURL):
    import pandas as pd
    dictionarySample = pd.read_json(JsonURL)
    print('_readict(): is working successfully!')
    return dictionarySample


print(_readDict(JSON_PATH_all)['image'][366])  # Test


def _json_annotation_v1(object_id, THING_CLASSES):

    category_id = THING_CLASSES.index(
        _readDict(JSON_PATH_all)["label"][object_id])

    width = _readDict(JSON_PATH_all)["width"][object_id]
    height = _readDict(JSON_PATH_all)["height"][object_id]
    fn = _readDict(JSON_PATH_all)["image"][object_id]  # Cool.
    xmin = _readDict(JSON_PATH_all)["xmin"][object_id]
    ymin = _readDict(JSON_PATH_all)["ymin"][object_id]
    xmax = _readDict(JSON_PATH_all)["xmax"][object_id]
    ymax = _readDict(JSON_PATH_all)["ymax"][object_id]

    bbox = [xmin, ymin, xmax, ymax]  # Cool.
    BBOX_MODE = BoxMode.XYXY_ABS  # CONSTANT.

    print('_json_annotation_v1(object_id):, Finished Successfully.')

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


object_id = 366
print(_json_annotation_v1(object_id, THING_CLASSES))
