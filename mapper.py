#!/usr/bin/env python
import sys
import numpy as np
import math
import pickle

def euclid_dist(v1, v2):
    return math.sqrt(np.dot(v1-v2, v1-v2))

# Get the list of old centroids
with open('old_cens.pkl', 'rb') as f:
    cens = pickle.load(f)

partial_sum = {}

for line in sys.stdin:
    dataline = line.strip().split()
    # First element is only for numbering the images
    img = np.asarray(dataline[1:]).astype(int)

    # Get the closest centroid
    min_dist = 1e10 # Magic number for inf
    for i, cen in cens.items():
        dist = euclid_dist(img, cen)
        if dist < min_dist:
            min_dist = dist
            assigned_cen = i
    
    # Add the current sample to the partial sum
    if assigned_cen not in partial_sum:
        partial_sum[assigned_cen] = {'count': 1, 'img': img}
    else:
        partial_sum[assigned_cen]['count'] += 1
        partial_sum[assigned_cen]['img'] += img

# Print the partial sums from this mapper
for cen in partial_sum:
    img = ' '.join([str(pixel) for pixel in partial_sum[cen]['img']])
    print '%s\t%s %s' % (str(cen), str(partial_sum[cen]['count']), img)

