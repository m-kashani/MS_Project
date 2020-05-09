# MS_Project
**Comparison of different object detection algorithms on coral reef data sets.**


>Powered By: [[`detectron2(code)`](https://github.com/facebookresearch/detectron)]

## Abstract
Sometimes we need to be sure about our very first steps, mainly when we havedived into the underwater ecosystem. While we need to think about being equipped with an in-depth real-time application mindset, it is still an open question for many of the marine scientists, which state of art methodology helps to be the most caring about the gaseous substances that provide the vital life-sustainingforce. After a comprehensive exploratory data analysis on our new coral-reefdataset and validating the quality of the annotation, we have decided the rightpre-trained model on the appropriate dataset. We examined three-under developing open-source detection benchmarks on our coral reef dataset. Our study on the comparison of object detection algorithms includes, but is not limited to,YOLOv2, YOLOv3, Faster RCNN, CascadeRCNN, and RetinaNet.

#	Explain the directories and everything ... 

Annotations:
	.csv
	.txt

## TODO
 - [ ] cleaning ... 
 - [ ] writing.
 - [x] Reading from the good project (readme) https://github.com/youngwanLEE/vovnet-detectron2/edit/master/README.md
 - [x] Running the Docker file.
 - [x] Installing the detectron2.
 - [x] Working withthe Meshrcnn, pytorch3. [added to the future work.] https://github.com/m-kashani/meshrcnn
 - [x] JPGImages.zip -> Original Files
 - [x] Preprocessing the red images. -> Not a good result though still.
 - [x] Enhanced.zip -> .png images
 - [x] Choosing 20 Images with most amount of Objects and then choosing 3 good images.
 - [x] Opened an issue on `code12.py`. > Add to do list here:
 - [x] Code 5 should crop the objects in images and save their renamed name in an specific directory.
 - [x] Upload the zipped directory to the google drive.
 - [x] Ubuntu > Mac issue ... (Finally commit them ... 1 version!).
 - [x] Refactoring all of the codes with autopep8 standard and auto config and installing Kite.
 - [x] Converting my `.csv to coco format/ imagenet` / code6.py and registering the data in detectron2.
 - [x] Preprocessed the data -> enhanced.png.
 - [x] Splitting the data into the training and test and making sure that we have every categories in both.
 - [x] Figuring out the code for evaluation.
 - [x] Pixel-wise annotation tool and segmentation taks -> Labelme.
 - [x] running the code on GPU with over 8GB memory -> worked -> reporting the error.
 - [ ] running the code on GPU with over 12GB memory -> AWS Sagerate
 - [x] labeling and background truth validation with Sagemaker -> Fixing the Docker forwarding port issue.
 - [ ] Start writing the report!
 - [ ] Calculating the Fscore and Recal based on the AP.
 - [x] Yolo2 vs Yolo3.
 - [ ] mmdetectron.
 - [ ] Running the detectron2 colab in `code8.py`. -> GPU is needed.
 - [ ] Creating the binary mask for the images created in `code5.py` for later on -> pycoco
 - [ ] Figuring out the rotation and zooming in zooming out and other augmentation methods on the objects.
 - [x] generated AssertionError: Torch not compiled with CUDA enabled error > `code8.py`

 - [ ] Add the detectron dependencies to the setup.py -> https://github.com/facebookresearch/detectron2/network/dependencies

 - [ ] FlowerDetection -> ALDI -> Next
 - [ ] Zeidan -> IP Proj
 
Data:
	ImageSets/
		/Main		#	It will be generated by the splitter.
			train.txt
			test.txt
			val.txt
			trainval.txt
```bash
.
├── Data
│   ├── Annotations
│   │   ├── FL_Keys_Coral-export.csv
│   │   └── my_data.txt
│   ├── ImageSets
│   │   └── Main
│   │   ├── test.txt
│   │   ├── train.txt
│   │   ├── trainval.txt
│   │   └── val.txt
│   └── vott-csv-export
│   └── JPGImages
│   ├── 3D_L0215_161.jpg
    .
    .
    .
│   └── D_3D_L0649_83.jpg
├── JPGImages.zip
├── LICENSE
├── NewDF.csv # width, height, aria, Object portion
├── R.ipynb
├── README.md
├── code12.py
├── code3.py
├── code4.py
├── csvtojson5
    ├── Cropped_Objects
       ├── Antillo
        │   ├── 1001_Antillo_3D_L0622_22.png
        .
        .
        │   └── 999_Antillo_3D_L0622_22.png
        ├── Apalm
        │   ├── 1519_Apalm_3D_L0457_119.png
        .
        .
        │   └── 763_Apalm_3D_L0453_81.png
        ├── Fish
        │   ├── 105_Fish_3D_L0441_110.png
        .
        .
        │   └── 928_Fish_3D_L0622_176.png
        ├── Galaxaura
        │   ├── 1883_Galaxaura_A_3D_L0646_144.png
        .
        .
        │   └── 9_Gorgonia_3D_L0215_161.png
        ├── Orb
        │   ├── 104_Orb_3D_L0441_110.png
        .
        .
        │   └── 467_Orb_3D_L0443_93.png
        ├── Other_Coral
        │   ├── 1000_Other_Coral_3D_L0622_22.png
        .
        .
        │   └── 997_Other_Coral_3D_L0622_22.png
        ├── Past
        │   ├── 0_Past_3D_L0215_161.png
        .
        .
        │   └── 993_Past_3D_L0622_22.png
        ├── SeaRods
        │   ├── 1006_SeaRods_3D_L0622_54.png
        .
        .
        │   └── 982_SeaRods_3D_L0622_22.png
        └── Ssid
        ├── 102_Ssid_3D_L0441_110.png
        .
        .
        └── 964_Ssid_3D_L0622_22.png
│   ├── Cropped_Objects.zip
│   ├── code5.py
│   ├── code6.py
│   ├── code7.py
│   ├── json_annotation_v1.json
│   ├── output
│   └── pycococreator
│   ├── LICENSE
│   ├── README.md
│   ├── examples
│   │   └── shapes
│   │   ├── shapes_to_coco.py
│   │   ├── train
│   │   │   ├── annotations
│   │   │   │   ├── 1000_square_0.png
│   │   │   │   ├── 1001_circle_0.png
│   │   │   │   ├── 1001_circle_3.png
│   │   │   │   ├── 1001_square_1.png
│   │   │   │   └── 1001_square_2.png
│   │   │   └── shapes_train2018
│   │   │   ├── 1000.jpeg
│   │   │   └── 1001.jpeg
│   │   └── visualize_coco.ipynb
│   ├── pycococreatortools
│   │   ├── __init__.py
│   │   └── pycococreatortools.py
│   ├── setup.cfg
│   └── setup.py
├── my_split.py
├── result.html
└── top_20.csv

25 directories, 4171 files
```
