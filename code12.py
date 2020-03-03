"""
#Code 1:
#Author: Mahdi Kashani
#mahdi@uga.edu
#Title: Libraries and reading the .csv file provided by doctor Hopkinson from the original dataset.
"""

# Libraries
import pandas as pd
import matplotlib.pyplot as plt
#% import matplotlib inline # It's not necessary cause I use conda and not Jupyter Notebook here.
from matplotlib import patches #? https://matplotlib.org/3.1.1/api/patches_api.html
	
# Read a comma-separated values (.csv) file into DataFrame.
train = pd.read_csv('./Data/vott-csv-export/FL_Keys_Coral-export.csv') # Used in code 2 as well
# print(train.head(5)) # Looking at the first 5 rows to get the insigt on the data.
print(train.label.unique())

"""
#Code 2:
#Author: Mahdi Kashani
#mahdi@uga.edu
#Title: # reading single image using imread function of matplotlib

"""
from PIL import Image #http://effbot.org/imagingbook/introduction.html

JPGImagesPATH = './Data/vott-csv-export/JPGImages/' # Used in code 3
jpg1_str = '3D_L0215_161.jpg' #Used in code 3

jpgfile = Image.open(str(JPGImagesPATH)+str(jpg1_str)) #.convert('RGBA')

# Printing the size, shape and the format of each image. (in bits, (width,length), jpeg/png/jpg ... ?
print(jpgfile.bits,'= bits |', jpgfile.size,'= shape |', jpgfile.format,'= imageType')
jpgfile.show()

# How many images do I have?
print(train['image'].nunique())
	
# How many objects in each images exist?
print(train['image'].value_counts())

# How many classes do we have in label?
print(train['label'].value_counts())