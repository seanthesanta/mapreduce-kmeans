#!/usr/bin/env python

import numpy as np
import math
import pickle

with open('old_cens.pkl', 'rb') as f:
    old_cens = pickle.load(f)

# Convert new_cens to numpy array, and dump it to pkl file
new_cens = {}
with open("new_cens", 'r') as f:
    for line in f.readlines():
        dataline = line.strip().split()
        cen = int(dataline[0])
        new_cens[cen] = np.asarray(dataline[1:]).astype(float)
# If centroids not updated
for cen in old_cens:
    if cen not in new_cens:
        new_cens[cen] = old_cens[cen]

# Write new centroids to pickle file
with open('new_cens.pkl', 'wb') as f:
    pickle.dump(new_cens, f)

# Calculate total distance between corresponding old and new centroids
diff = 0
for cen in new_cens:
    v1 = new_cens[cen]
    v2 = old_cens[cen]
    diff += math.sqrt(np.dot(v1-v2, v1-v2))

# Logging the diff
with open("diff.log", 'a+') as f:
    f.write(str(diff) + '\n')

# Set stopping threshold
THRESHOLD = 30

# If diff falls below given threshold, stop
if diff <= THRESHOLD:
    print 'STOP'

