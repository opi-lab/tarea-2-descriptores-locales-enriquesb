# -*- coding: utf-8 -*-

import os
from PIL import Image
from numpy import *
from pylab import *
import harris

im1 = array(Image.open(os.path.abspath("data/cuaderno_1.jpg")).convert('L'))
im2 = array(Image.open(os.path.abspath("data/cuaderno_2.jpg")).convert('L'))

wid = 50
harrisim = harris.compute_harris_response(im1,5)
filtered_coords1 = harris.get_harris_points(harrisim,wid+1,0.2)
d1 = harris.get_descriptors(im1,filtered_coords1,wid)

harrisim = harris.compute_harris_response(im2,5)
filtered_coords2 = harris.get_harris_points(harrisim,wid+1,0.2)
d2 = harris.get_descriptors(im2,filtered_coords2,wid)

print('starting matching')
matches = harris.match_twosided(d1,d2)

figure()
gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
show()

