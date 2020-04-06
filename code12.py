"""
# Code 1:
# Author: Mahdi Kashani
# mahdi@uga.edu
# Title: Libraries and reading the .csv file provided by doctor Hopkinson from the original dataset.
# I can preprocess the whole csv file here and calculate width, height using the lambda function.
"""
# Libraries
# % import matplotlib inline # It's not necessary cause I use conda and not Jupyter Notebook here.
# ? https://matplotlib.org/3.1.1/api/patches_api.html

from matplotlib import patches
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image  # http://effbot.org/imagingbook/introduction.html

CSV_PATH = "./Data/Annotations/FL_Keys_Coral-export.csv"


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
    print(DF.info())
    return DF


DF = makeDF(csv_path=CSV_PATH)  # Test.

"""
# Code 2:
# Author: Mahdi Kashani
# mahdi@uga.edu
# Title: # reading single image using imread function of matplotlib
"""
JPGPATH = './Data/vott-csv-export/JPGImages/'


def _sortedImages():

    return pd.DataFrame(DF['image'].value_counts()).reset_index()['index'].to_numpy(dtype=list)


top_5_list = _sortedImages()[0:5]
top_5to10_list = _sortedImages()[5:10]
top_10to15_list = _sortedImages()[10:15]
# TODO: Reading a random image from the above directory or just reading the first image.
jpg1_str = '3D_L0215_161.jpg'

jpgfile = Image.open(str(JPGPATH)+str(jpg1_str))  # .convert('RGBA') Code4.py

# Printing the size, shape and the format of each image. (in bits, (width,length), jpeg/png/jpg ... ?
print(jpgfile.bits, '= bits ||', jpgfile.size,
      '= shape ||', jpgfile.format, '= imageType')
# jpgfile.show()

# How many images do I have?
print(DF['image'].nunique())

# How many objects in each images exist?
print(DF['image'].value_counts())


print(top_10to15_list)

# How many classes do we have in label?
print(DF['label'].value_counts()[:])

# Visualization:
cn = ['red', 'green', 'blue', 'tan', 'magenta',
      'black', 'white', 'cyan', 'yellow', 'teal']

plt.figure(figsize=(18, 8))
plt.title('Number of differet objects')
plt.xlabel('Classes')
plt.ylabel('Numbers')

# https://stackoverflow.com/questions/51058053/how-to-plot-a-histogram-of-one-column-colored-by-another-in-python
# Build a histogram for the same class breaks as earlier chart
n, bins, patches = plt.hist(DF['label'], bins=len(cn))

# Apply the same color for each class to match the map
idx = 0
for c, p in zip(bins, patches):
    plt.setp(p, 'facecolor', cn[idx])
    idx += 1

plt.show()
# FIXME: Histogram needed to be right in the middle.
