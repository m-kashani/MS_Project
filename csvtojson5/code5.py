# .csv to .json on 5 images.

path = '/home/mahdi/Desktop/MasterProject/Data/vott-csv-export/JPGImages/'

# im_0 = '3D_L0441_41.jpg' # 4 objects lowest 3

im_1 = 'A_3D_L0646_144.jpg'
#next4 = ['3D_L0622_176.jpg','3R010215_829.jpg','3D_L0622_139.jpg','B_3D_L0647_42.jpg']

# Libraries
import pandas as pd

# Read a comma-separated values (.csv) file into DataFrame.
DF = pd.read_csv('../Data/Annotations/FL_Keys_Coral-export.csv') # From code 1.

print(DF[DF['image']==im_1]) # test.
''' result:
1881
.
.
.
1938
'''

NewDF = DF[DF['image']==im_1] # test.
# print(NewDF)

# How many classes do we have in label?
print(NewDF['label'].value_counts()[:])
''' result:
Galaxaura    51
Antillo       3
Ssid          1
Fish          1
'''

# The goal is to create to convert the 

