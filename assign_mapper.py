#!/usr/bin/env python

import numpy as np
import math
import sys

def euclid_dist(v1, v2):
    return math.sqrt(np.dot(v1-v2, v1-v2))

# Get the list of final centroids
cens = {}
with open('final_cens', 'r') as f:
    for line in f.readlines():
        dataline = line.strip().split()
        cens[int(dataline[0])] = np.asarray(dataline[1:]).astype(float)

#import fileinput
#for line in fileinput.input('sample_images'):
for line in sys.stdin:
    dataline = line.strip().split()
    number = dataline[0]
    dataline = dataline[1:]
    img = np.asarray(dataline).astype(int)

    # Get the closest centroid
    min_dist = 1e10 # Magic number for inf
    for i, cen in cens.items():
        dist = euclid_dist(cen, img)
        if dist < min_dist:
            min_dist = dist
            assigned_cen = i
    
    print '%s\t%s' % (number, str(assigned_cen))

