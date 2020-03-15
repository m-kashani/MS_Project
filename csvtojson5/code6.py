# http://cocodataset.org/#format-data
"""
annotation{
"id": int, "image_id": int, "category_id": int, "segmentation": RLE or [polygon], "area": float, "bbox": [x,y,width,height], "iscrowd": 0 or 1,
}

categories[{
"id": int, "name": str, "supercategory": str,
}]
"""

# https://github.com/facebookresearch/detectron2/issues/349

from detectron2.data.datasets.coco import convert_to_coco_json
from detectron2.data import MetadataCatalog, DatasetCatalog

def data_dict():
    return [{
        'file_name': 'image.png',
        'image_id': 'image',
        'height': 100,
        'width': 100,
        'annotations': [{
            'bbox': [70, 30, 100, 70],
            ## area should be 30*40=1200
            'bbox_mode': BoxMode.XYXY_ABS,
            'category_id': 0,
            'iscrowd': 0,
        }]
    }]

def to_json():
    DatasetCatalog.register('test', data_dict)
    MetadataCatalog.get('test').set(thing_classes=["first"])
    convert_to_coco_json('test', output_folder='./output', allow_cached=False)

if __name__ == '__main__':
    to_json()