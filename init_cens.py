#!/usr/bin/env python

import numpy as np
import pickle

def init_centroids(k = 37, dim = 28*28):
    cens = {}
    for i in range(k):
        cens[i] = np.random.uniform(low=0, high=256, size=(dim,))
    return cens

init_cens = init_centroids()
with open('init_cens.pkl', 'wb') as f:
    pickle.dump(init_cens, f)

