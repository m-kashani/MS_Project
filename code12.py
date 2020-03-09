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
DF = pd.read_csv('./Data/Annotations/FL_Keys_Coral-export.csv') # Used in code 2 as well

print(DF.head(5)) # Looking at the first 5 rows to get the insigt on the data.
print(DF.label.unique())

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
#jpgfile.show()

# How many images do I have?
print(DF['image'].nunique())
	
# How many objects in each images exist?
print(DF['image'].value_counts())

num = 20
pd.DataFrame(DF['image'].value_counts().head(num)).to_csv('top_'+str(num)+'.csv') #Small fix is needed here. (later)

print(DF['image'].value_counts().head(20))
top_5_list = ['A_3D_L0646_144.jpg','3D_L0622_176.jpg','3R010215_829.jpg','B_3D_L0647_42.jpg','3D_L0622_139.jpg']

# How many classes do we have in label?
print(DF['label'].value_counts()[:])


########  Visualization:
cn = ['red','green','blue','tan','magenta','black','white','cyan','yellow','teal']

plt.figure(figsize=(18,8))
plt.title('Number of differet objects')
plt.xlabel('Classes')
plt.ylabel('Numbers')

# https://stackoverflow.com/questions/51058053/how-to-plot-a-histogram-of-one-column-colored-by-another-in-python
# build a histogram for the same class breaks as earlier chart
n, bins, patches = plt.hist(DF['label'], bins=len(cn))

# apply the same color for each class to match the map
idx = 0
for c, p in zip(bins, patches):
    plt.setp(p, 'facecolor', cn[idx])
    idx+=1

plt.show()