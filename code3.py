# Libraries
import pandas as pd
from PIL import Image, ImageDraw, ImageFont  # Explained Bellow.
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

CSV_PATH = "./Data/Annotations/FL_Keys_Coral-export.csv"
JPGImagesPATH = './Data/vott-csv-export/JPGImages/'

# Color Name.
cn = ['red', 'green', 'blue', 'tan', 'magenta',
      'black', 'white', 'cyan', 'yellow', 'teal']
# https://python-graph-gallery.com/python-colors/


def makeDF(csv_path):
    """ Read a comma-separated values (.csv) file into DataFrame.
    Arg: csv PATH:
    Return: new DF.
    """
    DF = pd.read_csv(csv_path)

    DF['height'] = DF.apply(lambda DF: abs(DF['ymax'] - DF['ymin']), axis=1)
    DF['width'] = DF.apply(lambda DF: abs(DF['xmax'] - DF['xmin']), axis=1)
    DF['objArea'] = DF.apply(lambda DF: (DF['width'] * DF['height']), axis=1)
    imageArea = 2704 * 1524
    DF['objPortion'] = DF.apply(lambda DF: (DF['objArea'] / imageArea), axis=1)

    # DF.to_csv('/NewDF.csv')
    DF.to_json('json_annot_all.json')

    # Looking at the first 5 rows to get the insigt on the data.
    print(DF.head(5))
    print(DF.label.unique())
    return DF


def _boxMsg(imageList):
    def _insideIfBoxMsg(category_id):
        print(classes[category_id])  # tested.
        msg = classes[category_id]
        w, h = draw.textsize(msg)

        edgecolor = cn[category_id]
        draw.rectangle((xmin, ymin, xmax, ymax), outline=edgecolor, width=3)
        # TODO: <Modify> the object's size -> Scale of the Box size. ? >
        draw.text(((xmin + (width-w)/2), ymin+(height-h)/2),
                  text=msg, fill=edgecolor)

    for jpeg_str in imageList:
        # GOAL IS: Plot the image BEFORE and AFTER the bouding Box.
        input_image = Image.open(str(JPGImagesPATH)+str(jpeg_str))

        # (outside of the loop).
        # input_image.show(title = "input image")
        # Image.save(output_image,"input_image") # https://stackoverflow.com/questions/26379027/using-pillows-image-save-function-throws-an-attributeerror-when-trying-to-dow

        """ Visualizing it later on.
        font_size = 14
        font = ImageFont.truetype("arial.ttf", font_size)
        """

        draw = ImageDraw.Draw(input_image)

        # _ is the object number, for example in 3D_L0215_161.jpg we have 29 objects.
        for obj_id, row in DF[DF.image == jpeg_str].iterrows():

            xmin = row.xmin
            xmax = row.xmax
            ymin = row.ymin
            ymax = row.ymax

            width = row.xmax - row.xmin
            height = row.ymax - row.ymin
            print('object_id: '+str(obj_id + 2), "width: " +
                  str(width), "height: "+str(height))

            for category_id in range(len(classes)):
                if row.label == classes[category_id]:
                    _insideIfBoxMsg(category_id)

        # (outside of the loop) Ploting the image after bouding box.
        output_image = input_image
        output_image.show(title="output image")

        output_image.save('./BG/'+jpeg_str[:-4]+'_BGtruth.jpeg')


def _sortedImages():
    return pd.DataFrame(DF['image'].value_counts()).reset_index()['index'].to_numpy(dtype=list)


down5 = ['3D_L0443_21.jpg', '3D_L0443_36.jpg',
         '3D_L0441_41.jpg', '3D_L0457_97.jpg', '3D_L0453_119.jpg']

if __name__ == '__main__':
    DF = makeDF(csv_path=CSV_PATH)  # Test.
    # print(DF.label.unique()) # From code 1. #FIXME: IT's not sorted as the Detectron2 is sorted.

    # Different Classes copied from code! -> Detectron2.
    classes = ['Past', 'Gorgonia', 'SeaRods', 'Antillo', 'Fish',
               'Ssid', 'Orb', 'Other_Coral', 'Apalm', 'Galaxaura']

    im = _sortedImages()[:]
    # im = down5
    _boxMsg(imageList=im)
