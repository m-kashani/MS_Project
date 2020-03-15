# .csv to .json on 5 images.

# Libraries.
import pandas as pd

# Color Name.
cn = ['red','green','b','tan','magenta','black','white','cyan','yellow','teal']
    #https://python-graph-gallery.com/python-colors/
# Different Classes.
classes = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral', 'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']

# Path + Image Name.
path = '/home/mahdi/Desktop/MasterProject/Data/vott-csv-export/JPGImages/'

im_0 = '3D_L0441_41.jpg' # 4 objects lowest 3

#im_1 = 'A_3D_L0646_144.jpg'
#next4 = ['3D_L0622_176.jpg','3R010215_829.jpg','3D_L0622_139.jpg','B_3D_L0647_42.jpg']

im = im_0

# Read a comma-separated values (.csv) file into DataFrame.
DF = pd.read_csv('../Data/Annotations/FL_Keys_Coral-export.csv') # From code 1.

#'''
imageArea = 2704 * 1524
DF['height'] = DF.apply(lambda DF: abs(DF['ymax'] - DF['ymin']), axis = 1)
DF['width'] = DF.apply(lambda DF: abs(DF['xmax'] - DF['xmin']), axis = 1)
DF['objArea'] = DF.apply(lambda DF: (DF['width'] * DF['height']),axis = 1)
DF['objPortion'] = DF.apply(lambda DF: (DF['objArea'] / imageArea),axis = 1)
#'''
#print(DF[DF['image']==im]) # test.

''' result:
               image         xmin         ymin         xmax         ymax    label
366  3D_L0441_41.jpg  1771.904437   922.258702  1984.163823  1184.253859     Ssid
367  3D_L0441_41.jpg  1336.311263    93.837394  1687.000683   274.650953  Antillo
368  3D_L0441_41.jpg  1395.374744  1147.353133  1519.038908  1304.181220  Antillo
369  3D_L0441_41.jpg  1194.189761   483.399516  1380.608874   758.050469  Antillo
'''

NewDF = DF[DF['image']==im]
NewDF.to_json('json_annotation.json') # Just a sample example of pandas to_json() method.
print(NewDF)

# How many classes do we have in label?
print(NewDF['label'].value_counts()[:])
''' result:
Antillo    3
Ssid       1
'''

################################# From code 3 We have:
imagelist = [im]
from PIL import Image,ImageDraw,ImageFont
for jpeg_str in imagelist:
    jpg1_str=jpeg_str

    # GOAL IS: Plot the image BEFORE and AFTER the bouding Box.


    # Iterating over the img for multiple objects.
    for _,row in DF[DF.image == jpg1_str].iterrows(): # _ is the object number, for example in 3D_L0215_161.jpg we have 29 objects.
        
        xmin = row.xmin
        xmax = row.xmax
        ymin = row.ymin
        ymax = row.ymax
        width = row.width
        height = row.height

        print('object_id: '+str(_),"width: "+str(width),"height: "+str(height))

        input_image = Image.open(str(path)+str(jpg1_str))

        draw = ImageDraw.Draw(input_image)
        output_image = input_image
        
        if row.label == classes[0]:
            print(classes[0])
            msg = classes[0]
            w, h = draw.textsize(msg)

            edgecolor = cn[0]
            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)
        elif row.label == classes[1]:
            print(classes[1])
            msg = classes[1]
            w, h = draw.textsize(msg)

            edgecolor = cn[1]
            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)
        elif row.label == classes[2]:
            print(classes[2])
            msg = classes[2]
            w, h = draw.textsize(msg)

            edgecolor = cn[2]
            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)
        elif row.label == classes[3]: # Antillo
            print(classes[3])
            msg = classes[3]
            w, h = draw.textsize(msg)

            edgecolor = cn[3]
#            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
#            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)
            
            imcr = input_image.crop((xmin,ymin,xmax,ymax)) # Test
            imcr.show() # Test

            output_image.save(str(_)+"_"+str(classes[3])+"_"+str(jpg1_str[:-4])+'.png') # creating the binary mask for Anitolio.
        elif row.label == classes[4]:
            print(classes[4])
            msg = classes[4]
            w, h = draw.textsize(msg)

            edgecolor = cn[4]
            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)
        elif row.label == classes[5]:
            print(classes[5])
            msg = classes[5]
            w, h = draw.textsize(msg)

            edgecolor = cn[5]
            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)
        elif row.label == classes[6]:
            print(classes[6])
            msg = classes[6]
            w, h = draw.textsize(msg)

            edgecolor = cn[6]
            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)
        elif row.label == classes[7]:
            print(classes[7])
            msg = classes[7]
            w, h = draw.textsize(msg)

            edgecolor = cn[7]
            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)
        elif row.label == classes[8]:
            print(classes[8])
            msg = classes[8]
            w, h = draw.textsize(msg)

            edgecolor = cn[8]
            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)
        elif row.label == classes[9]: # Ssid
            print(classes[9])
            msg = classes[9]
            w, h = draw.textsize(msg)

            edgecolor = cn[9]
#            draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
#            draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)

            imcr = input_image.crop((xmin,ymin,xmax,ymax)) # Test
            imcr.show() # Test

            output_image.save(str(_)+"_"+str(classes[9])+"_"+str(jpg1_str[:-4])+'.png') # Creating the binary mask for the Ssid.

        # print('*'*66)


#    output_image.save("Final" + str(jpg1_str)+'.png') # creating the binary mask for Anitolio.


# The goal is to create to convert the 

