# Preprocessing
import pandas as pd
from PIL import Image,ImageDraw,ImageFont
import cv2
import numpy as np
from PIL import Image

# Path and image names.
JPGImagesPATH = './Data/vott-csv-export/JPGImages/'
jpg1_str = 'A_3D_L0646_144.jpg'

#im_cv = cv2.imread(str(JPGImagesPATH)+str(jpg1_str))

#cv2.imwrite(str(JPGImagesPATH)+str(jpg1_str), im_cv)
#pil_img = Image.fromarray(im_cv)
#pil_img.save('preprocessing'+str(jpg1_str)+'.jpg')

 ## Simplest color balancing
    # https://gist.github.com/hobson/e3b8805a558d974d48336e133dfb2bbd#file-simple_cb-py

""" White balance (color balance)
Adjust colors to flatten color histogram peaks and broaden color spectrum for better color contrast.
This is also sometimes called white balancing or probability distribution whitening.
References:
  - Color balance algorithm in [OpenCV](http://www.morethantechnical.com/2015/01/14/simplest-color-balance-with-opencv-wcode/)
  - Ported to python by [DavidYKay](https://github.com/DavidYKay)
  - Optimized (`O(N^2)` -> `O(N)`) by @alxrsngartn funded in part by NSF grant number 1722399 to [Aira](http://github.com/aira) (@jmeyers-aira)
  - Incorporated into [nlpia](github.com/aira/nlpia) by @hobson
 
Dependencies:
  - Python >= 2.7.8
  - OpenCV == 2.4.10
"""
import numpy as np
import cv2


def apply_mask(matrix, mask, fill_value):
    masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
    return masked.filled()


def apply_threshold(matrix, low_value, high_value):
    low_mask = matrix < low_value
    matrix = apply_mask(matrix, low_mask, low_value)

    high_mask = matrix > high_value
    matrix = apply_mask(matrix, high_mask, high_value)

    return matrix


def simple_colorbalance(img, percent):
    """ Applies Simple Color balancing to RBG image
    Args:
      img: numpy array of an image in RGB space
      percent: [0, 100], cutoff value for light and dark pixels
    Returns:
      Color balanced image
    Examples:
      Flatten (broaden) the color histogram for a cup of coffee photo.
      >>> from skimage.data import coffee
      >>> img = coffee()
      >>> img.std().round(0)
      74.0
      >>> x = simple_colorbalance(img, 9)
      >>> x.std().round(0)
      80.0
    """
    assert img.shape[2] == 3
    assert 0 <= percent <= 100

    half_percent = percent / 200

    channels = cv2.split(img)

    out_channels = []
    for channel in channels:
        assert len(channel.shape) == 2
        # find the low and high precentile values (based on the input percentile)
        height, width = channel.shape[:2]
        vec_size = width * height
        flat = channel.reshape(vec_size)

        assert len(flat.shape) == 1

        low_val = np.percentile(flat, half_percent * 100)
        high_val = np.percentile(flat, (1 - half_percent) * 100)

        # saturate below the low percentile and above the high percentile
        thresholded = apply_threshold(channel, low_val, high_val)

        # scale the channel
        normalized = cv2.normalize(thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX)
        out_channels.append(normalized)

    return cv2.merge(out_channels)


if __name__ == '__main__':
    import doctest
    doctest.testmod()