# Libraries
import pandas as pd
from PIL import Image,ImageDraw,ImageFont # Explained Bellow.
    # https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
    # http://effbot.org/imagingbook/introduction.html

# Read a comma-separated values (.csv) file into DataFrame.
DF = pd.read_csv('./Data/Annotations/FL_Keys_Coral-export.csv') # From code 1.
print(DF.label.unique()) # From code 1.

JPGImagesPATH = './Data/vott-csv-export/JPGImages/' # From code 2.
jpg1_str = '3D_L0215_161.jpg' # From code 2.

# Color Name.
cn = ['red','g','b','tan','m','k','w','c','y','teal']
    #https://python-graph-gallery.com/python-colors/
# Different Classes.
classes = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral', 'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']

"""
# Label Dictionary
lb_dic={"Past":cn[0],"Gorgonia":cn[1],'SeaRods':cn[2],'Antillo':cn[3],'Fish':cn[4],'Ssid':cn[5],'Orb':cn[6],'Other_Coral':cn[7],'Apalm':cn[8],'Galaxaura':cn[9]}
print(lb_dic.keys())
print(lb_dic.values())
"""

# GOAL IS: Plot the image BEFORE and AFTER the bouding Box.
input_image = Image.open(str(JPGImagesPATH)+str(jpg1_str))

# (outside of the loop).
input_image.show(title = "input image")
#Image.save(output_image,"input_image") # https://stackoverflow.com/questions/26379027/using-pillows-image-save-function-throws-an-attributeerror-when-trying-to-dow

""" Visualizing it later on.
font_size = 14
font = ImageFont.truetype("arial.ttf", font_size)
"""

draw = ImageDraw.Draw(input_image)

# Iterating over the img for multiple objects.
for _,row in DF[
DF.image == jpg1_str].iterrows(): # _ is the object number, for example in 3D_L0215_161.jpg we have 29 objects.
    
    xmin = row.xmin
    xmax = row.xmax
    ymin = row.ymin
    ymax = row.ymax

    width = row.xmax - row.xmin
    height = row.ymax - row.ymin
    print('object_id: '+str(_),"width: "+str(width),"height: "+str(height))

    if row.label == classes[0]:
        print(classes[0]) # tested.
        msg = classes[0]
        w, h = draw.textsize(msg)

        edgecolor = cn[0]
        draw.rectangle((xmin,xmax,ymin,ymax), outline=edgecolor) # not tested yet
        draw.text((( (width-w)/2),(height-h)/2), text=msg, fill='white')

    elif row.label == classes[1]:
        print(classes[1]) # tested.
        edgecolor = cn[1]

    elif row.label == classes[2]:
        print(classes[2]) # tested.
        edgecolor = cn[2]

    elif row.label == classes[3]:
        print(classes[3]) # tested.
        edgecolor = cn[3]

    elif row.label == classes[4]:
        print(classes[4]) # tested.
        edgecolor = cn[4]

    elif row.label == classes[5]:
        print(classes[5]) # tested.
        edgecolor = cn[5]

    elif row.label == classes[6]:
        print(classes[6]) # tested.
        edgecolor = cn[6]

    elif row.label == classes[7]:
        print(classes[7]) # tested.
        edgecolor = cn[7]

    elif row.label == classes[8]:
        print(classes[8]) # tested.
        edgecolor = cn[8]

    elif row.label == classes[9]:
        print(classes[9]) # tested.
        edgecolor = cn[9]

    # print('*'*66)

# (outside of the loop) Ploting the image after bouding box.
output_image = input_image
output_image.show(title = "output image")
#Image.save(output_image,"output_image") # https://stackoverflow.com/questions/26379027/using-pillows-image-save-function-throws-an-attributeerror-when-trying-to-dow