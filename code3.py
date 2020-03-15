# Libraries
import pandas as pd
from PIL import Image,ImageDraw,ImageFont # Explained Bellow.
    # https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
    # http://effbot.org/imagingbook/introduction.html

# Read a comma-separated values (.csv) file into DataFrame.
DF = pd.read_csv('./Data/Annotations/FL_Keys_Coral-export.csv') # From code 1.
#print(DF.label.unique()) # From code 1.

JPGImagesPATH = './Data/vott-csv-export/JPGImages/' # From code 2.
#jpg1_str = '3D_L0215_161.jpg' # From code 2.

# Color Name.
cn = ['red','green','blue','tan','magenta','black','white','cyan','yellow','teal']
    #https://python-graph-gallery.com/python-colors/
# Different Classes.
classes = ['Past', 'SeaRods', 'Apalm', 'Antillo', 'Other_Coral', 'Fish', 'Galaxaura', 'Orb', 'Gorgonia', 'Ssid']

#    """
#    # Label Dictionary
#    lb_dic={"Past":cn[0],"Gorgonia":cn[1],'SeaRods':cn[2],'Antillo':cn[3],'Fish':cn[4],'Ssid':cn[5],'Orb':cn[6],'Other_Coral':cn[7],'Apalm':cn[8],'Galaxaura':cn[9]}
#    print(lb_dic.keys())
#    print(lb_dic.values())
#    """

imagelist1 = ['A_3D_L0646_144.jpg','3D_L0622_176.jpg','3R010215_829.jpg','3D_L0622_139.jpg','B_3D_L0647_42.jpg'] # First 'Antillo', 'Other_Coral' -> Magenta + cyan + white + yellow + red + green
imagelist2 = ['3L040215_322.jpg','B_3D_L0647_127.jpg','3D_L0622_91.jpg','3D_L0622_150.jpg','3D_L0453_49.jpg'] 
imagelist3 = ['3D_L0453_283.jpg','B_3D_L0647_160.jpg','3D_L0623_38.jpg','3L010215_778.jpg','B_3D_L0647_488.jpg'] # First 'Apalm' Observed here. -> Color Blue
imagelist4 = ['A_3D_L0646_394.jpg','3D_L0215_202.jpg','3D_L0623_59.jpg','C_3D_L0648_194.jpg','A_3D_L0646_263.jpg']

down5 = ['3D_L0443_21.jpg','3D_L0443_36.jpg','3D_L0441_41.jpg','3D_L0457_97.jpg','3D_L0453_119.jpg']

imagelist = down5

print(imagelist) # Test


def _insideIf(category_id):
    print(classes[category_id]) # tested.
    msg = classes[category_id]
    w, h = draw.textsize(msg)

    edgecolor = cn[category_id]
    draw.rectangle((xmin,ymin,xmax,ymax), outline=edgecolor,width=3)
    draw.text(((xmin+ (width-w)/2),ymin+(height-h)/2), text=msg, fill=edgecolor)


for jpeg_str in imagelist:
    jpg1_str=jpeg_str

    # GOAL IS: Plot the image BEFORE and AFTER the bouding Box.
    input_image = Image.open(str(JPGImagesPATH)+str(jpg1_str))

    # (outside of the loop).
    #input_image.show(title = "input image")
    #Image.save(output_image,"input_image") # https://stackoverflow.com/questions/26379027/using-pillows-image-save-function-throws-an-attributeerror-when-trying-to-dow

    """ Visualizing it later on.
    font_size = 14
    font = ImageFont.truetype("arial.ttf", font_size)
    """

    draw = ImageDraw.Draw(input_image)

    # Iterating over the img for multiple objects.
    _ = 0
    for _,row in DF[DF.image == jpg1_str].iterrows(): # _ is the object number, for example in 3D_L0215_161.jpg we have 29 objects.
        
        xmin = row.xmin
        xmax = row.xmax
        ymin = row.ymin
        ymax = row.ymax

        width = row.xmax - row.xmin
        height = row.ymax - row.ymin
        print('object_id: '+str(_),"width: "+str(width),"height: "+str(height))


        for category_id in range(len(classes)):
            if row.label == classes[category_id]:
                _insideIf(category_id)

    # (outside of the loop) Ploting the image after bouding box.
    output_image = input_image
    output_image.show(title = "output image")

    output_image.save(jpg1_str+'_a.jpeg')
