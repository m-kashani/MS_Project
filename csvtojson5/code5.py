# .csv to .json on 5 images creating the binary mask for each image and then using the pytococo.
# Cropper and Saver -> Do it + Function.

# Libraries and initial variables.
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Different Classes.
classes = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral',
           'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']

# Sample images to check my function.
im_0 = '3D_L0441_41.jpg'  # 4 objects lowest 3
im_1 = 'A_3D_L0646_144.jpg'  # Almost 53 objects which are mostly `Galaxaura`.
img_2345 = ['3D_L0622_176.jpg', '3R010215_829.jpg',
            '3D_L0622_139.jpg', 'B_3D_L0647_42.jpg']

# Setting up the image PATH + Reading the images.

DF = pd.read_csv('../Data/Annotations/FL_Keys_Coral-export.csv')  # From Code12

JPGPATH = '../Data/vott-csv-export/JPGImages/'

imageArea = 2704 * 1524
DF['height'] = DF.apply(lambda DF: abs(DF['ymax'] - DF['ymin']), axis=1)
DF['width'] = DF.apply(lambda DF: abs(DF['xmax'] - DF['xmin']), axis=1)
DF['objArea'] = DF.apply(lambda DF: (DF['width'] * DF['height']), axis=1)
DF['objPortion'] = DF.apply(lambda DF: (DF['objArea'] / imageArea), axis=1)
# print(DF[DF['image']==im]) # test.

''' result: It will be removed.
(myenv37) mahdi@mahdi-ThinkPad-T520:~/Desktop/MS_Project/csvtojson5$ python code5.py 
               image         xmin         ymin         xmax         ymax    label      height       width       objArea  objPortion
366  3D_L0441_41.jpg  1771.904437   922.258702  1984.163823  1184.253859     Ssid  261.995157  212.259386  55610.931154    0.013495
367  3D_L0441_41.jpg  1336.311263    93.837394  1687.000683   274.650953  Antillo  180.813559  350.689420  63409.402210    0.015387
368  3D_L0441_41.jpg  1395.374744  1147.353133  1519.038908  1304.181220  Antillo  156.828087  123.664164  19394.014263    0.004706
369  3D_L0441_41.jpg  1194.189761   483.399516  1380.608874   758.050469  Antillo  274.650953  186.419113  51200.187013    0.012425
'''

im = im_0

NewDF = DF[DF['image'] == im]
# NewDF.to_json('json_annotation.json')  # test
print(NewDF)

# How many classes do we have in label?
print(NewDF['label'].value_counts()[:])
''' result:
Antillo    3
Ssid       1
'''


def insideIfCropper():
    print("To be written.")


def cropper(imageList):
    """
    Arg: list of jpeg images.
    Return: cropped images and save them.

    # Iterating over the images in imagelist for multiple objects.

    # # _ is the object number, for example in 3D_L0215_161.jpg we have 29 objects.
    """
    # Color Name.
    cn = ['red', 'green', 'b', 'tan', 'magenta',
          'black', 'white', 'cyan', 'yellow', 'teal']

    # You can edit the jpg1_str later. -> Here I am testing it only on one image.
    for jpg1_str in [imageList]:
        print('jpg_str:', jpg1_str)
        for object_id, row in DF[DF.image == jpg1_str].iterrows():

            xmin = row.xmin
            xmax = row.xmax
            ymin = row.ymin
            ymax = row.ymax
            # Might be unnecessary but I am keeping it here for a while + better speed performance. (To be checked later.)
            width = row.width
            height = row.height

            # I print the object_id and height and width of each object here. ( Or bounding Box.)
            print('object_id: '+str(object_id), "objWidth: " +
                  str(width), "objHeight: "+str(height))

            input_image = Image.open(JPGPATH + jpg1_str)
            # print(input_image)  # Test to see if the image is being read.

            for index in range(len(classes)):
                if row.label == classes[index]:
                    print("classes[index]: ", classes[index])
                    # msg = classes[index]
                    # w, h = draw.textsize(msg)
                    # edgecolor = cn[index]
                    # draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
                    # draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)

                    imcr = input_image.crop((xmin, ymin, xmax, ymax))  # Test
                    imcr.show()  # Test

                    # creating the binary mask for Anitolio.
                    renameIt = jpg1_str[:-4]
                    imcr.save(
                        str(object_id)+"_"+str(classes[index])+"_"+renameIt+'.png')

        #    output_image.save("Final" + str(jpg1_str)+'.png') # creating the binary mask for Anitolio.


cropper(im)
