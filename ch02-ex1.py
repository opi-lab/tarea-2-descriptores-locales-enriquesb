# -*- coding: utf-8 -*-
"""
Modify the function for matching Harris corner points to also take a maximum
pixel distance between points for them to be considered as correspondences, in
order to make matching more robust.
"""

import os
from PIL import Image
from numpy import *
from pylab import *
import harris



def match_mod(desc1,desc2,locs1,locs2,max_dist,threshold=0.5,):
    """ For each corner point descriptor in the first image,
    select its match to second image using
    normalized cross-correlation. """
    
    n = len(desc1[0])
    
    # pair-wise distances
    d = -ones((len(desc1),len(desc2)))
    for i in range(len(desc1)):
        for j in range(len(desc2)):
            if linalg.norm(locs1[i]-locs2[j]) <= max_dist:
                d1 = (desc1[i] - mean(desc1[i])) / std(desc1[i])
                d2 = (desc2[j] - mean(desc2[j])) / std(desc2[j])
                ncc_value = sum(d1 * d2) / (n-1)
                if ncc_value > threshold:
                    d[i,j] = ncc_value
                
                
    ndx = argsort(-d)
    matchscores = ndx[:,0]
    
    return matchscores

def match_twosided_mod(desc1,desc2,locs1,locs2,max_dist,threshold=0.5):
    """ Two-sided symmetric version of match(). """
    
    matches_12 = match_mod(desc1,desc2,locs1,locs2,max_dist,threshold)
    matches_21 = match_mod(desc2,desc1,locs2,locs1,max_dist,threshold)
    
    ndx_12 = where(matches_12 >= 0)[0]
    
    # remove matches that are not symetric
    for n in ndx_12:
        if matches_21[matches_12[n]] != n:
            matches_12[n] = -1
            
    return matches_12



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
matches = match_twosided_mod(d1,d2,filtered_coords1,filtered_coords2,400,0.5)

figure()
gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
show()



