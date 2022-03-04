#!/usr/bin/env python

import sys
import numpy as np

curr_cen = None

for line in sys.stdin:
    dataline = line.strip().split()
    img = np.asarray(dataline).astype(int)
    cen = img[0]
    count = img[1]

    if curr_cen == None:
        curr_count = count
        curr_sum = img[2:]
        curr_cen = cen
    elif curr_cen == cen:
        # Summing points in the same cluster
        curr_sum += img[2:]
        curr_count += count
    else:
        # Print out the new centroids: cen + pixel
        avg = ' '.join([str(round(float(pixel)/curr_count, 3)) for pixel in curr_sum])
        print '%s\t%s' % (str(curr_cen), avg)

        curr_count = count
        curr_sum = img[2:]
        curr_cen = cen

# Print out the new centroids
avg = ' '.join([str(round(pixel/curr_count, 3)) for pixel in curr_sum])
print '%s\t%s' % (str(curr_cen), avg)

