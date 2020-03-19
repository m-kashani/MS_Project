# You may need to restart your runtime prior to this, to let your installation take effect
# Some basic setup:
# Setup detectron2 logger
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import Visualizer
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2 import model_zoo
import random
import cv2
import numpy as np
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
# import some common libraries
# import some common detectron2 utilities

CROPPED_PATH = './Cropped_Objects/Galaxaura/'


def list_of_images(CROPPED_PATH):
    """
    Arg: JPGPATH

    Return: listOf_images for cropper() function.

    Kinda got helped from.
    https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/
    """
    import os
    listOF_imgs = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(CROPPED_PATH):
        for file in f:
            if '.png' in file:
                listOF_imgs.append(os.path.join(file))

    return listOF_imgs


GalaxauraList = list_of_images(CROPPED_PATH)
# print(GalaxauraList, '\n', 'X'*66)  # Test.


def my_part():
    """
    !wget http://images.cocodataset.org/val2017/000000439715.jpg -O input.jpg
    im = cv2.imread("./input.jpg")
    cv2_imshow(im)
    """
    from PIL import Image

    SampleObj = GalaxauraList[3]  # test
    SampleObj = '1889_Galaxaura_A_3D_L0646_144.png'  # test

    input_image = Image.open(CROPPED_PATH+SampleObj)
    input_image.show()
    return input_image


input_image = my_part()

"""
cfg = get_cfg()
# add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
cfg.merge_from_file(model_zoo.get_config_file(
    "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
# Find a model from detectron2's model zoo. You can use the https://dl.fbaipublicfiles... url as well
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(
    "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
predictor = DefaultPredictor(cfg)
outputs = predictor(input_image)

print(outputs)
"""
